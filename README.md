# SAE401 - DevCloud - Document de Conception

## Identification des micro-services

### Diagramme des communications

![Diagramme de communication](diag_com_general.png "Titre de l'image").

### Gestion des projets

**Responsable : Paul HOFFBECK**  

| HTTP Méthode | Action | Description | Codes |
|-------------|--------|-------------|----------|
| **GET** | Page de connexion | Affiche la page de connexion | 200 |
| **POST** | Authentification utilisateur | Connecte un utilisateur | 302 : Succès, redirection <br> 403 : Échec de l'authentification |
| **GET** | Page d'inscription | Affiche la page d'inscription | 200 |
| **POST** | Enregistrement utilisateur | Crée un nouvel utilisateur | 302 : Succès, redirection <br> 513 : Échec de l'enregistrement |
| **GET** | Déconnexion utilisateur | Déconnecte l'utilisateur et redirige | 302 |
| **GET** | Liste des projets | Affiche la page d'accueil avec les projets | 200 : Succès <br> 403 : Non authentifié |
| **GET** | Détails d'un projet | Affiche les détails d'un projet | 200 : Succès <br> 404 : Projet non trouvé |
| **GET** | Données JSON d'un projet | Renvoie les données JSON du projet | 200 : Succès <br> 404 : Projet non trouvé |
| **POST** | Ajouter un projet | Création d'un projet | 302 : Succès, redirection <br> 403 : Accès refusé <br> 415 : Format invalide <br> 511 : Échec des permissions <br> 512 : Échec import SBOM <br> 513 : Échec de la sauvegarde |
| **PUT** | Modifier un projet | Mise à jour d'un projet | 302 : Succès, redirection <br> 403 : Accès refusé <br> 404 : Projet non trouvé <br> 513 : Échec de la sauvegarde |
| **DELETE** | Supprimer un projet | Suppression d'un projet | 302 : Succès, redirection <br> 403 : Accès refusé <br> 404 : Projet non trouvé <br> 513 : Échec de la suppression |
| **POST** | Ajouter un utilisateur à un projet | Ajoute un utilisateur avec des permissions | 302 : Succès, redirection <br> 511 : Échec des permissions |
| **GET** | Télécharger un rapport | Récupère un fichier PDF du rapport | 200 : Succès <br> 404 : Rapport non trouvé |
| **GET** | Télécharger un SBOM | Récupère un fichier JSON du SBOM | 200 : Succès <br> 404 : SBOM non trouvé |
| **GET** | Informations de vulnérabilité | Récupère un fichier JSON des vulnérabilités | 200 : Succès <br> 404 : Informations non trouvées |

**Base de Données Projet :**

```json
{
  "ID": "string",
  "Nom du projet":string,
  "Description":string

}
```

### **Cette API permet notamment :**  

- Retourner une page de connexion
- Retourner une page de gestion de projet centralisée
  - Ajouter un projet

  - Afficher les détails des projets : SBOM, Rapport Vulnérabilité, etc

  - Lier un utilisateur à un projet en lui attribuant des permissions

  - Gérer les services d'authentification

### Intéraction avec tous les autres micro services

Ce micro-service centrale est en contact avec tous les autres :

- **"import-sbom"** : Nous intéragissons avec lors de la création d'un projet ou nous lui envoyons un SBOM.

- **"vuln"** : Nous intéragissons avec l'API pour que celle-ci nous retourne son fichier de vulnérabilité

- **"consultation-sbom"** : Nous intéragissons avec celle-ci pour avoir toutes les informations relatives au SBOM. Cela nous permet d'éviter d'intéragir trop souvent avec le micro-service **import-sbom**.

- **"rapport"** : API utilisée pour importer les rapports

- **"user"** : API utilisée pour l'enregistrement des utilisateurs, l'authentification, l'ajout de projet etc.

### Arborescence

```
├── Dockerfile
├── README.md
├── app.py
├── diag_com.png
├── diag_user.png
├── openapi.yaml
├── requirements.txt
└── templates
    ├── detail.html
    ├── index.html
    ├── login.html
    └── register.html
```

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


## Voici l'organisation de la base de données.


### **base_de_donnees_sbom.json** 

