from flask import Flask, jsonify, request
import json
from multiprocessing import Process

app_importSBOM = Flask(__name__)

db_sbom = json.load(open("base_de_donnees_sbom.json"))

index_html = """
<h1> Bienvenue dans l'accueil du Micro Service Importation SBOM</h1>
<p><strong>Voir toute les Access Points : </strong></p><a href="http://127.0.0.1:5000/sbom">GET SBOMs</a>
"""

@app_importSBOM.route('/') 
def accueil():
    return index_html

@app_importSBOM.route('/sbom', methods=['GET', 'POST'])
def sboms():
    if request.method == 'GET':
        return jsonify(db_sbom)
    if request.method == 'POST':
        sbom = request.get_json()
        db_sbom[str(len(db_sbom.keys())+1)] = sbom
        return jsonify(db_sbom)

@app_importSBOM.route('/sbom/dependance/<id>', methods=['POST'])
def dependance(id):
    dependance = request.get_json()
    return jsonify(db_sbom[id])

@app_importSBOM.route('/sbom/<id>/<cle>/<new_val>')
def sbom_patch(id, cle, new_val):
    db_sbom[id][cle] = new_val
    return jsonify(db_sbom[id])

@app_importSBOM.route('/sbom/dependance/delete/<id1>/<id2>')
def delete_dependance(id1, id2):
    global db_sbom
    del db_sbom[id1]["components"][int(id2)]
    return jsonify(db_sbom)

@app_importSBOM.route('/sbom/delete/<id>')
def delete_sbom(id):
    global db_sbom
    del db_sbom[id]
    return jsonify(db_sbom)

if __name__ == '__main__':

    p1 = Process(target=lambda: app_importSBOM.run(debug=True, port=5000))

    p1.start()

    p1.join()

"""
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