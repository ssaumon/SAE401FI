
from datetime import datetime

# Obtenir la date et l'heure actuelles
# Afficher la date et l'heure
print("Date et heure actuelles :", datetime.now())


## librairy
from flask import *
import copy
import time

## fichier locaux
import reset_app
from fonction import *
##### INIT #####

json_path_usr = 'user.json'
json_path_perm = 'permission.json'
json_path_log = 'logs.txt'


json_user = read_json(json_path_usr)

json_perm = read_json(json_path_perm)

##### START #####

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')     # racine
def hello_world():
    return 'Hello, World!'

############################################################################################################################

@app.route('/reset_json')     # racine
def reset_json():
    write_json(json_path_usr, json_user1)
    write_json(json_path_perm, json_perm1)
    
    global json_user, json_perm
    json_user = json_user1
    json_perm = json_perm1
    time.sleep(0.1)
    return jsonify({"message": "reset_json"}), 200

############################################################################################################################

@app.route('/register', methods=['POST'])
def register():
    global json_user
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid content type, JSON is expected"}), 415

    last_name = data.get('last_name', '').strip()
    first_name = data.get('first_name', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    birth_date = data.get('birth_date', '')

    required_fields = ["last_name", "first_name", "email", "password", "birth_date"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    if get_object_by_email(json_user, email):
        return jsonify({"message": "Un utilisateur avec cet e-mail existe déjà."}), 409

    js = {
        "last_name": last_name,
        "first_name": first_name,
        "email": email,
        "password": password,
        "birth_date": birth_date
    }
    json_user.append(js)
    write_json(json_path_usr, json_user)
    return jsonify({"message": "User added", "data": js}), 200
    
############################################################################################################################
    
@app.route('/login', methods=['POST'])
def login():
    global json_user 
    data = request.get_json()
    # print(data['id'])
    email = purify_field(data['email'])  # .strip() pour supprimer les espaces
    password = purify_field(data['password'])
    write_json(json_path_log, email)
    required_fields = ["email", "password"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

        print(json_user)
        # print(request)

        a = get_object_by_email(json_user, email)
        # print(a)
        if a != None:
            if a['password'] == password:
                return jsonify({"message": "User avec bon mdp"}), 200
    return jsonify({"error": "Tous les champs sont requis"}), 400
############################################################################################################################
    
@app.route('/user/<email>', methods=['GET'])
def user(email):
    
    # Supposons que json_user soit une liste d'utilisateurs chargée ailleurs dans votre application
    user_data = get_user_by_email(json_user, email)
    if user_data is None:
        return jsonify({"error": "Utilisateur non trouvé"}), 409
    else:
        return jsonify({"message": "Utilisateur trouvé", "data": user_data}), 200

############################################################################################################################

@app.route('/modify', methods=['POST'])
def modify():
    global json_user 
    data = request.get_json()
    # print(data['id'])
    last_name = data['last_name'].strip()  # .strip() pour supprimer les espaces
    first_name = data['first_name'].strip()
    email = data['email'].strip()
    password = data['password']
    birth_date = data['birth_date']
    
    required_fields = ["last_name", "first_name", "email", "password", "birth_date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400
    print(data)
    print(request)
    # json_user= []
    if last_name != "" and first_name != "" and email != "" and password != "" and birth_date != "":
        js = {
            "last_name": last_name,
            "first_name": first_name,
            "email": email,  
            "password": password,
            "birth_date": birth_date
        }
        if get_object_by_email(json_user, email) == "":
            return jsonify({"message": "User dosent exist"}), 409
        a = modify_user_by_email(json_user, last_name, first_name, email, password, birth_date)
        if a != "":
            json_user = a
            write_json(json_path_usr,json_user)
            return jsonify({"message": "User modify", "data": js}), 200
    # print("a"+id+nom+localisation+version)
    return jsonify({"error": "Tous les champs sont requis"}), 400

############################################################################################################################

@app.route('/delete-user/<email>', methods=['DELETE'])
def deleteuser(email):
    global json_user 
    # data = request.get_json()
    # print(data['id'])
    # email = data['email'].strip()
    
    # required_fields = ["email"]
    # for field in required_fields:
    #     if field not in data:
    if email == "":
        return jsonify({"error": f"Champ manquant"}), 400
    # print(data)
    print(request)
    # json_user= []
    if email != "":
        a = delete_user_by_email(json_user, email)
        if a != "":
            return jsonify({"message": "User deleted"}), 200

    return jsonify({"error": "Tous les champs sont requis"}), 400

############################################################################################################################

@app.route('/add-permissions', methods=['POST'])
def addpermissions():
    global json_user 
    data = request.get_json()
    # print(data['id'])
    project_id = data['project_id'].strip()  # .strip() pour supprimer les espaces
    email = data['email'].strip()
    write = data['write']
    read = data['read']
    admin = data['admin']
    
    required_fields = ["project_id", "email", "write", "read", "admin"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    if project_id == "" or email == "" or email == "" or write == "" or read == "" or admin == "":
        return jsonify({"error": "Tous les champs sont requis"}), 400

    if get_object_by_email(json_user, email) == "":
        return jsonify({"message": "User dosent exist"}), 409
    
    a = get_perm_email_idproject(json_perm, email, project_id)
    if a == None:
        js = {
            "project_id": project_id,
            "email": email,
            "write": write,
            "read": read,
            "admin": admin
        }
        json_perm.append(js)
        
        write_json(json_path_perm,json_perm)
    return jsonify({"message": "User modify", "data": "true"}), 200

############################################################################################################################

@app.route('/modify-permissions', methods=['PUT'])
def modifypermissions():
    global json_user 
    data = request.get_json()
    # print(data['id'])
    project_id = data['project_id'].strip()  # .strip() pour supprimer les espaces
    email = data['email'].strip()
    write = data['write']
    read = data['read']
    admin = data['admin']
    
    required_fields = ["project_id", "email", "write", "read", "admin"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    if project_id == "" or email == "" or email == "" or write == "" or read == "" or admin == "":
        return jsonify({"error": "Tous les champs sont requis"}), 400

    if get_object_by_email(json_user, email) == "":
        return jsonify({"message": "User dosent exist"}), 409
    
    js = {
        "project_id": project_id,
        "email": email,
        "write": write,
        "read": read,
        "admin": admin
    }
    json_perm.append(js)
    
    write_json(json_path_perm,json_perm)
    return jsonify({"message": "User modify", "data": "true"}), 200


############################################################################################################################


@app.route('/delete-permissions', methods=['DELETE'])
def delete_permissions():
    global json_user, json_perm

    project_id = request.args.get('project_id', '').strip()
    email = request.args.get('email', '').strip()

    if not project_id or not email:
        return jsonify({"error": "Tous les champs sont requis"}), 400

    if not get_object_by_email(json_user, email):
        return jsonify({"error": "L'utilisateur n'existe pas"}), 404

    for perm in json_perm:
        if perm['project_id'] == project_id and perm['email'] == email:
            json_perm.remove(perm)
            write_json(json_path_perm, json_perm)
            return jsonify({"message": "Permissions supprimées", "data": "true"}), 200

    return jsonify({"error": "Permissions non trouvées"}), 404


############################################################################################################################

@app.route('/permissions-by-project/<project_id>', methods=['GET'])
def permissionsbyproject(project_id):
    project_id = project_id.strip()

    if not project_id:
        return jsonify({"error": "Le project_id est requis"}), 400

    js = get_permissions_by_project(json_perm, project_id)

    if js:
        return jsonify({"message": "Get permissions", "data": js}), 200
    else:
        return jsonify({"error": "Aucune permission trouvée pour ce projet"}), 409

############################################################################################################################


@app.route('/permissions-by-email/<email>', methods=['GET'])
def permissionsbyemail(email):
    email = email.strip()

    if not email:
        return jsonify({"error": "Le email est requis"}), 400

    js = get_permissions_by_email(json_perm, email)

    if js != "":
        return jsonify({"message": "Get permissions", "data": js}), 200
    else:
        return jsonify({"error": "Aucune permission trouvée pour ce projet"}), 409

############################################################################################################################


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
    app.run(host='0.0.0.0', port=5000)
