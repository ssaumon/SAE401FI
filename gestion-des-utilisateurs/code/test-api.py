import json
import os

def read_json(filename):
    """Lit un fichier JSON et retourne son contenu sous forme de dictionnaire."""
    if not os.path.exists(filename):
        print(f"Le fichier {filename} n'existe pas.")
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON dans le fichier {filename} : {e}")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {filename} : {e}")
        return None

def write_json(filename, data):
    """Écrit un dictionnaire dans un fichier JSON avec un formatage lisible."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erreur d'écriture dans le fichier {filename} : {e}")

def clean_data(data):
    """Supprime les clés avec des valeurs None dans un dictionnaire."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    else:
        return data

json_path_usr = 'user.json'
json_path_perm = 'permission.json'

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

# Vérifier et traiter le fichier user.json
a = read_json(json_path_usr)
if a is None:
    print(f"Réécriture du fichier {json_path_usr} avec les données par défaut.")
    write_json(json_path_usr, json_user1)
else:
    a_clean = clean_data(a)
    write_json(json_path_usr, a_clean)

# Vérifier et traiter le fichier permission.json
b = read_json(json_path_perm)
if b is None:
    print(f"Réécriture du fichier {json_path_perm} avec les données par défaut.")
    write_json(json_path_perm, json_perm1)
else:
    b_clean = clean_data(b)
    write_json(json_path_perm, b_clean)