```
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

### **Cette API permet notamment :**  
- D'ajouter un SBOM dans la base de données   
- De lister tout les SBOMs.  
- De modifier un élément d'un SBOM en renseignant son ID, la clé de la valuer à changer et la nouvelle valeur.
- D'ajouter une dépendance à un SBOM en renqeignant son ID.
- De supprimmer une dependance d'un SBOM par son ID et l'index de la dépendance dans la liste. 
- De supprimmer un SBOM par leur ID. 

---

### **Interaction avec un autre microservice**  

L'API interagit avec le microservice Consultation de SBOM pour permettre aux autres microservices de communiquer avec la base de données SBOMs, mais c'est le seul qui envoie des requêtes directs au microservice Importation de SBOM.

---

## Consultation de SBOM

**Responsable : Simon COLLET**  

# Organisation du microservice consult-sbom

```text
code/
├── consultation_sbom.py    # Application Flask principal
├── Dockerfile          # Dockerfile pour conteneuriser l'application
├── conception.md           # Documentation, explication de l'application
├── requirements.txt    # les dépendance requise pour l'application
└── contrat_dinterface_consultation_SBOM.yaml  # Contrat d'interface de l'application au format openAPI

```

| Méthode | Requête | Description | Réponse |
|---------|---------|-------------|----------|
| **GET** | `/sbom/<id>` | Récupère le fichier SBOM correspondant à `id` | **200** : OK <br> **404** : SBOM introuvable <br> **400** : Erreur import SBOM <br> |
| **GET** | `/version/<id>` | Retourne les dépendances contenus dans le SBOM correspondant à `id` | **200** : OK **404** : SBOM introuvable <br> **400** : Erreur import SBOM <br> **402** SBOM mal formaté |

---

---

### **Cette API permet notamment :**  

- traiter les SBOMs
- de retourner les dependances d'un SBOM
- de retourner un SBOM en fonction de son ID

---

### **Interaction avec un autre microservices**  

L'API interagit avec un autre microservices :  

1. **Récuperer le contenu de la base de donnée SBOM**  

## Rapports

# Organisation du microservice consult-sbom

```text
code/
├── rapports.py    # Application Flask principal
├── Dockerfile          # Dockerfile pour conteneuriser l'application
├── conception.md           # Documentation, explication de l'application
├── requirements.txt    # les dépendance requise pour l'application
├── contrat_dinterface_consultation_SBOM.yaml  # Contrat d'interface de l'application au format openAPI
├── template
    ├──rapport.html     # template des fichiers pdf

