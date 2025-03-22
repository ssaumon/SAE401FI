from flask import *

from fonction import *

##### INIT #####

json_path_usr = 'user.json'
json_path_perm = 'permission.json'

import reset_app

json_user = read_json(json_path_usr)

json_perm = read_json(json_path_perm)

##### START #####

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')     # racine
def hello_world():
    return 'Hello, World!'

############################################################################################################################

@app.route('/register', methods=['POST'])
def register():
    global json_user 
    if request.method == 'POST':    # ajoute un bloc json 
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
        # print(data)
        # print(request)
        # json_user= []
        if last_name != "" and first_name != "" and email != "" and password != "" and birth_date != "":
            js = {
                "last_name": last_name,
                "first_name": first_name,
                "email": email,  
                "password": password,
                "birth_date": birth_date
            }
            if  get_object_by_email(json_user, email) != "":
                return jsonify({"message": "Un utilisateur avec cet e-mail existe déjà."}), 409
            json_user.append(js)
            write_json(json_path_usr,json_user)
            return jsonify({"message": "User added", "data": js}), 201
        # print("a"+id+nom+localisation+version)
        return jsonify({"error": "Tous les champs sont requis"}), 400
    
############################################################################################################################
    
@app.route('/login', methods=['POST'])
def login():
    global json_user 
    if request.method == 'POST':    # ajoute un bloc json 
        data = request.get_json()
        # print(data['id'])
        email = data['email'].strip()  # .strip() pour supprimer les espaces
        password = data['password'].strip()
        
        required_fields = ["email", "password"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Champ manquant : {field}"}), 400

        # print(data)
        # print(request)

        a = get_object_by_email(json_user, email)
        # print(a)
        if a['password']==password:
            return jsonify({"message": "User avec bon mdp"}), 201

############################################################################################################################

@app.route('/modify', methods=['POST'])
def modify():
    global json_user 
    if request.method == 'POST':    # ajoute un bloc json 
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
                return jsonify({"message": "User modify", "data": js}), 201
        # print("a"+id+nom+localisation+version)
        return jsonify({"error": "Tous les champs sont requis"}), 400

############################################################################################################################

@app.route('/delete-user', methods=['DELETE'])
def deleteuser():
    global json_user 
    if request.method == 'DELETE':    # ajoute un bloc json 
        data = request.get_json()
        # print(data['id'])
        email = data['email'].strip()
        
        required_fields = ["email"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Champ manquant : {field}"}), 400
        print(data)
        print(request)
        # json_user= []
        if email != "":
            a = delete_user_by_email(json_user, email)
            if a != "":
                return jsonify({"message": "User deleted"}), 201
        # print("a"+id+nom+localisation+version)
        return jsonify({"error": "Tous les champs sont requis"}), 400

############################################################################################################################

@app.route('/permissions', methods=['POST'])
def permissions():
    global json_user 
    if request.method == 'POST':    # ajoute un bloc json 
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
                return jsonify({"message": "User modify", "data": js}), 201
        # print("a"+id+nom+localisation+version)
        return jsonify({"error": "Tous les champs sont requis"}), 400


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
        return jsonify({"error": "Aucune permission trouvée pour ce projet"}), 404

############################################################################################################################


@app.route('/permissions-by-email/<email>', methods=['GET'])
def permissionsbyemail(email):
    email = email.strip()

    if not email:
        return jsonify({"error": "Le email est requis"}), 400

    js = get_permissions_by_email(json_perm, email)

    if js:
        return jsonify({"message": "Get permissions", "data": js}), 200
    else:
        return jsonify({"error": "Aucune permission trouvée pour ce projet"}), 404

############################################################################################################################


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
