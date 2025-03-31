from flask import Flask, render_template, send_file
import json, requests
from pathlib import Path
from fpdf import FPDF, HTMLMixin

app = Flask(__name__)

sbom = {}
vul = []
prj = {}
cwd= Path.cwd().joinpath("rapports")



def recup_sbom(id):
    global sbom
    sbom = requests.get("consult_sbom/sbom/"+id)
    #with open(cwd.joinpath("exemple_sbom.json"),encoding='UTF-8') as f:
    #    sbom = json.load(f)

def recup_vul(id):
    global vul
    vul = requests.get("vuln:5000/Vulnerability/sbom/"+id)
    #with open(cwd.joinpath("exemple_vulnerabilite.json"),encoding='UTF-8')as f:
    #    vul = json.load(f)

def recup_prj(id):
    global prj
    vul = requests.get("projet:5000/projet/"+id)
    #with open(cwd.joinpath("exemple_projet.json"),encoding='UTF-8') as f:
    #    prj = json.load(f)

def recup_global(id):
    recup_sbom(id)
    recup_prj(id)
    recup_vul(id)

@app.route("/")
def index():
    recup_global(10)
    return render_template("rapport.j2",projet=prj,sbom=sbom,vul=vul)

@app.route("/pdf/<id>")
def pdf(id):
    recup_global(id)


    pdf=FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=30)
    pdf.cell(0,30,prj["nom"],align="C",ln=1)

    pdf.set_font("Arial", size=20)
    pdf.cell(0,20,"description : ",ln=1)

    pdf.set_font("Arial", size=12)
    pdf.cell(0,20,prj["description"],ln=1)

    pdf.set_font("Arial", size=20)
    pdf.cell(0,20,f'Version : {sbom["metadata"]["component"]["version"]}',ln=1)

    pdf.cell(0,15,'Tableau de dépendances : ',ln=1)

    for v in vul:
        if str(v["id"])==id:

            pdf.set_font("Arial", size=17)
            pdf.cell(180,20,v["PkgName"]+" : "+v["InstalledVersion"],border=1,ln=1)

            pdf.set_font("Arial", size=12)
            pdf.cell(60,20,"Vulneraibilité"+" : "+v["Title"],border=1)
            pdf.cell(60,20,"Severity"+" : "+v["Severity"],border=1)
            pdf.cell(60,20,"Version fixé"+" : "+v["FixedVersion"],border=1,ln=1)

            pdf.cell(150,20,v["Description"],border=1)
            pdf.cell(30,20,v["References"],border=1,ln=1)
            pdf.ln()


    pdf.output(cwd.joinpath("mon_fichier.pdf"))
    return send_file(cwd.joinpath("mon_fichier.pdf"))

#app.run()
