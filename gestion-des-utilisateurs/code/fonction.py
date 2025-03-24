from flask import jsonify
import json

# Fonction pour valider et lire un fichier JSON
def read_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)  # Charger le JSON dans un objet Python
        return data
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON : {e}")
        return None
    except Exception as e:
        (f"Erreur : {e}")
        return None
    
    
if __name__ == '__main__':
    print(read_json('ap-python/ap.json'))

def write_json(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)  # Réécrire le JSON dans un format lisible
    except Exception as e:
        return(f"Erreur d'écriture dans le fichier : {e}")

    
    
if __name__ == '__main__':
    print(write_json('ap-python/ap.json','{}'))
 
   
def get_object_by_email(json_data, search_email):
    for obj in json_data:
        if obj['email'] == str(search_email):  # Vérifie si l'ID correspond
            return obj  # Retourne l'objet trouvé
    return ""  # Retourne None si l'objet n'est pas trouvé


def modify_user_by_email(users, last_name, first_name, email, password, birth_date):
    for user in users:
        if user['email'] == email:
            user['last_name'] = last_name
            user['first_name'] = first_name
            user['password'] = password
            user['birth_date'] = birth_date
            break  # Sortir de la boucle après modification
    return users  # Retourne toute la liste mise à jour

def delete_user_by_email(users, email):
    for user in users:
        if user["email"] == email:
            users.remove(user)
            return users  # Retourne la liste mise à jour
    return ""

def get_permissions_by_project(json_perm, project_id: str):
    return [perm for perm in json_perm if str(perm['project_id']) == str(project_id)]


def get_permissions_by_email(json_perm, email_id: str):
    return [perm for perm in json_perm if str(perm['email']) == str(email_id)]
