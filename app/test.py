import requests
import json

url = 'http://127.0.0.1:5007/Vulnerability'

js = {
    "id": 4,
    "VulnerabilityID": "CVE-2022-0778",
    "PkgName": "openssl",
    "InstalledVersion": "1.1.1k",
    "FixedVersion": "1.1.1n",
    "Severity": "HIGH",
    "Title": "OpenSSL - Infinite Loop in BN_mod_sqrt() (CVE-2022-0778)",
    "Description": "The BN_mod_sqrt() function in OpenSSL contains a flaw that can cause an infinite loop when parsing certain ASN.1 encoded certificates, potentially leading to denial-of-service (DoS).",
    "References": "https://nvd.nist.gov/vuln/detail/CVE-2022-0778"
}
x = requests.post(url, json=js)
print(x)