```

**Responsable : Simon COLLET**  

| Méthode | Requête | Description | Réponse |
|---------|---------|-------------|----------|
| **GET** | `/pdf/<id>` |crée le rapport au format PDF à partir de l'ID passé en paramètre | **200** : OK <br> **400** : SBOM introuvable <br> **401** : projet introuvable |

---

### **Cette API permet notamment :**  

- permet de générer des rapports au format PDF  

---

### **Interaction avec trois autres microservices**  

L'API interagit avec trois autres microservices :  

1. **Consultation du microservice `vuln` pour récupérer les vulnérabilités associées a l'id**  

2. **Consultation du microservice `consult-sbom` pour récupérer le sbom correspondant a l'id.**  

3. **Consultation du microservice `projet` pour récupérer les données du projet correspondant a l'id.**  

## Gestion des vulnérabilités

**Responsable : Killian CHESNOT**

### Organisation du microservice vulnérabilité

```text
code/
├── Vulnerability.py    # Application Flask principal
├── Vulnerability.json  # Base de données JSON des Vulnérabilités
├── Dockerfile          # Dockerfile pour conteneuriser l'application
├── Exemple.jpg         # Représentation de l'application
├── LICENSE             # License
├── README.md           # Documentation, explication de l'application
├── requirements.txt    # les dépendance requise pour l'application
├── Threat Processing API.postman_collection.json    # Collection d'une batterie de test, pour vérifier le fonctionnement de l'application
└── Vulnerability.yaml  # Contrat d'interface de l'application au format openAPI
```

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

### Voici l'organisation de la base de données

#### **Vulnerability.json**  

```json
{
    "id": 1,
    "VulnerabilityID": "CVE-2023-23397",
    "PkgName": "microsoft-outlook",
    "InstalledVersion": "16.0.15330.20298",
    "FixedVersion": "16.0.16130.20306",
    "Severity": "CRITICAL",
    "Title": "Microsoft Outlook - NTLM Relay Attack (CVE-2023-23397)",
    "Description": "A vulnerability in Microsoft Outlook allows remote attackers to perform NTLM relay attacks by sending specially crafted emails, leading to privilege escalation.",
    "References": "https://nvd.nist.gov/vuln/detail/CVE-2023-23397"
}
```

---

### **Cette API permet notamment :**  

- L'ajout de vulnérabilités, plusieurs à la fois.  
- La suppression de vulnérabilités par leur ID.  
- La liste de toutes les vulnérabilités ou d'une seule grâce à son ID.  
- La modification d'une vulnérabilité avec la possibilité de préciser ou non l'ID.  

---

### **Interaction avec deux autres microservices**  

L'API interagit avec deux autres microservices à l'aide de deux méthodes :  

1. **Récupération des vulnérabilités associées à un SBOM**  
   - Le SBOM peut contenir un ou plusieurs packages (nom, version).  
2. **Consultation du microservice `consult-sbom` pour récupérer les vulnérabilités associées.**  

### Améliorations Possibles

1. Implémenter la branche feature dans le projet.

- Ajouter une amélioration dans le code de la branche feature, en ne récupérant que les informations intéressantes.

2. Commenter le code, pour plus de compréhension, lisibilité.
3. Implémenter une base de données au lieu de fichiers JSON.
4. Implémenter un système de log lors de la consultation, modification, suppression de vulnérabilité dans une base de données JSON. Les retourner lors de la construction du rapport PDF.
5. Implémenter du multi-thread dans le cas où plusieurs communications pourraient être en simultanées sur le microservice.

## Gestion des utilisateurs

**Responsable : Malo DURANTON**  

### Structure du projet

```text
├── README.md            # readme specialiser gestion des user
├── code
│   ├── app.py           # Application Flask principale
│   ├── fonction.py      # Fichier avec les functions  
│   ├── reset_app.py     # Réinitialliser les json si illisible
│   ├── user.json        # Données utillisateur en json
│   └── permission.json  # Données permission en json
├── docker-compose.yaml  # docker compose de test
├── gestuser.Dockerfile  # dockerfile pour build 
├── lunsh_test.sh        # example pour tester l'api user
├── openapi.yaml         # contrat d'api user
├── requirements.txt     # dependances python a installer
├── test_api_bon.hurl
├── test_api_errors.hurl
└── test_api_vide.hurl
```

### Prérequis

- Python 3.x
- Flask
- Docker et Docker Compose
- Dependences listées dans `requirements.txt`
- Internet

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

| HTTP Méthode | Action | Description | Paramètres | Codes |
|--------------|--------|-------------|------------|-------|
| **POST** | `Register` | Inscription d'un nouvel utilisateur | `last_name`, `first_name`, `email`, `password`, `birth_date` | **200** : Utilisateur créé avec succès <br> **400** : Champ manquant <br> **411** : Un utilisateur avec cet e-mail existe déjà <br> **415** : Type de contenu invalide, JSON attendu |
| **POST** | `Login` | Connexion utilisateur | `email`, `password` | **200** : Connexion réussie <br> **400** : Champ manquant <br> **401** : Mot de passe incorrect <br> **404** : Utilisateur non trouvé <br> **415** : Type de contenu invalide, JSON attendu |
| **GET** | `User Info` | Informations utilisateur | `email` (dans le chemin) | **200** : Utilisateur trouvé <br> **409** : Utilisateur non trouvé |
| **PUT** | `Modify User` | Modifier les informations utilisateur | `last_name`, `first_name`, `email`, `password`, `birth_date` | **200** : Informations utilisateur mises à jour <br> **400** : Requête invalide <br> **409** : Utilisateur n'existe pas |
| **DELETE** | `Delete User` | Supprimer un utilisateur | `email` (dans le chemin) | **200** : Utilisateur supprimé avec succès <br> **400** : Requête invalide |
| **POST** | `Add Permissions` | Ajouter des permissions utilisateur | `project_id`, `email`, `write`, `read`, `admin` | **200** : Permissions ajoutées avec succès <br> **400** : Requête invalide <br> **404** : Utilisateur non trouvé <br> **409** : Permissions existent déjà |
| **PUT** | `Modify Permissions` | Modifier les permissions utilisateur | `project_id`, `email`, `write`, `read`, `admin` | **200** : Permissions mises à jour avec succès <br> **400** : Requête invalide <br> **404** : Permissions non trouvées |
| **DELETE** | `Delete Permissions` | Supprimer les permissions utilisateur | `project_id`, `email` (dans la requête) | **200** : Permissions supprimées avec succès <br> **400** : Requête invalide <br> **404** : Utilisateur ou permissions non trouvés |
| **GET** | `Permissions by Project` | Récupérer les permissions utilisateur par projet | `project_id` (dans le chemin) | **200** : Permissions récupérées avec succès <br> **400** : Requête invalide <br> **409** : Aucune permission trouvée pour ce projet |
| **GET** | `Permissions by Email` | Récupérer les permissions utilisateur par e-mail | `email` (dans le chemin) | **200** : Permissions récupérées avec succès <br> **400** : Requête invalide <br> **409** : Aucune permission trouvée pour cet utilisateur |

### Détails du Code

#### Fonctions Utilitaires (`fonction.py`)

##### Opérations JSON

- `read_json(filename)`: Lit et valide le fichier JSON.
- `write_json(filename, data)`: Écrit les données dans le fichier JSON.

##### Fonctions de Gestion des Utilisateurs

- `get_user_by_email(json_data, search_email)`: Retourne l'utilisateur par son email.
- `modify_user_by_email(users, last_name, first_name, email, password, birth_date)`: Modifie les données de l'utilisateur.
- `get_user_by_email(users, email)`: Retourne les données de l'utilisateur (sans mot de passe).
- `delete_user_by_email(users, email)`: Retire l'utilisateur du système.

##### Fonctions de Gestion des Permissions

- `get_permissions_by_project(json_perm, project_id)`: Obtient les permissions du projet.
- `get_permissions_by_email(permissions_list, email)`: Obtient les permissions de l'utilisateur.
- `get_perm_email_idproject(json_perm, email_id, project_id)`: Trouve une permission spécifique.

#### Réinitialisation de l'Application (`reset_app.py`)

- Initialise les données par défaut dans les fichiers JSON.
- Gère la création et la validation des fichiers.
- Fournit des données par défaut pour les utilisateurs et les permissions.

### Considérations de Sécurité

- Les mots de passe sont stockés en texte brut (à améliorer).
- Pas de système de jetons JWT (à implémenter).
- Validation basique des entrées (à renforcer).
- Pas de limitation de débit implémentée.
- Pas de HTTPS par défaut.

### Améliorations Possibles user

1. Implémenter le hachage des mots de passe.
2. Ajouter un système d'authentification JWT.
3. Améliorer la validation des données.
4. Implémenter une base de données au lieu de fichiers JSON.
5. Implémenter un système de journalisation plus robuste.
6. Ajouter une limitation de débit.
7. Activer HTTPS par défaut.
8. Ajouter une désinfection des entrées.
9. Implémenter la gestion des sessions.

### Ce que je peux faire mieux

1. Mieux tester l'API.
2. Standardiser les sorties des fonctions, toujours retourner `[]` pour les résultats vides.
3. Améliorer l'organisation et la lisibilité du code.

---

## Conteneurisation et orchestration
**Responsable :** Tout le monde

La conteneurisation et l'orchestration sont deux étapes qui ont été faites de manières séparées. Ainsi, la responsabilité de la conteneurisation de chaque micro-srvice a été attribué à chaque responsable des micro-service. Elle a été faite par le biais de DockerFiles. Pour plus d'informations sur la conteneurisation des micro-services individuellement, se référer aux README individuels. 

L'orchestration quant à elle a été gérée de manière collective : le projet possède un docker compose qui orchestre tous les containers. Nous pouvons nous intéresser à ce docker compose. Il est composé de plusieurs parties : 

- La déclaration de deux réseau :

```
networks:
  internal_network:
    internal: true
  external_network:
