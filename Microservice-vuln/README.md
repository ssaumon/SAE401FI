Voici une version mise à jour du README en prenant en compte l'ajout du nouveau point d'API `/Vulnerability/sbom/CVE` :

---

# Vulnerability MicroService

## SAE401 - DevCloud - Document de Conception MicroService Vulnerability

### Gestion des vulnérabilités
**Responsable : Killian CHESNOT**

| API REST | Méthode | Description | Code |
|----------|---------|-------------|-------------|
| **GET /Vulnerability** | `ListerAjouter()` | Affiche toutes les vulnérabilités. | **200** : Succès <br> **500** : Erreur lors de la lecture du fichier JSON |
| **POST /Vulnerability** | `ListerAjouter()` | Ajoute une ou plusieurs vulnérabilités. | **200** : Ajout réussi <br> **400** : Données invalides ou champs manquants <br> **422** : L'ID existe déjà |
| **PUT /Vulnerability** | `ListerAjouter(data)` | Modifie une vulnérabilité en récupérant automatiquement son ID. | **200** : Mise à jour réussie <br> **500** : Erreur de lecture de la base de données <br> **404** : Aucune vulnérabilité avec cet ID |
| **GET /Vulnerability/int:id_Vuln** | `rechSupModID(id_Vuln)` | Récupère les données d’une vulnérabilité par ID. | **200** : Retourne la vulnérabilité correspondante <br> **404** : Aucune vulnérabilité avec cet ID <br> **500** : Erreur de lecture de la base de données |
| **DELETE /Vulnerability/int:id_Vuln** | `rechSupModID(id_Vuln)` | Supprime les données d’une vulnérabilité par ID. | **200** : Suppression réussie <br> **500** : Vulnérabilité non supprimée |
| **PUT /Vulnerability/int:id_Vuln** | `rechSupModID(id_Vuln)` | Modifie les données d’une vulnérabilité par son ID. | **200** : Mise à jour réussie <br> **404** : Aucune vulnérabilité avec cet ID <br> **500** : Erreur de lecture de la base de données |
| **POST /Vulnerability/sbom** | `traitement()` | Récupère le nom du package et sa version, puis retourne les vulnérabilités associées. | **200** : Retourne les vulnérabilités correspondant au SBOM <br> **404** : Aucune vulnérabilité correspondante trouvée <br> **400** : Clés manquantes dans l'entrée JSON |
| **GET /Vulnerability/sbom/int:idSbom** | `getSbomTrait(idSbom)` | Reçoit un ID SBOM et effectue une requête vers le microservice SBOM pour retourner les vulnérabilités associées. | **200** : Retourne les vulnérabilités associées au SBOM <br> **404** : Aucune vulnérabilité correspondante trouvée <br> **400** : Clés manquantes dans les données récupérées <br> **500** : Erreur de lecture de la base de données <br> **420** : Erreur de liaison du microservice |
| **POST /Vulnerability/sbom/CVE** | `recherche()` | Récupère les vulnérabilités associées à un package et une version via une requête à la NVD. | **200** : Retourne les vulnérabilités correspondantes <br> **400** : Clés manquantes dans l'entrée JSON <br> **505** : Erreur lors de la requête CVE |

---

### Description du MicroService

Ce microservice sert de base de données de vulnérabilités et utilise un fichier JSON comme format de stockage. À travers les différents points d'API, il est possible de :

- **Lister les vulnérabilités** : Obtenez toutes les vulnérabilités stockées.
- **Ajouter une ou plusieurs vulnérabilités** : Envoyer un ou plusieurs éléments pour ajout.
- **Modifier une vulnérabilité** : Vous pouvez modifier les données d'une vulnérabilité en récupérant automatiquement son ID sans avoir à le spécifier explicitement dans le chemin de l'URL.
- **Supprimer une vulnérabilité** : Supprimer une vulnérabilité via son ID.

En outre, le service peut interagir avec d'autres microservices via deux points d'API :

1. **POST /Vulnerability/sbom** : Accepte un JSON contenant le nom du package et la version installée. Le microservice compare ces données avec les informations dans la base de données et retourne les vulnérabilités associées à ces packages.
2. **GET /Vulnerability/sbom/int:idSbom** : Permet de consulter un SBOM spécifique en injectant son ID dans une requête vers le microservice SBOM, et retourne les vulnérabilités associées à ce SBOM.

### Nouveau Point d'API `/Vulnerability/sbom/CVE`

Ce nouveau point d'API permet de récupérer les vulnérabilités associées à un package et à sa version spécifique en interrogeant le National Vulnerability Database (NVD). Il prend en entrée un JSON avec les clés suivantes :

- `PkgName` : Le nom du package.
- `InstalledVersion` : La version installée du package.

