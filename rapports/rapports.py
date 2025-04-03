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
    sbom = {}
    requ=requests.get("http://consult-sbom:5000/sbom/"+id)
    if requ.status_code==200:
        sbom = json.loads(requ.text)
    return requ.status_code



def recup_vul(id):
    global vul
    vul = []
    requ=requests.get("http://vuln:5000/Vulnerability/sbom/"+id)
    if requ.status_code==200:
        vul = json.loads(requ.text)
    return requ.status_code


def recup_prj(id):
    global prj
    prj = {}
    requ=requests.get("http://gestion_projet:5000/projet/json/"+id)
    if requ.status_code==200:
        prj = json.loads(requ.text)
    return requ.status_code


def recup_global(id):
    recup_vul(id)
    if recup_sbom(id) != 200:
        return"sbom non importé", 400
    if recup_prj(id) != 200:
        return"projet non importé", 401
    else : return "recuperation complétée", 200


@app.route("/pdf/<id>")
def pdf(id):
    if recup_global(id)[1] ==400:
        return "sbom non importé", 400
    elif recup_global(id)[1] ==401:
        return "projet non importé", 401
    try:
        os.system("rm mon_fichier.pdf")
    except:
        print("pas de fichier de ce nom")

    pdf=FPDF()
    pdf.add_page()



    pagehtml = render_template("rapport.html",vul=vul,prj=prj,sbom=sbom)

    pdf.write_html(pagehtml)
    pdf.output("mon_fichier.pdf")
    return send_file("mon_fichier.pdf"), 200

#app.run()
