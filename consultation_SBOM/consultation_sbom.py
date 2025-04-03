from flask import Flask
import requests
import json
from pathlib import Path

app = Flask(__name__)
sboms= {}

def recup_sbom():
    global sboms
    r=requests.get("http://import-sbom:5000/sbom")
    if r.status_code==200:
        sboms = json.loads(r.text)
        return 200
    else: return 400




@app.route("/version/<id>")
def version(id):
    if recup_sbom()!=200:
        return "erreur import_sbom", 400
    li=[]
    if id in sboms.keys():
        if "components" in sboms[id]:
            for el in sboms[id]["components"]:
                if "version" in el.keys() and "name" in el.keys():
                    temp_dict={}
                    temp_dict["InstalledVersion"]=el["version"]
                    temp_dict["PkgName"]=el["name"]
                    li.append(temp_dict)
                else: return "SBOM mal formé", 402
            return li,200
        else: return "SBOM mal formé", 402
    else: return f"SBOM {id} introuvable", 404

@app.route("/sbom/<id>")
def sbom(id):
    if recup_sbom()!=200:
        return "erreur import_sbom", 400
    if id in sboms.keys():
        return sboms[id],200
    else: return "sbom introuvable", 404
    


#app.run()

