from flask import Flask
import requests
import json
from pathlib import Path

app = Flask(__name__)
sboms= {}

def recup_sbom():
    global sboms
    #sboms = requests.get("URL de maxence")
    with open(Path.cwd().joinpath("consultation_SBOM\exemple_sbom.json")) as f:
        sboms = json.load(f)



@app.route("/version/<id>")
def version(id):
    recup_sbom()
    li=[]
    temp_dict={}
    for el in sboms[id]["components"]:
        temp_dict[el["name"]]=el["version"]
        li.append(temp_dict)
    return temp_dict

@app.route("/sbom/<id>")
def sbom(id):
    recup_sbom()
    return sboms[id]

#app.run()

