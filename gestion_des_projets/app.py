from flask import Flask, request, render_template, redirect, jsonify, send_file
import json
import requests

app = Flask(__name__)

user = {}
perm = []

def open_project_file():
    try:
        with open('ap.json', 'r') as pr:
            return json.load(pr)
    except FileNotFoundError:
        with open('ap.json', 'w') as pr:
            json.dump({}, pr)
        return {}
    except:
        return None

def save_project_file(dico):
    try:
        with open('ap.json', 'w') as pr:
            json.dump(dico, pr)
        return True
    except:
        return False

@app.route("/homepage")
def bienvenue():
    global perm, user
    if not user:
        return jsonify({"error": "Forbidden"}), 403
    
    projets = open_project_file()
    if projets is None:
        return jsonify({"error": "Fichier trouvé mais non exploitable"}), 415
    
    lstid = [p["project_id"] for p in perm if p['read']]
    lstprojet = {k: v for k, v in projets.items() if k in lstid}
    
    return render_template("index.html", projets=lstprojet, user=user), 200

@app.route('/')
def login():
    return render_template("login.html"), 200

@app.route('/login/login', methods=["POST"])
def checklogin():
    global user, perm
    mail = request.form.get('mail')
    pswd = request.form.get('password')
    content = {'email': mail, 'password': pswd}
    
    try:
        r = requests.post("http://user:5000/login", json=content)
    except:
        return jsonify({"error": "API Injoignable"}), 503
    
    if r.status_code == 200:
        try:
            user1 = requests.get(f"http://user:5000/user/{mail}").json()
            perm1 = requests.get(f"http://user:5000/permissions-by-email/{mail}").json()
        except:
            return jsonify({"error": "API Injoignable"}), 503
        
        user = user1.get("data", {})
        perm = perm1.get("data", [])
        return redirect("/homepage")
    else:
        return redirect('/', code=403)

@app.route('/projet/<id>')
def get_project(id):
    projets = open_project_file()
    if projets is None or id not in projets:
        return jsonify({"error": "ID Inconnu"}), 404
    
    for permission in perm:
        if permission['read'] and permission["project_id"] == str(id):
            return render_template("detail.html", projets=projets[id], perm=permission)
    
    return jsonify({"error": "Forbidden"}), 403

@app.route('/projet/json/<id>')
def get_json(id):
    projets = open_project_file()
    if projets is None or id not in projets:
        return jsonify({"error": "ID Inconnu"}), 404
    return jsonify(projets[id])

@app.route('/logout')
def logout():
    global user, perm
    user = {}
    perm = []
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