```
Ainsi, nous déclarons deux types de réseaux : un réseau interne qui servira à la communication inter service. Ceux-ci ne seront pas accessibles depuis l'extèrieur. Il est cependant aussi nécessaire de déclarer un autre réseau afin que le conteneur **gestion-des-projets** soit acessible depuis l'extèrieur. En effet, si nous lui attribuons un seul réseau interne, celui-ci ne sera pas accessible par l'extèrieur.

- La déclaration des volumes correponsdant aux différentes bases de données : 

```
volumes:
  gestion_projet:
  vuln:
  sbom:
  user:
```
Ces volumes seront utiles pour stocker de façont permanentes les données des conteneurs ayant une base de donnée. Ainsi même si les conteneurs sont supprimés, ceux-ci auront leurs informations lors de la recréation.

- Enfin, la création à proprement parlé des conteneurs. Ils ont globalement la même configuration entre eux mais certains ont des spécificités. Ils sont déclarés par la variable **service** : 

```
services:
  user:
    build:
      context: "./gestion-des-utilisateurs"
      dockerfile: gestuser.Dockerfile
    container_name: user
    networks:
      - internal_network
    volumes:
      - user:/app

```
Nous construisons le conteneur à partir du DockerFile que les différents microservices ont créés. Nous spécifions aussi leurs noms afin qu'ils puissent communiquer en utilisant leurs noms et non leurs adresses IP qui peuvent être amenés à changer.

Le service est interconnecté via un réseau interne, ce qui empêche des intrusions. Enfin, nous montons un dossier sur un volume afin de créer des données persistantes.

Les conteneurs **consult-sbom**, **vuln**, **rapport** et **gestions** de projets dépendent d'autres conteneurs, nous leurs ajoutons donc un paramètre "depends-on":

```
  rapport:
    build:
      context: "./rapports"
    container_name: rapport
    depends_on:
      - vuln
    networks:
      - internal_network
