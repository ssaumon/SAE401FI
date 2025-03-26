# SAE401 - DevCloud - Document de Conception

## Identification des micro-services

### Gestion des projets
**Responsable : Paul HOFFBECK** 

| HTTP Méthode | Action | Description | Codes |  
|-------------|--------|-------------|---------- |
| `N/A` | Display | Regroupe les projets existants | N/A |
| **POST** | `Create_Project` | Création d'un projet | **200** : OK <br> **403** : Permission refusée <br> **400** : BDD non trouvée |
| **PATCH** | `Update_Project` | Modification d'un projet | **200** : OK <br> **403** : Permission refusée <br> **400** : BDD non trouvée |
| **DELETE** | `Delete_Project` | Suppression d'un projet | **200** : OK <br> **403** : Permission refusée <br> **400** : BDD non trouvée |

**Base de Données Projet :**
```json
{
  "Nom du projet": "string",
  "Utilisateurs autorisés": [
    "user1",
    "user2"]
}
```

---

### Importation de SBOM  
**Responsable : Maxence DEBEAUVAIS**

| HTTP Méthode | Action | Description | Codes |
|-------------|--------|-------------|--------|
| **POST** | `Ajout_SBOM` | Ajout d'un SBOM en fournissant un nom d’application, une version, des dépendances et leurs caractéristiques | **200** : OK <br> **400** : Erreur d'entrée |
| **PATCH** | `Update_SBOM` | Modification d’une ou plusieurs données d’un fichier SBOM existant | **200** : Modification réussie <br> **400** : Entrée invalide <br> **404** : SBOM introuvable |
| **POST** | `Ajout_dependance_sbom` | Ajout d’une dépendance à un fichier SBOM existant | **200** : OK <br> **400** : Erreur d'entrée <br> **404** : SBOM introuvable |
| **DELETE** | `Suppression_dependance_sbom` | Suppression d’une dépendance dans un fichier SBOM | **200** : Succès <br> **404** : SBOM introuvable |
| **DELETE** | `Suppression_SBOM` | Suppression d’un fichier SBOM | **200** : Succès <br> **404** : SBOM introuvable |
```

**Base de Données SBOM :**
```json
{
 "bomFormat": "CycloneDX",
 "specVersion": "1.4",
 "serialNumber": "urn:uuid:3e016e55-f35b-41cd-b660-e6e642ecc9e5",
 "version": 1,
 "metadata": {
 "timestamp": "2023-10-01T12:00:00Z",
 "tools": [
 {
 "vendor": "CycloneDX",
 "name": "CycloneDX Core Library",
 "version": "1.4"
 }
 ],
 "component": {
 "type": "application",
 "name": "ExampleApp",
 "version": "1.0.0",
 "swid": {
 "tagId": "ExampleApp"
 }
 }
 },
 "components": [
 {
 "type": "library",
 "name": "log4j",
 "version": "2.14.1",
 "swid": {
 "tagId": "log4j"
 },
 "purl": "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1"
 },
 {
 "type": "library",
 "name": "jackson-databind",
 "version": "2.12.3",
 "swid": {
 "tagId": "jackson-databind"
 },
 "purl": "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.12.3"
 }
 ]
}
```

---

## Consultation de SBOM
**Responsable : Simon COLLET**

| Méthode | Requête | Description | Réponse |
|---------|---------|-------------|----------|
| **GET** | `consult_sbom(id)` | Récupère le fichier SBOM correspondant à `id` | **200** : OK <br> **404** : SBOM introuvable |
| **GET** | `Import_perms(id_sbom, id_user)` | Retourne les permissions relatives à l’ID du SBOM pour un utilisateur donné | **200** : OK |

---

## Gestion des vulnérabilités
**Responsable : Killian CHESNOT**

| API REST | Méthode | Description | Code |
|----------|---------|-------------|-------------|
| **POST** | `Import_JSON()` | Importation des données pour traitement | **400** : Format non pris en charge <br> **200** : Réussite |
| **POST** | `export_json()` | Export des données traitées en format JSON | **200** : Réussite |
| **POST** | `save_to_db(data)` | Envoie les données traitées vers un autre microservice (BDD) | **400** : Erreur d'import <br> **200** : Succès |
| **GET** | `get_vulnerability(id)` | Récupère les données d’une vulnérabilité par ID | **200** : OK <br> **404** : Non trouvé |

---

## Gestion des utilisateurs
**Responsable : Malo DURANTON**  
- Fonction pour inscrire un utilisateur  
- Fonction pour connecter un utilisateur  
- Fonction de déconnexion  
- Suppression de compte  
- Gestion des permissions (lecture, écriture, suppression)

**Base de données Utilisateurs :**
```json
{
  "nom": "string",
  "prenom": "string",
  "email": "string",
  "mdp": "string",
  "date_naissance": "jj-mm-yyyy",
  "permissions": {
    "read": true,
    "write": false,
    "delete": false
  }
}
```

**Requêtes API :**
```http
POST /createuser
{
  "mail": "string",
  "mdp": "string",
  "nom": "string",
  "prenom": "string",
  "date_naissance": "jj-mm-yyyy"
}

POST /connect
{
  "mail": "string",
  "mdp": "string"
}

POST /deleteuser
{
  "mail": "string"
}

POST /permission
{
  "id_user": "string",
  "permissions": {
    "read": true,
    "write": false,
    "delete": false
}
```
---

## Conteneurisation et orchestration
**Responsable :** Tout le monde

- Conteneurisation des microservices
- Orchestration des conteneurs avec Kubernetes
- Création et gestion des volumes pour les bases de données
- Intégration continue et déploiement automatique

---

## Sécurité : Authentification et permissions
- Gestion de l'authentification des utilisateurs
- Implémentation de l’authentification par token JWT
- Sécurisation des API avec des rôles et permissions spécifiques
- Gestion des logs et des rapports de sécurité

---

### Liens utiles
- [Documentation](https://foad.univ-exemple.com/docs/SAE401)

---

