import requests
import json

url2 = 'http://127.0.0.1:5007/Vulnerability'
url3 = 'http://127.0.0.1:5007/Vulnerability/7'

js = [
    {
        "id": 1,
        "VulnerabilityID": "CVE-2021-3156",
        "PkgName": "sudo",
        "InstalledVersion": "1.8.31",
        "FixedVersion": "1.9.5p2",
        "Severity": "CRITICAL",
        "Title": "Sudo - Heap-based Buffer Overflow in sudoedit (CVE-2021-3156)",
        "Description": "A heap-based buffer overflow in sudoedit in sudo before 1.9.5p2 allows privilege escalation to root via a crafted command line.",
        "References": "https://nvd.nist.gov/vuln/detail/CVE-2021-3156"
    }
]

import requests
import json

# URL du serveur où tu veux envoyer la requête PUT
url = 'http://localhost:5007/Vulnerability/6'  # Remplace par l'URL appropriée

# Données JSON que tu veux mettre à jour
data = {
    "id": 6,
    "VulnerabilityID": "CVE-2020-1472",
    "PkgName": "samba",
    "InstalledVersion": "4.10.18",
    "FixedVersion": "4.10.20",
    "Severity": "CRITICAL",
    "Title": "Samba - Zerologon Vulnerability (CVE-2020-1472)",
    "Description": "An elevation of privilege vulnerability exists in the Netlogon Remote Protocol (MS-NRPC) which allows attackers to impersonate domain controllers.",
    "References": "https://nvd.nist.gov/vuln/detail/CVE-2020-1472"
}

# Effectuer la requête PUT avec les données
response = requests.put(url, json=data)

# Vérifier la réponse
if response.status_code == 200:
    print('Vulnérabilité mise à jour avec succès')
    print(response.json())  # Afficher la réponse JSON du serveur