```
Ces dépendances permettent aux conteneurs de ne démarer que si les conteneurs précédents sont activés. Cela évite de la confusion et un plantage de l'orchestration. Voici le diagramme résumant les différentes dépendances : 

![Diagramme de dependance](dependance.png "Titre de l'image").

Nous pouvons constater que ces dépendances ont été fait de telle sorte que le service terminal n'est qu'une seule dépendance ou deux maximum mais pas 4 dépendances même si celu-ci dépends de beaucoup.

Une fois cela fait, l'utilisateur n'a qu'a exécuter le docker compose pour lancer le micro-service


## Sécurité : Authentification et permissions

L'authentification est gérée dès le début : la page racine de notre API est une page de login. Aucune action n'est possible sans que l'utilisateur soit authentifié. Les exceptions sont pour la page login et la page d'enregistrement logiquement.

Ainsi, lors de l'enregistrement de l'utilisateur, l'API **gestion-des-projets** envoit les informations nécessaires au service **user** pour vérifier si l'utilisateur n'existe pas déjà. Si l'utilisateur est nouveau, alors l'enregistrement se fait bien. 

Pour la connexion, la procédure est la même a l'exception que l'API **user** renvoit les informations de l'utilisateur (mot de passe non compris) et les permissions qui lui sont associés. Si l'utilisateur n'est pas valide, l'API renvoit une erreur et est redirigé vers la page **login**. Nous avons ajouté une redirection indirecte en cas d'erreur. Ansi, les utilisateurs devront utiliser une souris afin d'être redirigé. Cela évitera qu'un utilisateur fasse un grand nombre de tentative dans un très court laps de temps.

Une fois l'utilisateur connecté, il pourra voir la liste des projets lui étant autorisés. Ces autorisations sont attribuées par l'interface **plus** des projets.

Ainsi, lors de la création du projet, le créateur a automatiquement les 3 droits suivants : 

- **read** : Peux lire le projet et télécharger les rapports
- **write** : Peux mettre à jour le projet
- **admin** : Peux supprimer le projet ou ajouter des utilisateurs

Ensuite, il peut ajouter des utilisateurs avec chacun des trois droits au choix. Le tri des permsissions se fait en amont : l'API ne retourne que les JSON avec les bons droits afin qu'aucun manipulation malicieuse ne soit faite. 

Nous n'avons pas eu le temps de mettre en place les Token mais son développement a été initié par la branche **user**.
---

### Liens utiles

- [Documentation](https://foad.univ-exemple.com/docs/SAE401)

---
