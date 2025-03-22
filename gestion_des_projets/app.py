from flask import Flask, request, render_template, redirect, json
import json

app = Flask(__name__)

page_login = "Page Login à Faire ultérieurement"


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

@app.route('/')
def bienvenue():
    projets = open_project_file()
    return render_template("index.html", projets=projets)

@app.route('/login')
def login():
    return page_login


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/projet/<id>')
def get_project(id):
    projets = open_project_file()
    return render_template("detail.html", projets=projets[str(id)])

@app.route('/projet/add', methods=["POST"])
def add_project():
    projects= open_project_file()
    idp=len(projects)+1
    nom = request.form.get('name')
    description = request.form.get('description')
    projects[str(idp)]={"id":idp, "nom":nom, "description":description}
    save_project_file(projects)
    return redirect("/")

@app.route('/projet/update', methods=["POST"])
def update_project():
    projects= open_project_file()
    idp = request.form.get('id')
    nom = request.form.get('name')
    description = request.form.get('description')
    projects[str(idp)]={"id":idp, "nom":nom, "description":description}
    save_project_file(projects)
    return redirect("/")


@app.route('/projet/delete/<id>')
def remove_project(id):
    projects= open_project_file()
    del projects[str(id)]
    save_project_file(projects)
    return redirect("/")

