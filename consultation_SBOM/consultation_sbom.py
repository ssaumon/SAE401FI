from flask import Flask
import requests
import json
from pathlib import Path

app = Flask(__name__)
sboms= {}

def recup_sbom():
    #sboms = requests.get("URL de maxence")
    with open(Path.cwd().joinpath("exemple_sbom.json")) as f:
        sboms = json.load(f)

@app.route("/")
def index_html():
    recup_sbom()
    return sboms


app.run()

