
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

    required_fields = ["last_name", "first_name", "email", "password", "birth_date"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    last_name = data['last_name']
    first_name = data['first_name']
    email = data['email']
    password = data['password']
    birth_date = data['birth_date']
    
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

    # Vérifiez que toutes les clés requises sont présentes
    required_fields = ["email", "password"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    # Purifiez les champs
    email = data['email']
    password = data['password']

    # Écrire dans le journal (à des fins de débogage)
    write_json(json_path_log, {"action": "login_attempt", "email": email})

    # Recherchez l'utilisateur par e-mail
    user = get_object_by_email(json_user, email)
    print(user)
    if user:
        # Vérifiez le mot de passe
        if user['password'] == password:
            return jsonify({"message": "Utilisateur authentifié avec succès"}), 200
        else:
            return jsonify({"error": "Mot de passe incorrect"}), 401
    else:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
############################################################################################################################
    
@app.route('/user/<email>', methods=['GET'])
def user(email):
    
    # Supposons que json_user soit une liste d'utilisateurs chargée ailleurs dans votre application
    user_data = get_user_by_email(json_user, email)
    if user_data is "":
        return jsonify({"error": "Utilisateur non trouvé"}), 409
    else:
        return jsonify({"message": "Utilisateur trouvé", "data": user_data}), 200

############################################################################################################################

@app.route('/modify', methods=['POST'])
def modify():
    global json_user 
    data = request.get_json()    
    
    required_fields = ["last_name", "first_name", "email", "password", "birth_date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400
    last_name = data['last_name']  #  pour supprimer les espaces
    first_name = data['first_name']
    email = data['email']
    password = data['password']
    birth_date = data['birth_date']
    
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
    # email = data['email']
    
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
    global json_user, json_perm
    data = request.get_json()

    # Liste des champs requis
    required_fields = ["project_id", "email", "write", "read", "admin"]

    # Vérifiez que toutes les clés requises sont présentes
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    # Vérifiez que les valeurs ne sont pas vides
    project_id = data['project_id']
    email = data['email']
    write = data['write']
    read = data['read']
    admin = data['admin']
    if project_id.strip() == "" or email.strip() == "" or write not in [True, False] or read not in [True, False] or admin not in [True, False]:
        return jsonify({"error": "Tous les champs sont requis et doivent avoir des valeurs valides"}), 402


    # Vérifiez si l'utilisateur existe
    if not get_object_by_email(json_user, email):
        return jsonify({"error": "Utilisateur inexistant"}), 404

    # Vérifiez si les permissions existent déjà
    existing_perm = get_perm_email_idproject(json_perm, email, project_id)
    if existing_perm != "":
        return jsonify({"error": "Permissions déjà existantes pour cet utilisateur et ce projet"}), 409

    # Ajoutez les nouvelles permissions
    new_permission = {
        "project_id": project_id,
        "email": email,
        "write": write,
        "read": read,
        "admin": admin
    }
    json_perm.append(new_permission)
    write_json(json_path_perm, json_perm)

    return jsonify({"message": "Permissions ajoutées avec succès"}), 200

############################################################################################################################

@app.route('/modify-permissions', methods=['PUT'])
def modifypermissions():
    global json_user, json_perm
    data = request.get_json()

    # Vérifiez que toutes les clés requises sont présentes
    required_fields = ["project_id", "email", "write", "read", "admin"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    # Récupérez et nettoyez les valeurs
    project_id = data['project_id'].strip()
    email = data['email'].strip()
    write = data['write']
    read = data['read']
    admin = data['admin']

    # Vérifiez que les valeurs ne sont pas vides ou None
    if not project_id or not email or write is None or read is None or admin is None:
        return jsonify({"error": "Tous les champs sont requis et doivent avoir des valeurs valides"}), 400

    # Vérifiez si l'utilisateur existe
    if get_object_by_email(json_user, email) == "":
        return jsonify({"error": "Utilisateur inexistant"}), 404

    # Vérifiez si les permissions existent déjà
    existing_perm = get_perm_email_idproject(json_perm, email, project_id)
    if existing_perm == "":
        return jsonify({"error": "Permissions non trouvées pour cet utilisateur et ce projet"}), 404

    # Modifiez les permissions existantes
    existing_perm['write'] = write
    existing_perm['read'] = read
    existing_perm['admin'] = admin

    write_json(json_path_perm, json_perm)
    return jsonify({"message": "Permissions modifiées avec succès"}), 200

############################################################################################################################


@app.route('/delete-permissions', methods=['DELETE'])
def delete_permissions():
    global json_user, json_perm

    # Récupérer les arguments avec des valeurs par défaut
    project_id = request.args.get('project_id', '').strip()
    email = request.args.get('email', '').strip()

    # Vérifier que les arguments requis sont présents
    if not project_id or not email:
        return jsonify({"error": "Tous les champs sont requis"}), 400

    # Vérifier si l'utilisateur existe
    if not get_object_by_email(json_user, email):
        return jsonify({"error": "L'utilisateur n'existe pas"}), 404

    # Supprimer les permissions correspondantes
    for perm in json_perm:
        if perm['project_id'] == project_id and perm['email'] == email:
            json_perm.remove(perm)
            write_json(json_path_perm, json_perm)
            return jsonify({"message": "Permissions supprimées", "data": "true"}), 200

    return jsonify({"error": "Permissions non trouvées"}), 404

############################################################################################################################

@app.route('/permissions-by-project/<project_id>', methods=['GET'])
def permissionsbyproject(project_id):
    project_id = project_id

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
    email = email

    if not email:
        return jsonify({"error": "Le email est requis"}), 400

    js = get_permissions_by_email(json_perm, email)
    print(js)
    if js != "":
        return jsonify({"message": "Get permissions", "data": js}), 200
    else:
        return jsonify({"error": "Aucune permission trouvée pour ce projet"}), 409

############################################################################################################################


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
    app.run(host='0.0.0.0', port=5000)
