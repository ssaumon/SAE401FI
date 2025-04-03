
  

# Rapports

  

**Responsable : Simon COLLET**

## EndPoints :  

| Méthode | Requête | Description | Réponse |

|--|--|--|--|

| **GET** | `/pdf/<id>` | crée le rapport au format PDF à partir de l'ID passé en paramètre | **200** : OK **400** : SBOM introuvable **401** : projet introuvable |

  

  

  

## Methodes du fichier `rapport.py`

  

### recup_sbom(id)

-- la fonction `recup_sbom(id)` fait une requête vers le micro-service `consult-sbom`. Nous allons ensuite récupérer le SBOM correspondant à l'ID passé en paramètre et le stocker dans la variable `sbom` sous forme de dictionnaire.

  

### recup_vul(id)

-- La fonction `recup_vul(id)` fait une requête vers le micro-service `vuln`. Nous allons ensuite stocké la liste de vulnérabilités retourné dans une variable `vul`. L'ID passé en paramètre nous permet de ne réceptionner que les vulnérabilités associé au projet d'identifiant ID.

  

### recup_prj(id)

-- La fonction `recup_prj(id)` permet, grace à une requête `GET` de récupérer les informations du projet d'identifiant ID sous forme de dictionnaire dans la variable .

  

### recup_global(id)

-- La fonction `recup_global(id)` à pour but d'appeler les 3 fonctions ci-dessus. elle permet de simplifier la lisibilité lors de l'appelle de la récupération de toutes les données.

### pdf(id)

  

-- La fonction pdf(id) est lier à l'endpoint `/pdf/<id>`. Nous commençons par appeler la fonction `recup_global(id)` pour mettre a jour nos variables. Puis nous allons essayer de supprimer le fichier "mon_fichier.pdf". Puis nous allons créer une variable pdf de type FPDF. Nous allons envoyer les données que nous voulons voir dans le compte rendu dans un template grace à jinja2 et la fonction rendre_template. puis nous allons, Grace à la méthode `write_html()`, insérer le contenu du template dans le pdf que nous allons ensuite enregistrer sous le nom de "mon_fichier.pdf". Nous allons ensuite retourné le fichier pdf grace à la méthode `send_file()`
