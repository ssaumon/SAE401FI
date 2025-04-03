# Importation SBOM MicroService

# SAE401 - DevCloud - Document de Conception MicroService Importation SBOM

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

---
## Expliation des méthodes

###### X.X.X.X = Ip où le microservice est déployé / YYYY = port où le microservice est déployé

### Get_SBOMs (GET)

Cette méthode permet de recevoir l'ensemble du contenu de la base de données SBOM, contenant l'ensemble des SBOMs enregistrés jusqu'à maintenant.

Pour faire appelle à cette méthode il faut dans une requête web, curl ou Postman mettre le chemin ``http://X.X.X.X:YYYY/sbom``.

Elle renvoie uniquement une réponse 200 avec la base de données en json.

### Ajout_SBOM (POST)

Cette méthode permet d'ajouter un SBOM en renseignant tout le json du SBOM dans son entiereté.

Pour faire appelle à cette méthode il faut dans une requête curl ou Postman mettre le chemin ``http://X.X.X.X:YYYY/sbom`` avec le SBOM en json.

Elle renvoie uniquement une réponse 200 en renvoyant SBOM Added To The Data Base.

### Ajout_Dependance_SBOM (POST)

Cette méthode permet d'ajouter une dépendance à un SBOM en particulier que l'on doit préciser en plus de la dépendance en json/dictionnaire.

Pour faire appelle à cette méthode il faut dans une requête curl ou Postman mettre le chemin ``http://X.X.X.X:YYYY/sbom/dependance/<id>`` avec l'id du SBOM voulue + en json/dictionnaire la dépendance à ajouter.

Elle renvoie une réponse 200 en renvoyant Dependance Added To The SBOM et une réponse 404 en renvoyant SBOM Not Found.

### Update_SBOM (PATCH)

Cette méthode permet de modifier une valeur d'un SBOM en particulier tant que la clé dont on veut changer la valeur existe dans le SBOM.

Pour faire appelle à cette méthode il faut dans une requête web, curl ou Postman mettre le chemin ``http://X.X.X.X:YYYY/sbom/<id>/<cle>/<new_val>`` avec, &lt;id&gt; l'id du SBOM à modifier, &lt;cle&gt; la clé correspondant à la valeur a changer et &lt;new_val&gt; la nouvelle valeur à mettre en place.

Elle renvoie une réponse 200 en renvoyant Value Changed, une réponse 404 en renvoyant Key Of SBOM Not Found et une autre réponse 404 en renvoyant SBOM Not Found.

### Suppression_dependance_SBOM (DELETE)

Cette méthode permet de supprimer une dépendance d'un SBOM

Pour faire appelle à cette méthode il faut dans une requête web, curl ou Postman mettre le chemin ``http://X.X.X.X:YYYY/sbom/dependance/delete/<id>/<id_dependance>`` avec, &lt;id&gt; l'id du SBOM à modifier, &lt;id_dependance&gt; l'id correspondant à l'index de l'emplace de la dépendance à supprimer.

Elle renvoie une réponse 200 en renvoyant Dependance Deleted, une réponse 404 en renvoyant Dependance Not Found et une réponse 404 en renvoyant SBOM Not Found.

### Suppression_SBOM (DELETE)

Cette méthode permet de supprimer un sbom de la base de données.

Pour faire appelle à cette méthode il faut dans une requête web, curl ou Postman mettre le chemin ``http://X.X.X.X:YYYY/sbom/delete/<id>`` avec &lt;id&gt; l'id du SBOM à supprimer.

Elle renvoie une réponse 200 en renvoyant SBOM Deleted et une réponse 404 en renvoyant SBOM Not Found.