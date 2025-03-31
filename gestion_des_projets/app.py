from flask import Flask, request, render_template, redirect, json
import json
import requests

app = Flask(__name__)

page_login = "Page Login à Faire ultérieurement"

user={}
perm=[]

def open_project_file():
    try:
        with open('ap.json', 'r') as pr:
            return json.load(pr)
    except FileNotFoundError:
        with open('ap.json', 'w') as pr:
            json.dump({}, pr)
        return {}
    
def save_project_file(dico):
    with open('ap.json', 'w') as pr:
        json.dump(dico,pr)

@app.route("/homepage")
def bienvenue():
    global perm
    global user
    projets = open_project_file()
    lstid= [permission["project_id" ] for permission in perm if permission['read']== True]
    lstprojet={}
    for projet in projets:
        if projet in lstid:
            lstprojet[projet] = projets[projet]
    return render_template("index.html", projets=lstprojet, user=user)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login/login', methods=["POST"])
def checklogin():
    global user
    global perm
    mail = request.form.get('mail')
    pswd= request.form.get('password')
    content = {'email':mail, 'password':pswd}
    r = requests.post("http://user/login", data=content)
    if r.status_code == 201:
        user = requests.get(f"http://user/user/{mail}")
        perm =  requests.get("http://user//permissions-by-email/{email}")
        return redirect("/homepage")
    else :
        return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)

@app.route('/projet/<id>')
def get_project(id):
    global perm
    projets = open_project_file()
    for permission in perm:
        if permission['read']==True and permission["project_id"]==str(id):
            return render_template("detail.html", projets=projets[str(id)], perm=perm[0])
    return "Petit chenapant c'est interdit"

@app.route('/projet/add', methods=["POST"])
def add_project():
    global user
    global perm
    projects= open_project_file()
    idp=len(projects)+1
    nom = request.form.get('name')
    description = request.form.get('description')
    projects[str(idp)]={"id":idp, "nom":nom, "description":description}
    permprojet= { "project_id": str(idp), "email": user["email"], "write": True,  "read": True, "admin": True}
    r= requests.post('http://user/add-permissions', data = permprojet)
    perm.append(permprojet)
    save_project_file(projects)
    return redirect("/homepage")

@app.route('/projet/update', methods=["POST"])
def update_project():
    global user
    global perm
    projects= open_project_file()
    lstid= [permission["project_id"] for permission in perm if permission['write']== True]
    idp = request.form.get('id')
    nom = request.form.get('name')
    if idp in lstid:
        description = request.form.get('description')
        projects[str(idp)]={"id":idp, "nom":nom, "description":description}
        save_project_file(projects)
        return redirect("/homepage")


@app.route('/projet/delete/<id>')
def remove_project(id):
    global user
    global perm
    lstid= [permission["project_id" ] for permission in perm if permission['admin']== True]
    if id in lstid:
        projects= open_project_file()
        del projects[str(id)]
        save_project_file(projects)
        return redirect("/homepage")
    return "vous n'avez pas les droits de supressions"

@app.route("/projet/projet/adduser", methods=['POST'])
def ajouter_user():
    mail = request.form.get('email')
    idproj = request.form.get('id')
    auth= request.form.getlist('permissions')
    lecture=True if "read" in auth else False
    ecriture=True if "write" in auth else False
    admin = True if "admin" in auth else False

    permprojet= { "project_id": str(idproj), "email": mail, "write": ecriture,  "read": lecture, "admin": admin}
    r= requests.post('http://user/add-permissions', data = permprojet)
    return redirect(f"/projet/{idproj}")


@app.route("/register")
def enre():
    return render_template("register.html")


@app.route("/register/send", methods=['POST'])
def send_user():
    donnee= request.form.to_dict()
    r=requests.post('http://user/register', data= donnee)
    return redirect("/")