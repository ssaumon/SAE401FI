import requests
import json
 
url = 'http://127.0.0.1:5000'
# url = 'http://148.60.76.67:5001'
 
 
# myobj = {'somekey': 'somevalue'}
 
 
print("test post /register")
js = {
    "last_name": "Doe3",
    "first_name": "John3",
    "email": "john.doe3@example.com",
    "password": "securepassword123",
    "birth_date": "1990-02-02"
    }
# print("Données envoyées :", json.dumps(js, indent=4))

x = requests.post(url+'/register', json=js)
if x.status_code != 201:
    print(x)
    exit(1)
     
     
print("test post /login")
js = {
      "email": "john.doe@example.com",
      "password": "securepassword123"
    }
# print("Données envoyées :", json.dumps(js, indent=4))
 
x = requests.post(url+'/login', json=js)
if x.status_code != 201:
    print(x)
    exit(1)
     
     
print("test post /modify")
js = {
    "last_name": "Does",
    "first_name": "Johns",
    "email": "john.doe3@example.com",
    "password": "securepassword123",
    "birth_date": "1990-02-02"
    }
# print("Données envoyées :", json.dumps(js, indent=4))
 
x = requests.post(url+'/modify', json=js)
if x.status_code != 201:
    print(x.content)
    exit(1)
     
     
print("test post /modify")
js = {
    "last_name": "Does",
    "first_name": "Johns",
    "email": "john.doe3@example.com",
    "password": "securepassword123",
    "birth_date": "1990-02-02"
    }
# print("Données envoyées :", json.dumps(js, indent=4))
 
x = requests.post(url+'/modify', json=js)
if x.status_code != 201:
    print(x.content)
    exit(1)
     
     
print("test post /delete-user")
js = {
    "email": "john.doe3@example.com"
    }
# print("Données envoyées :", json.dumps(js, indent=4))
 
x = requests.delete(url+'/delete-user', json=js)
if x.status_code != 201:
    print(x.content)
    exit(1)
     
     
print("Test GET /permissions-by-project/<project_id>")
project_id = "1"
x = requests.get(url+f'/permissions-by-project/{project_id}')
if x.status_code != 200:
    print("Erreur lors de la récupération des permissions:", x.json())
    exit(1)
# print("Récupération des permissions réussie:", x.json())
 
 
print("Test GET /permissions-by-email/<email>")
email = "john.doe@example.com"
x = requests.get(url+f'/permissions-by-email/{email}')
if x.status_code != 200:
    print("Erreur lors de la récupération des permissions:", x.json())
    exit(1)
# print("Récupération des permissions réussie:", x.json())