from flask import Flask
import requests
import json
from pathlib import Path

app = Flask(__name__)
sboms= {}

def recup_sbom():
    global sboms
    r = requests.get("import_sbom:5000/sbom")
    if r.status_code==200:
        sboms=r
    else: 
        return "erreur import_sbom", 400
    #with open(Path.cwd().joinpath("consultation_SBOM\exemple_sbom.json")) as f:
    #    sboms = json.load(f)



@app.route("/version/<id>")
def version(id):
    if recup_sbom()[1]!=200:
        return "erreur import_sbom", 400
    li=[]
    temp_dict={}
    if id in sboms.keys():
        if "components" in sboms[id].keys():
                for el in sboms[id]["components"]:
                    if "name" in sboms[id]["components"] and "version" in sboms[id]["components"]:
                        temp_dict[el["name"]]=el["version"]
                        li.append(temp_dict)
                    else : 
                        return "SBOM mal formaté", 402
                return temp_dict, 200
        else: 
            return "SBOM mal formaté", 402
    else: 
        return "SBOM non trouvé", 404

@app.route("/sbom/<id>")
def sbom(id):
    if recup_sbom()[1]!=200:
        return "erreur import_sbom", 400
    if id in sboms.keys():
        return sboms[id], 200
    else:
        return "SBOM non trouvé", 404

#app.run()

