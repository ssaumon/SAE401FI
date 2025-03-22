import json
def write_json(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)  # Réécrire le JSON dans un format lisible
    except Exception as e:
        return(f"Erreur d'écriture dans le fichier : {e}")

    
json_path_usr = 'user.json'
json_path_perm = 'permission.json'
a = [
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
write_json(json_path_usr, a)
b = [
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
write_json(json_path_perm, b)