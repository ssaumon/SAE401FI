import requests
import json

BASE_URL = 'http://127.0.0.1:5007'

data_vuln = {
    "id": 1,
    "VulnerabilityID": "CVE-2021-3156",
    "PkgName": "sudo",
    "InstalledVersion": "1.8.31",
    "FixedVersion": "1.9.5p2",
    "Severity": "CRITICAL",
    "Title": "Sudo - Heap-based Buffer Overflow in sudoedit (CVE-2021-3156)",
    "Description": "A heap-based buffer overflow in sudoedit in sudo before 1.9.5p2 allows privilege escalation to root via a crafted command line.",
    "References": ["https://nvd.nist.gov/vuln/detail/CVE-2021-3156"]
}

data_update_vuln = {
    "id": 6,
    "VulnerabilityID": "CVE-2020-1472",
    "PkgName": "samba",
    "InstalledVersion": "4.10.18",
    "FixedVersion": "4.10.20",
    "Severity": "CRITICAL",
    "Title": "Samba - Zerologon Vulnerability (CVE-2020-1472)",
    "Description": "An elevation of privilege vulnerability exists in the Netlogon Remote Protocol (MS-NRPC) which allows attackers to impersonate domain controllers.",
    "References": ["https://nvd.nist.gov/vuln/detail/CVE-2020-1472"]
}

data_sbom = [
    {
        "PkgName": "openssl",
        "InstalledVersion": "1.1.1"
    }
]

def test_get_vulnerabilities():
    response = requests.get(f"{BASE_URL}/Vulnerability")
    if response.status_code == 200:
        print("Vulnérabilités récupérées avec succès")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erreur: {response.status_code}")

def test_add_vulnerability():
    response = requests.post(f"{BASE_URL}/Vulnerability", json=data_vuln)
    if response.status_code == 200:
        print("Vulnérabilité ajoutée avec succès")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erreur: {response.status_code}")

def test_update_vulnerability():
    response = requests.put(f"{BASE_URL}/Vulnerability/6", json=data_update_vuln)
    if response.status_code == 200:
        print("Vulnérabilité mise à jour avec succès")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erreur: {response.status_code}")

def test_delete_vulnerability():
    response = requests.delete(f"{BASE_URL}/Vulnerability/1")
    if response.status_code == 200:
        print("Vulnérabilité supprimée avec succès")
    else:
        print(f"Erreur: {response.status_code}")

def test_get_vulnerability_by_id(vuln_id):
    response = requests.get(f"{BASE_URL}/Vulnerability/{vuln_id}")
    if response.status_code == 200:
        print(f"Vulnérabilité avec ID {vuln_id} récupérée avec succès")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erreur: {response.status_code}")

def test_post_sbom():
    response = requests.post(f"{BASE_URL}/Vulnerability/sbom", json=data_sbom)
    if response.status_code == 200:
        print("SBOM mis à jour avec succès")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erreur: {response.status_code}")

test_post_sbom()
