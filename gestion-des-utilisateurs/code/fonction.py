from flask import jsonify
import json
import copy

############################################################################################################################

# Fonction pour valider et lire un fichier JSON
def read_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)  # Charger le JSON dans un objet Python
        return data
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON : {e}")
        return ""
    except Exception as e:
        (f"Erreur : {e}")
        return ""
    
def write_json(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)  # Réécrire le JSON dans un format lisible
    except Exception as e:
        return(f"Erreur d'écriture dans le fichier : {e}")

############################################################################################################################

def get_object_by_email(json_data, search_email):
    search_email = str(search_email)
    for obj in json_data:
        print(obj)
        print(obj['email'])
        if str(obj['email']) == search_email:
            return obj
    return ""

def modify_user_by_email(users, last_name, first_name, email, password, birth_date):
    for user in users:
        if user['email'] == email:
            user['last_name'] = last_name
            user['first_name'] = first_name
            user['password'] = password
            user['birth_date'] = birth_date
            break  # Sortir de la boucle après modification
    return users  # Retourne toute la liste mise à jour

def get_user_by_email(users, email):
    for user in users:
        if user['email'] == email:
            user_copy = copy.deepcopy(user)
            del user_copy['password']
            return user_copy
    return ""


def delete_user_by_email(users, email):
    for user in users:
        if user["email"] == email:
            users.remove(user)
            return users  # Retourne la liste mise à jour
    return ""

############################################################################################################################

def get_permissions_by_project(json_perm, project_id: str):
    # return [perm for perm in json_perm if str(perm['project_id']) == str(project_id)]
    for perm in json_perm:
        if str(perm['project_id']) == (project_id):
            return perm
    return ""

def get_permissions_by_email(json_perm, email_id: str):
    # return [perm for perm in json_perm if str(perm['email']) == str(email_id)]
    for perm in json_perm:
        if str(perm['email']) == (email_id):
            return perm
    return ""

def get_perm_email_idproject(json_perm, email_id: str, project_id: str):
    for perm in json_perm:
        if str(perm['email']) == (email_id) and str(perm['project_id']) == (project_id) :
            return perm
    return ""



json_user1 = [
    {
    "last_name": "Doe",
    "first_name": "John",
    "email": "john.doe@example.com",
    "password": "securepassword123",
    "birth_date": "1990-01-01"
    },
    {
    "last_name": "Doe2",
    "first_name": "John2",
    "email": "john.doe2@example.com",
    "password": "securepassword123",
    "birth_date": "1990-02-02"
    }
]
# write_json(json_path_usr, a)
json_perm1 = [
    {
        "project_id": "1",
        "email": "john.doe@example.com",
        "write": True,
        "read": True,
        "admin": False
    },
    {
        "project_id": "2",
        "email": "john.doe2@example.com",
        "write": True,
        "read": True,
        "admin": False
    }
]
        
        
def purify_field(value):
    """
    Purifie un champ en s'assurant qu'il est une chaîne de caractères,
    supprime les espaces superflus et élimine les caractères indésirables.

    :param value: La valeur à purifier.
    :return: La valeur purifiée sous forme de chaîne de caractères.
    """
    if not isinstance(value, str):
        # Si la valeur n'est pas une chaîne, convertissez-la en chaîne
        value = str(value)

    # Supprimer les espaces superflus au début et à la fin
    value = value.strip()

    # Supprimer ou remplacer les caractères indésirables (exemple : supprimer les caractères non alphanumériques)
    value = ''.join(char for char in value if char.isalnum() or char.isspace())

    return value

