from flask import Flask, jsonify, request
import json
from multiprocessing import Process

app_importSBOM = Flask(__name__)

db_sbom = json.load(open("base_de_donnees_sbom.json"))


index_html = """
<h1> Bienvenue dans l'accueil du Micro Service Importation SBOM</h1>
<p><strong>Voir toute les Access Points : </strong></p><a href="http://127.0.0.1:5000/sbom">GET SBOMs</a>
"""

def save_modif(new_db):
    with open("base_de_donnees_sbom.json", "w") as f:
        json.dump(new_db, f, indent=4)

@app_importSBOM.route('/') 
def accueil():
    return index_html

@app_importSBOM.route('/sbom', methods=['GET', 'POST'])
def sboms():
    if request.method == 'GET':
        return jsonify(db_sbom), 200
    if request.method == 'POST':
        sbom = request.get_json()
        db_sbom[str(len(db_sbom.keys())+1)] = sbom
        save_modif(db_sbom)
        return jsonify("SBOM Added To The Data Base"), 200

@app_importSBOM.route('/sbom/dependance/<id>', methods=['POST'])
def dependance(id):
    dependance = request.get_json()
    if id in db_sbom.keys():
        db_sbom[id]["components"].append(dependance)
        save_modif(db_sbom)
        return jsonify("Dependance Added To The SBOM"), 200
    else:
        return jsonify("SBOM Not Found"), 404

@app_importSBOM.route('/sbom/<id>/<cle>/<new_val>')
def sbom_patch(id, cle, new_val):
    if id in db_sbom.keys():
        if cle in db_sbom[id].keys():
            db_sbom[id][cle] = new_val
            save_modif(db_sbom)
            return jsonify("Value Changed"), 200
        else:
            return jsonify("Key Of SBOM Not Found"), 404
    else:
        return jsonify("SBOM Not Found"), 404

@app_importSBOM.route('/sbom/dependance/delete/<id>/<id_compo>')
def delete_dependance(id, id_compo):
    global db_sbom
    if id in db_sbom.keys():
        if int(id_compo)+1 <= len(db_sbom[id]["components"]):
            del db_sbom[id]["components"][int(id_compo)]
            save_modif(db_sbom)
            return jsonify("Dependance Deleted"), 200
        else:
            return jsonify("Dependance Not Found"), 404
    else:
        return jsonify("SBOM Not Found"), 404

@app_importSBOM.route('/sbom/delete/<id>')
def delete_sbom(id):
    global db_sbom
    if id in db_sbom.keys():
        del db_sbom[id]
        save_modif(db_sbom)
        return jsonify("SBOM Deleted"), 200
    else:
        return jsonify("SBOM Not Found"), 404

if __name__ == '__main__':

    app_importSBOM.run(host="0.0.0.0", port=5000)
""" Contenu Initial de la DB
{
"1":    {
 "bomFormat": "CycloneDX",
 "specVersion": "1.4",
 "serialNumber": "urn:uuid:3e016e55-f35b-41cd-b660-e6e642ecc9e5",
 "version": 1,
 "metadata": {
 "timestamp": "2023-10-01T12:00:00Z",
 "tools": [
 {
 "vendor": "CycloneDX",
 "name": "CycloneDX Core Library",
 "version": "1.4"
 }
 ],
 "component": {
 "type": "application",
 "name": "ExampleApp",
 "version": "1.0.0",
 "swid": {
 "tagId": "ExampleApp"
 }
 }
 },
 "components": [
 {
 "type": "library",
 "name": "log4j",
 "version": "2.14.1",
 "swid": {
 "tagId": "log4j"
 },
 "purl": "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1"
 },
 {
 "type": "library",
 "name": "jackson-databind",
 "version": "2.12.3",
 "swid": {
 "tagId": "jackson-databind"
 },
 "purl": "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.12.3"
 }
 ]
},
"2": 
{
    "test": "tst"
}
}
"""