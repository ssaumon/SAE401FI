# Consultation de SBOM

**Responsable : Simon COLLET**

## EndPoints :  

| Méthode | Requête | Description | Réponse |
|---------|---------|-------------|----------|
| **GET** | `/sbom/<id>` | Récupère le fichier SBOM correspondant à `id` | **200** : OK <br> **404** : SBOM introuvable <br> **400** : Erreur import SBOM <br> |
| **GET** | `/version/<id>` | Retourne les dépendances contenus dans le SBOM correspondant à `id` | **200** : OK **404** : SBOM introuvable <br> **400** : Erreur import SBOM <br> **402** SBOM mal formaté |

## Méthodes du fichier `consultation_sbom.py`

### recup_sbom() :

La méthode `récup_sbom()` à pour but de mettre à jour la variable `sboms` qui doit contenir tous les sboms existants dans le micro-service importation de SBOM. Pour ce faire, nous allons faire une requête `GET` à destination de ce micro-service. Si la réponse est valide (code 200), nous remplaçons le contenu de `sboms` par celui de cette requête. Cette methode est implémentée au debut des deux autres fonctions de ce micro-service. 

### version(id) : 

La méthode `version(id)` est appelé lors d'une requête GET sur l'endpoint `/version/<id>`. Celle-ci à pour but de retourné toutes les dependences d'un sbom ainsi que leurs versions. Pour ce faire, nous commencons par mettre a jour notre variable `sboms`. Puis nous allons créer une liste de dictionnaire dans laquelle nous allons mettre les dictionnaires correspondants aux dépendances et leurs versions. Nous allons ensuite retourner cette liste.

### sbom(id) :
La méthode `sbom(id)` est appelé lors d'une requête GET sur l'endpoint `/sbom/<id>`. Celle-ci à pour but de retourné le sbom correspondant à l'id passé en paramètre. Nous commençons par mettre à jour notre variable `sboms`. Puis nous regardons si il exite la clé `id` dans la liste des clés de la variable `sboms`. Si cette clé existe, nous retournons le SBOM correspondant au format JSON. 