import requests
import json

url = 'http://127.0.0.1:5007/Vulnerability'

js = [
    {
        "id": 2,
        "VulnerabilityID": "CVE-2021-4034",
        "PkgName": "polkit",
        "InstalledVersion": "0.105-26",
        "FixedVersion": "0.105-31",
        "Severity": "CRITICAL",
        "Title": "Polkit - Local Privilege Escalation in pkexec (CVE-2021-4034)",
        "Description": "A local privilege escalation vulnerability in polkit's pkexec utility allows unprivileged users to gain root privileges on the system.",
        "References": "https://nvd.nist.gov/vuln/detail/CVE-2021-4034"
    },
    {
        "id": 3,
        "VulnerabilityID": "CVE-2022-0847",
        "PkgName": "linux-kernel",
        "InstalledVersion": "5.10.0",
        "FixedVersion": "5.10.102",
        "Severity": "HIGH",
        "Title": "Linux Kernel - Dirty Pipe Privilege Escalation (CVE-2022-0847)",
        "Description": "The Dirty Pipe vulnerability allows local users to overwrite data in read-only files, leading to privilege escalation in Linux kernel versions 5.8 and higher.",
        "References": "https://nvd.nist.gov/vuln/detail/CVE-2022-0847"
    },
    {
        "id": 4,
        "VulnerabilityID": "CVE-2021-44228",
        "PkgName": "log4j",
        "InstalledVersion": "2.14.1",
        "FixedVersion": "2.15.0",
        "Severity": "CRITICAL",
        "Title": "Apache Log4j - Remote Code Execution via JNDI (CVE-2021-44228)",
        "Description": "A remote code execution vulnerability exists in Apache Log4j versions 2.0-beta9 to 2.14.1 via improper deserialization of user input in the JNDI lookup feature.",
        "References": "https://nvd.nist.gov/vuln/detail/CVE-2021-44228"
    },
    {
        "id": 5,
        "VulnerabilityID": "CVE-2022-2327",
        "PkgName": "glibc",
        "InstalledVersion": "2.31",
        "FixedVersion": "2.31-13+deb11u3",
        "Severity": "MEDIUM",
        "Title": "glibc - Buffer Overflow in getcwd() (CVE-2022-2327)",
        "Description": "A buffer overflow in getcwd() in glibc before version 2.34 can cause applications to crash or execute arbitrary code.",
        "References": "https://nvd.nist.gov/vuln/detail/CVE-2022-2327"
    },
    {
        "id": 6,
        "VulnerabilityID": "CVE-2020-1472",
        "PkgName": "samba",
        "InstalledVersion": "4.10.18",
        "FixedVersion": "4.10.20",
        "Severity": "CRITICAL",
        "Title": "Samba - Zerologon Vulnerability (CVE-2020-1472)",
        "Description": "An elevation of privilege vulnerability exists in the Netlogon Remote Protocol (MS-NRPC) which allows attackers to impersonate domain controllers.",
        "References": "https://nvd.nist.gov/vuln/detail/CVE-2020-1472"
    },
    {
        "id": 7,
        "VulnerabilityID": "CVE-2022-42889",
        "PkgName": "apache-commons-text",
        "InstalledVersion": "1.9",
        "FixedVersion": "1.10.0",
        "Severity": "CRITICAL",
        "Title": "Apache Commons Text - Arbitrary Code Execution (CVE-2022-42889)",
        "Description": "Apache Commons Text versions 1.5 through 1.9 are vulnerable to arbitrary code execution when untrusted input is passed to certain string interpolation features.",
        "References": "https://nvd.nist.gov/vuln/detail/CVE-2022-42889"
    }
]

x = requests.post(url, json=js)
print(x)