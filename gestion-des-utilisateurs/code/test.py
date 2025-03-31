import requests

url = 'https://www.example.com'
response = requests.get(url)

print(f"Code d'état : {response.status_code}")
print(f"En-têtes de réponse : {response.headers}")

# Afficher la date et l'heure dans un format personnalisé
