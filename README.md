# Vulnerability MicroService

## Description
Le **Vulnerability MicroService** est une application web construite avec la librairie **Flask**, permettant de gérer et de manipuler des informations sur des vulnérabilités logicielles. Le service est découpé en plusieurs méthodes, chacune exposée via des routes dédiées sur le serveur. Ce microservice vous permet d'effectuer différentes opérations comme la création, la modification, la suppression et la consultation des vulnérabilités, le tout à travers une interface HTTP simple. Toutes les données sont stockées dans un fichier JSON nommé **Vulnerability.json**.

L'application porte le nom de **Vulnerability.py** et dispose d'un script de test en Python intitulé **test.py**. Un contrat d'interface est également fourni sous le nom de **Vulnerability.yaml**.

## Routes et Méthodes

L'application expose plusieurs routes, chacune correspondant à une fonctionnalité spécifique. Voici un aperçu des routes disponibles :

### 1. `/`
**Méthode : GET**

- **Description** : Affiche la page de "test" pour vérifier le bon fonctionnement du microservice. Ce chemin retourne simplement le message "Microservice Vulnerability".

### 2. `/Vulnerability`
**Méthodes : GET, POST, PUT**

- **GET** : Liste toutes les vulnérabilités stockées dans la base de données.
- **POST** : Permet d'ajouter une ou plusieurs nouvelles vulnérabilités à la base de données. L'API peut envoyer plusieurs vulnérabilités simultanément en format JSON.
- **PUT** : Permet de modifier une vulnérabilité sans spécifier d'ID dans l'URL. Cette méthode récupère l'ID depuis le corps JSON de la vulnérabilité pour effectuer la modification en toute sécurité.

### 3. `/Vulnerability/<int:id_Vuln>`
**Méthodes : GET, DELETE, PUT**

- **GET** : Permet de récupérer une vulnérabilité spécifique en utilisant son ID.
- **DELETE** : Permet de supprimer une vulnérabilité en spécifiant son ID.
- **PUT** : Permet de modifier une vulnérabilité en utilisant son ID dans l'URL.

### 4. `/Vulnerability/sbom`
**Méthode : POST**

- **Description** : Permet de rechercher dans la base de données la présence de vulnérabilités pour une version spécifique d'un package, envoyée depuis l'API du SBOM (Software Bill of Materials). Si une version compromise est trouvée, la méthode retourne les informations relatives à cette vulnérabilité, telles que la version corrigée, les liens vers la documentation, etc.

## Fichiers Importants

- **Vulnerability.py** : Script principal de l'application qui définit les routes et gère les requêtes.
- **test.py** : Script de test en Python pour vérifier le bon fonctionnement du service et tester les différentes routes.
- **Vulnerability.yaml** : Contrat d'interface (Swagger/OpenAPI) définissant les routes, les paramètres et les réponses possibles.

## Exemple d'Utilisation

1. **Ajouter une vulnérabilité** (méthode POST) :
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{
        "VulnerabilityID": "CVE-2021-3156",
        "PkgName": "sudo",
        "InstalledVersion": "1.8.31",
        "FixedVersion": "1.9.5p2",
        "Severity": "CRITICAL",
        "Title": "Sudo - Heap-based Buffer Overflow in sudoedit (CVE-2021-3156)",
        "Description": "A heap-based buffer overflow in sudoedit in sudo before 1.9.5p2 allows privilege escalation to root via a crafted command line.",
        "References": ["https://nvd.nist.gov/vuln/detail/CVE-2021-3156"]
    }' http://127.0.0.1:5007/Vulnerability
    ```

2. **Obtenir la liste des vulnérabilités** (méthode GET) :
    ```bash
    curl http://127.0.0.1:5007/Vulnerability
    ```

3. **Modifier une vulnérabilité** (méthode PUT) :
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{
        "VulnerabilityID": "CVE-2021-3156",
        "PkgName": "sudo",
        "InstalledVersion": "1.8.31",
        "FixedVersion": "1.9.5p2",
        "Severity": "CRITICAL",
        "Title": "Sudo - Heap-based Buffer Overflow in sudoedit (CVE-2021-3156)",
        "Description": "A heap-based buffer overflow in sudoedit in sudo before 1.9.5p2 allows privilege escalation to root via a crafted command line.",
        "References": ["https://nvd.nist.gov/vuln/detail/CVE-2021-3156"]
    }' http://127.0.0.1:5007/Vulnerability
    ```

4. **Supprimer une vulnérabilité** (méthode DELETE) :
    ```bash
    curl -X DELETE http://127.0.0.1:5007/Vulnerability/1
    ```

## Installation

1. Clonez ce repository :
    ```bash
    git clone https://github.com/yourusername/vulnerability-microservice.git
    cd vulnerability-microservice
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Lancez l'application Flask :
    ```bash
    python Vulnerability.py
    ```

4. L'application sera disponible à l'adresse `http://127.0.0.1:5007`.

## Technologies Utilisées

- **Flask** : Framework web pour Python.
- **JSON** : Format de stockage des vulnérabilités.
- **cURL** : Utilisé dans les exemples pour tester les routes API.

## Contributeurs

- Votre nom ou équipe

## License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