L'API va ensuite effectuer une requête vers l'API NVD en utilisant le nom du package et la version fournis. Elle retourne les vulnérabilités associées à ces informations.

**Exemple d'entrée JSON :**
```json
{
    "PkgName": "openssl",
    "InstalledVersion": "1.1.1"
}
```

**Exemple de réponse JSON :**
```json
{
    "format": "NVD_CVE",
    "resultsPerPage": 1,
    "startIndex": 0,
    "timestamp": "2025-04-02T15:14:05.632",
    "totalResults": 1,
    "version": "2.0",
    "vulnerabilities": [
        {
            "cve": {
                "configurations": [
                    {
                        "nodes": [
                            {
                                "cpeMatch": [
                                    {
                                        "criteria": "cpe:2.3:a:openvpn:openvpn:*:*:*:*:*:*:*:*",
                                        "matchCriteriaId": "3DCBC37F-7869-42AE-B343-456FC9416C90",
                                        "versionEndExcluding": "2.4.12",
                                        "versionStartIncluding": "2.1.0",
                                        "vulnerable": true
                                    },
                                    {
                                        "criteria": "cpe:2.3:a:openvpn:openvpn:*:*:*:*:*:*:*:*",
                                        "matchCriteriaId": "964D0D5A-F643-40FB-A051-E9DC5F859A1C",
                                        "versionEndExcluding": "2.5.6",
                                        "versionStartIncluding": "2.5.0",
                                        "vulnerable": true
                                    }
                                ],
                                "negate": false,
                                "operator": "OR"
                            }
                        ]
                    },
                    {
                        "nodes": [
                            {
                                "cpeMatch": [
                                    {
                                        "criteria": "cpe:2.3:o:fedoraproject:fedora:34:*:*:*:*:*:*:*",
                                        "matchCriteriaId": "A930E247-0B43-43CB-98FF-6CE7B8189835",
                                        "vulnerable": true
                                    },
                                    {
                                        "criteria": "cpe:2.3:o:fedoraproject:fedora:36:*:*:*:*:*:*:*",
                                        "matchCriteriaId": "5C675112-476C-4D7C-BCB9-A2FB2D0BC9FD",
                                        "vulnerable": true
                                    }
                                ],
                                "negate": false,
                                "operator": "OR"
                            }
                        ]
                    },
                    {
                        "nodes": [
                            {
                                "cpeMatch": [
                                    {
                                        "criteria": "cpe:2.3:o:debian:debian_linux:9.0:*:*:*:*:*:*:*",
                                        "matchCriteriaId": "DEECE5FC-CACF-4496-A3E7-164736409252",
                                        "vulnerable": true
                                    }
                                ],
                                "negate": false,
                                "operator": "OR"
                            }
                        ]
                    }
                ],
                "cveTags": [],
                "descriptions": [
                    {
                        "lang": "en",
                        "value": "OpenVPN 2.1 until v2.4.12 and v2.5.6 may enable authentication bypass in external authentication plug-ins when more than one of them makes use of deferred authentication replies, which allows an external user to be granted access with only partially correct credentials."
                    },
                    {
                        "lang": "es",
                        "value": "OpenVPN versiones 2.1 hasta v2.4.12 y versión v2.5.6, puede permitir una omisión de autenticación en los complementos de autenticación externa cuando más de uno de ellos hace uso de las respuestas de autenticación diferida, lo que permite que sea concedido acceso a un usuario externo con credenciales sólo parcialmente correctas"
                    }
                ],
                "id": "CVE-2022-0547",
                "lastModified": "2024-11-21T06:38:53.400",
                "metrics": {
                    "cvssMetricV2": [
                        {
                            "acInsufInfo": false,
                            "baseSeverity": "HIGH",
                            "cvssData": {
                                "accessComplexity": "LOW",
                                "accessVector": "NETWORK",
                                "authentication": "NONE",
                                "availabilityImpact": "PARTIAL",
                                "baseScore": 7.5,
                                "confidentialityImpact": "PARTIAL",
                                "integrityImpact": "PARTIAL",
                                "vectorString": "AV:N/AC:L/Au:N/C:P/I:P/A:P",
                                "version": "2.0"
                            },
                            "exploitabilityScore": 10.0,
                            "impactScore": 6.4,
                            "obtainAllPrivilege": false,
                            "obtainOtherPrivilege": false,
                            "obtainUserPrivilege": false,
                            "source": "nvd@nist.gov",
                            "type": "Primary",
                            "userInteractionRequired": false
                        }
                    ],
                    "cvssMetricV31": [
                        {
                            "cvssData": {
                                "attackComplexity": "LOW",
                                "attackVector": "NETWORK",
                                "availabilityImpact": "HIGH",
                                "baseScore": 9.8,
                                "baseSeverity": "CRITICAL",
                                "confidentialityImpact": "HIGH",
                                "integrityImpact": "HIGH",
                                "privilegesRequired": "NONE",
                                "scope": "UNCHANGED",
                                "userInteraction": "NONE",
                                "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                                "version": "3.1"
                            },
                            "exploitabilityScore": 3.9,
                            "impactScore": 5.9,
                            "source": "nvd@nist.gov",
                            "type": "Primary"
                        }
                    ]
                },
                "published": "2022-03-18T18:15:12.017",
                "references": [
                    {
                        "source": "security@openvpn.net",
                        "tags": [
                            "Vendor Advisory"
                        ],
                        "url": "https://community.openvpn.net/openvpn/wiki/CVE-2022-0547"
                    },
                    {
                        "source": "security@openvpn.net",
                        "tags": [
                            "Vendor Advisory"
                        ],
                        "url": "https://community.openvpn.net/openvpn/wiki/SecurityAnnouncements"
                    },
                    {
                        "source": "security@openvpn.net",
                        "tags": [
                            "Mailing List",
                            "Third Party Advisory"
                        ],
                        "url": "https://lists.debian.org/debian-lts-announce/2022/05/msg00002.html"
                    },
                    {
                        "source": "security@openvpn.net",
                        "url": "https://lists.fedoraproject.org/archives/list/package-announce%40lists.fedoraproject.org/message/GFXJ35WKPME4HYNQCQNAJHLCZOJL2SAE/"
                    },
                    {
                        "source": "security@openvpn.net",
                        "url": "https://lists.fedoraproject.org/archives/list/package-announce%40lists.fedoraproject.org/message/R36OYC5SJ6FLPVAYJYYT4MOJ2I7MGYFF/"
                    },
                    {
                        "source": "security@openvpn.net",
                        "tags": [
                            "Patch",
                            "Vendor Advisory"
                        ],
                        "url": "https://openvpn.net/community-downloads/"
                    },
                    {
                        "source": "af854a3a-2127-422b-91ae-364da2661108",
                        "tags": [
                            "Vendor Advisory"
                        ],
                        "url": "https://community.openvpn.net/openvpn/wiki/CVE-2022-0547"
                    },
                    {
                        "source": "af854a3a-2127-422b-91ae-364da2661108",
                        "tags": [
                            "Vendor Advisory"
                        ],
                        "url": "https://community.openvpn.net/openvpn/wiki/SecurityAnnouncements"
                    },
                    {
                        "source": "af854a3a-2127-422b-91ae-364da2661108",
                        "tags": [
                            "Mailing List",
                            "Third Party Advisory"
                        ],
                        "url": "https://lists.debian.org/debian-lts-announce/2022/05/msg00002.html"
                    },
                    {
                        "source": "af854a3a-2127-422b-91ae-364da2661108",
                        "url": "https://lists.fedoraproject.org/archives/list/package-announce%40lists.fedoraproject.org/message/GFXJ35WKPME4HYNQCQNAJHLCZOJL2SAE/"
                    },
                    {
                        "source": "af854a3a-2127-422b-91ae-364da2661108",
                        "url": "https://lists.fedoraproject.org/archives/list/package-announce%40lists.fedoraproject.org/message/R36OYC5SJ6FLPVAYJYYT4MOJ2I7MGYFF/"
                    },
                    {
                        "source": "af854a3a-2127-422b-91ae-364da2661108",
                        "tags": [
                            "Patch",
                            "Vendor Advisory"
                        ],
                        "url": "https://openvpn.net/community-downloads/"
                    }
                ],
                "sourceIdentifier": "security@openvpn.net",
                "vulnStatus": "Modified",
                "weaknesses": [
                    {
                        "description": [
                            {
                                "lang": "en",
                                "value": "CWE-305"
                            }
                        ],
                        "source": "security@openvpn.net",
                        "type": "Secondary"
                    },
                    {
                        "description": [
                            {
                                "lang": "en",
                                "value": "CWE-287"
                            }
                        ],
                        "source": "nvd@nist.gov",
                        "type": "Primary"
                    }
                ]
            }
        }
    ]
}
```

Si une erreur survient lors de la requête à l'API NVD, un message d'erreur avec le code `505` sera renvoyé.

### Diagramme de la représentation du MicroService Vulnérabilité

![Représentation du MicroService Vulnérabilité](Exemple.jpg)

---

## Contributors

- FI

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

---

Cette version mise à jour inclut la description du nouveau point d'API `/Vulnerability/sbom/CVE` pour récupérer les vulnérabilités via la NVD, ainsi que des informations supplémentaires sur son fonctionnement.