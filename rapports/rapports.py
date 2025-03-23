from flask import Flask, render_template
import json, requests
from pathlib import Path

app = Flask(__name__)

sbom = {}
vul = []
prj = {}
cwd= Path.cwd().joinpath("rapports")
def recup_sbom(id):
    global sbom
    #requests.get("sbom/"+id)
    with open(cwd.joinpath("exemple_sbom.json")) as f:
        sbom = json.load(f)

def recup_vul(id):
    global vul
    with open(cwd.joinpath("exemple_vulnerabilite.json"))as f:
        vul = json.load(f)

def recup_prj(id):
    global prj
    with open(cwd.joinpath("exemple_projet.json")) as f:
        prj = json.load(f)

def recup_global(id):
    recup_sbom(id)
    recup_prj(id)
    recup_vul(id)

@app.route("/")
def index():
    recup_global(10)
    return  f'''

<h1>{prj}</1>
<br>
<br>
<h2>{sbom}</h2>

<br>
<br>
<h2>{vul}</h2>

'''
app.run()