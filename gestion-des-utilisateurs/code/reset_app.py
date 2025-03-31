import json

def read_json(filename):
    try:
        with open(filename, 'r') as pr:
            return json.load(pr)
    except FileNotFoundError:
        with open(filename, 'w') as pr:
            json.dump({}, pr)
        return []
    
def write_json(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)  # Réécrire le JSON dans un format lisible
    except Exception as e:
        return(f"Erreur d'écriture dans le fichier : {e}")

    
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
# write_json(json_path_perm, b)

### test json file else recreate id
a = read_json(json_path_usr)
# print(a)
if a is None:
    
    write_json(json_path_usr, json_user1)
try:
    # Tente de charger la chaîne en tant que JSON
    aa = json.loads(a)
    print(aa)
except (ValueError, TypeError) as e:
    print(e)
    # Une exception indique que la chaîne n'est pas un JSON valide
    write_json(json_path_usr, json_user1)

### test json file else recreate id
b = read_json(json_path_perm)
# print(b)
if b is None:
    write_json(json_path_perm, json_perm1)
    
    
write_json(json_path_usr, a)
write_json(json_path_perm, b)
