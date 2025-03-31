from flask import Flask
import requests
import json
from pathlib import Path

app = Flask(__name__)
sboms= {}

def recup_sbom():
    global sboms
    sboms = json.loads(requests.get("http://import-sbom:5000/sbom").text)
    #with open(Path.cwd().joinpath("consultation_SBOM\exemple_sbom.json")) as f:
    #    sboms = json.load(f)



@app.route("/version/<id>")
def version(id):
    recup_sbom()
    li=[]
    
    for el in sboms[id]["components"]:
        temp_dict={}
        temp_dict[el["name"]]=el["version"]
        li.append(temp_dict)
    return li

@app.route("/sbom/<id>")
def sbom(id):
    recup_sbom()
    return sboms[id]
    

#app.run()

