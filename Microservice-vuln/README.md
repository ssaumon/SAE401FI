
# Vulnerability MicroService

# SAE401 - DevCloud - Document de Conception MicroService Vulnerability


## Gestion des vulnérabilités
**Responsable : Killian CHESNOT**

| API REST | Méthode | Description | Code |
|----------|---------|-------------|-------------|
| **GET /Vulnerability** | `ListerAjouter()` | Affiche toutes les vulnérabilité | **200** : Succès <br> **500** : Erreur lors de la lecture du fichier JSON |
| **POST /Vulnerability** | `ListerAjouter()` | Ajouter un ou plusieurs Vulnérabilités | **200** : Ajout Réussi <br> **400** : Données invalides ou champs manquants <br> **422** : L'ID existe déjà |
| **PUT /Vulnerability** | `ListerAjouter(data)` | Modification d'une Vulnérabilité en récupérant automatiquement son ID|**200** : Mise à jour réussie. <br> **500** : Erreur de lecture de la base de données <br> **404** :  Aucune vulnérabilité avec cet ID |
| **GET /Vulnerability/int:id_Vuln** | `rechSupModID(id_Vuln)` | Récupère les données d’une vulnérabilité par ID | **200** : Retourne la vulnérabilité correspondante <br> **404** : Aucune vulnérabilité avec cet ID <br> **500**: Erreur de lecture de la base de données| 
| **DELETE /Vulnerability/int:id_Vuln** | `rechSupModID(id_Vuln)` | Supprime les données d’une vulnérabilité par ID | **200** : Suppression réussie <br> **500** : Vulnérabilité non supprimé |
| **PUT /Vulnerability/int:id_Vuln** | `rechSupModID(id_Vuln)` | Modifie les données d’une vulnérabilité par son ID | **200** : Mise à jour réussie <br> **404** :  Aucune vulnérabilité avec cet ID <br> **500**: Erreur de lecture de la base de données |
| **POST /Vulnerability/sbom** | `traitement()` | Récupère le Nom du Package et sa version, cela retourne les vulnérabilités associés | **200** :Retourne les vulnérabilités correspondant au SBOM <br> **404** :  Aucune vulnérabilité correspondante trouvée <br> **400** : Clés manquantes dans l'entrée JSON |
| **GET /Vulnerability/sbom/int:idSbom** | `getSbomTrait(idSbom)` | Reçois un ID SBOM et effectue une requête vers le Microservice SBOM pour retourner les vulnérabilités associés | **200** :Retourne les vulnérabilités associées au SBOM <br> **404** :  Aucune vulnérabilité correspondante trouvée <br> **400** : Clés manquantes dans les données récupérées <br> **500**: Erreur de lecture de la base de données <br> **420**: Erreur de liaison du microservice |

---
Ce microservice va servir de base de données de vulnerabilité, nous avons cette base de données au format json. Atravers les differents chemin possible dans l'url nous pouvons lister les vulnerabilités, en afficher une precisement modifier une vulnerabilité automatiquement sans preiser dans le chemin son id cest a dire que le microservice va recuperer automatiquement lid pour modifier les informations en recuperant automatiquement l'id. Nous pouvons aussi les supprime en fonction de l'id. En ce qui concerne les jonctions entre les microservices nous avons deux chemin interessannt pour les autre micro service il sagit du post d'un json au format pkgname et versioninstalled qui seront recuperer puis comparer au sein de la base de données. Si une vulnerabilité est trouvé pour le ou les packages envoyer il retournera les vulnerabilité associer. Nous avons le dernier chemin ou, nous pouvons preciser un id qui sera reinjecter dans une requete pour consulter un sbom en particulier sur consult-sbom. Il retournera ensuite les vulnerabilité associer au sbom.

Vous disposez egalement d'un fichier de test unitaire pour tester le microservice. Vous trouverez ce fichier ci-joint au format json. Cette batterie de test est a realiser avec postman.
---
![Représentation du MicroService Vulnérabilité](Exemple.jpg)

## Contributors

- FI

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.
