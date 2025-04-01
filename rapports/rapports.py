from flask import Flask, render_template, send_file
import json, requests
from pathlib import Path
from fpdf import FPDF, HTMLMixin
import os

app = Flask(__name__)

sbom = {}
vul = []
prj = {}


cwd= Path.cwd().joinpath("rapports")



def recup_sbom(id):
    global sbom
    requ=requests.get("http://consult-sbom:5000/sbom/"+id)
    if requ.status_code==200:
        sbom = json.loads(requ.text)
    return requ.status_code



def recup_vul(id):
    global vul
    requ=requests.get("http://vuln:5000/Vulnerability/sbom/"+id)
    if requ.status_code==200:
        vul = json.loads(requ.text)
    return requ.status_code


def recup_prj(id):
    global prj
    requ=requests.get("http://gestion_projet:5000/projet/json/"+id)
    
    if requ.status_code==200:
        prj = json.loads(requ.text)
    return requ.status_code


def recup_global(id):
    recup_vul(id)
    if recup_sbom(id) != 200:
        return"sbom non importé"
    if recup_prj(id) != 200:
        return"projet non récupéré"

@app.route("/")
def index():
    recup_global(1)
    return render_template("rapport.j2",projet=prj,sbom=sbom,vul=vul)

@app.route("/pdf/<id>")
def pdf(id):
    print(recup_global(id))
    try:
        os.system("rm mon_fichier.pdf")
    except:
        print("pas de fichier de ce nom")

    pdf=FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=30)
    pdf.cell(0,30,prj["nom"],align="C",ln=1)

    pdf.set_font("Arial", size=20)
    pdf.cell(0,20,"description : ",ln=1)

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0,20,prj["description"])

    pdf.set_font("Arial", size=20)
    pdf.cell(0,20,f'Version : {sbom["metadata"]["component"]["version"]}',ln=1)

    pdf.cell(0,15,'Tableau de dépendances : ',ln=1)

    for v in vul:
        
        pdf.set_font("Arial", size=17)
        pdf.multi_cell(180,15,v["PkgName"]+" : "+v["InstalledVersion"],border=1)

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(60,15,"Vulneraibilité"+" : "+v["Title"],border=1,ln=1)
        pdf.multi_cell(60,15,"Severity"+" : "+v["Severity"],border=1,ln=1)
        pdf.multi_cell(60,15,"Version fixé"+" : "+v["FixedVersion"],border=1)

        pdf.multi_cell(150,15,v["Description"],border=1,ln=1)
        pdf.multi_cell(30,15,v["References"],border=1)
        pdf.ln()

    
    pdf.output("mon_fichier.pdf")
    return send_file("mon_fichier.pdf")

#app.run()
