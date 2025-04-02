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
| **GET** | `Get_SBOMs` | Affichage de l'ensemble des SBOMs actuellement dans la base de données | **200** : OK |
| **POST** | `Ajout_SBOM` | Ajout d'un SBOM en fournissant un nom d’application, une version, des dépendances et leurs caractéristiques | **200** : SBOM Added To The Data Base |
| **POST** | `Ajout_dependance_SBOM` | Ajout d’une dépendance à un fichier SBOM existant | **200** : Dependance Added To The SBOM <br> **404** : SBOM Not Found |
| **PATCH** | `Update_SBOM` | Modification d’une ou plusieurs données d’un fichier SBOM existant | **200** : Value Changed <br> **404** : Key Of SBOM Not Found <br> **404** : SBOM Not Found |
| **DELETE** | `Suppression_dependance_SBOM` | Suppression d’une dépendance dans un fichier SBOM | **200** : Dependance Deleted <br> **404** : Dependance Not Found <br> **404** : SBOM Not Found |
| **DELETE** | `Suppression_SBOM` | Suppression d’un fichier SBOM | **200** : SBOM Deleted <br> **404** : SBOM Not Found |

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

## Rapports

**Responsable : Simon COLLET**

| Méthode | Requête | Description | Réponse |
|---------|---------|-------------|----------|
| **GET** | `getrapport(id)` |crée le rapport a partir de l'ID passé en paramètre | **200** : OK <br> **404** : ID introuvable |

---

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

## Gestion des utilisateurs

**Responsable : Malo DURANTON**  

***Fonction utillisateur***

- Fonction pour inscrire un utilisateur  
- Fonction pour connecter un utilisateur  
- Fonction pour recuperer les info d'un utillisateur
- Fonction pour suppression un compte  
- Gestion des permissions (lecture, écriture, suppression)

***Fonction utillisateur***

- Fonction pour ajouter des permissions a un utillisateur  
- Fonction pour modifier des permissions  
- Fonction pour supprimser des permission
- Fonction pour recuperer les permissions par identifient de projet
- Fonction pour recuperer les permissions par email

**Base de données Utilisateurs :**

```json
{
   "last_name": "string",
   "first_name": "string",
   "email": "string",
   "password": "string",
   "birth_date": "string"
}

```

**Base de données des Permmissions :**

```json
{
    "project_id": "int",
    "email": "string",
    "write": "bool",
    "read": "bool",
    "admin": "bool"
}

```

**Requêtes API :**

| HTTP Méthode | Action | Description | Codes |
|--------------|--------|-------------|-------|
| **POST** | `Register` | Inscription d'un nouvel utilisateur | **200** : Utilisateur créé avec succès <br> **400** : Champ manquant <br> **411** : Un utilisateur avec cet e-mail existe déjà <br> **415** : Type de contenu invalide, JSON attendu |
| **POST** | `Login` | Connexion utilisateur | **200** : Connexion réussie <br> **400** : Champ manquant <br> **401** : Mot de passe incorrect <br> **404** : Utilisateur non trouvé <br> **415** : Type de contenu invalide, JSON attendu |
| **GET** | `User Info` | Informations utilisateur | **200** : Utilisateur trouvé <br> **409** : Utilisateur non trouvé |
| **PUT** | `Modify User` | Modifier les informations utilisateur | **200** : Informations utilisateur mises à jour <br> **400** : Requête invalide <br> **409** : Utilisateur n'existe pas |
| **DELETE** | `Delete User` | Supprimer un utilisateur | **200** : Utilisateur supprimé avec succès <br> **400** : Requête invalide |
| **POST** | `Add Permissions` | Ajouter des permissions utilisateur | **200** : Permissions ajoutées avec succès <br> **400** : Requête invalide <br> **404** : Utilisateur non trouvé <br> **409** : Permissions existent déjà |
| **PUT** | `Modify Permissions` | Modifier les permissions utilisateur | **200** : Permissions mises à jour avec succès <br> **400** : Requête invalide <br> **404** : Permissions non trouvées |
| **DELETE** | `Delete Permissions` | Supprimer les permissions utilisateur | **200** : Permissions supprimées avec succès <br> **400** : Requête invalide <br> **404** : Utilisateur ou permissions non trouvés |
| **GET** | `Permissions by Project` | Récupérer les permissions utilisateur par projet | **200** : Permissions récupérées avec succès <br> **400** : Requête invalide <br> **409** : Aucune permission trouvée pour ce projet |
| **GET** | `Permissions by Email` | Récupérer les permissions utilisateur par e-mail | **200** : Permissions récupérées avec succès <br> **400** : Requête invalide <br> **409** : Aucune permission trouvée pour cet utilisateur |

## Code Details

### Utility Functions (`fonction.py`)

#### JSON Operations

- `read_json(filename)`: Reads and validates JSON files
- `write_json(filename, data)`: Writes data to JSON files

#### User Management Functions

- `get_user_by_email(json_data, search_email)`: Finds user by email
- `modify_user_by_email(users, last_name, first_name, email, password, birth_date)`: Updates user data
- `get_user_by_email(users, email)`: Retrieves user data (without password)
- `delete_user_by_email(users, email)`: Removes user from the system

#### Permission Management Functions

- `get_permissions_by_project(json_perm, project_id)`: Gets project permissions
- `get_permissions_by_email(permissions_list, email)`: Gets user permissions
- `get_perm_email_idproject(json_perm, email_id, project_id)`: Finds specific permission

### Reset Application (`reset_app.py`)

- Initializes default data in JSON files
- Handles file creation and validation
- Provides default user and permission data

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
