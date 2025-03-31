import json
import os

def read_json(filename):
    if not os.path.exists(filename):
        return ""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON : {e}")
        return ""
    except Exception as e:
        print(f"Erreur : {e}")
        return ""

def write_json(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Erreur d'écriture dans le fichier : {e}")

json_path_usr = 'user.json'
json_path_perm = 'permission.json'
json_path_log = 'logs.txt'

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

# Test et recréation des fichiers JSON si nécessaire
a = read_json(json_path_usr)
if a is "":
    write_json(json_path_usr, json_user1)
else:
    try:
        # Vérifiez que les données sont un objet JSON valide
        aa = json.loads(json.dumps(a))
        print(aa)
    except (ValueError, TypeError) as e:
        print(f"Erreur de validation JSON : {e}")
        write_json(json_path_usr, json_user1)

b = read_json(json_path_perm)
if b is "":
    write_json(json_path_perm, json_perm1)
else:
    write_json(json_path_perm, b)

# Écriture des fichiers JSON
write_json(json_path_usr, a if a is not "" else json_user1)
write_json(json_path_perm, b if b is not "" else json_perm1)
write_json(json_path_log, "a")
