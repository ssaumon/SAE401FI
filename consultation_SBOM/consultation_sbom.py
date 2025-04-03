from flask import Flask
import requests
import json
from pathlib import Path

app = Flask(__name__)
sboms= {}

def recup_sbom():
    global sboms

    sboms = json.loads(requests.get("http://import-sbom:5000/sbom").text)




@app.route("/version/<id>")
def version(id):
    if recup_sbom()[1]!=200:
        return "erreur import_sbom", 400
    li=[]

    for el in sboms[id]["components"]:
        temp_dict={}
        temp_dict["InstalledVersion"]=el["version"]
        temp_dict["PkgName"]=el["name"]
        li.append(temp_dict)
    return li

@app.route("/sbom/<id>")
def sbom(id):
    recup_sbom()
    return sboms[id]
    


#app.run()

