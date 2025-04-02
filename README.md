# Présentation générale du microservice

Ce micro-service à pour but de rassembler toutes les fonctionnalités des autres micro-services afin de les rendre exploitables de manière ergonomique. Il aura donc deux rôles principaux : 
 
 -**Communiquer** avec les autres micro-services afin de recevoir ou d'envoyer des données
 
 -**Afficher** les données reçus par ces dernière pour que l'utilisateur aie une expèrience agréable
 
 
# Fichiers composant le micro-service

Ce micro service est donc constitué des fichiers : 

- **README** : contient les informations du micro service, un diagramme d'utilisateur ainsi qu'un diagramme de fonctionnement
- **DockerFile** : Ce fichier sert à construire une image du conteneur hébergeant notre site
- **Contrat d'interface** : Ce fichier affichera toutes les fonctions étant acessibles grâce à des requêtes HTTP
- **Code python** : Ce fichier constitue la majeur partie du microservice. Il constitue la partie fonctionnelle de l'application
- **Template** : Utilisées par le code python afin de créer des sites dynamiques

# Diagramme de fonctionnement

Voici maintenant le diagramme de fonctionnement de notre micro-service. Celui-ci illustrera le fonctionnement de notre micro service ainsi que ses nombreux liens avec les autres micro-services :

![Diagramme de communication](diag_com "Titre de l'image").

Celui-ci est très dépendant des autres micro services


# DockerFile

Le fichier DockerFile sert dans un premier temps à construire l'image Docker de notre micro-service. Dans un second temps, celui-ci sera utilisé dans le DockerCompose afin de créer et démarrer automatiquement tous les services. Voici donc la composition de notre Docker File : 
```
FROM python:3.11
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]
```

L'image que nous utilisons est donc une image python 3.11. Nous creeons ensuite un dossier **app** et nous nous plaçons dedans afin de pouvoir importer des fichiers sans risque de perturber le fonctionnement de l'image en elle même. Nous copions le fichier **requierement.txt**. Celui-ci contiens tous les modules indispensables à installer pour le bon fonctionnement de notre microservice. Les voici : 

- Flask version 3.1
- requests version 2.32

Nous installons ensuite automatiquement les modules. Cela a pour avantage d'avoir une uniformité d'image et que côté utilisateur, cela soit totalement transparent.

Une fois l'installation achevée, nous copions le dossier contenant tous les fichiers (appli python et template principalement). Nous modifions ensuite les variables d'environnement afin que le conteneur sache quel fichier sera utilisé comme application FLASK et lui ordonner d'écouter sur toutes les adresses IP. Nous ouvrons ensuite le port 5000 afin que l'appli soit joignable de l'extèrieur. Cette dernière action n'est pas obligatoire mais vise à améliorer la transparence du code.

Lors de la création du conteneur, nous exécutons un flask run pour démarrer le service/

# Contrat d'interface
Le contrat d'interface se trouve dans le fichier **openapi.yaml**. Celui-ci contient les différentes informations sur notre micro-service. 

Ce contrat peut être découpé en trois sous catégories : 

## Gestion des utilisateurs

Cette partie est identifiée par le tag **"user"**. Elle est composée de 5 méthodes distinctes identifiées par les routes suivantes : 

- "/" : Méthode GET : Retourne la page d'authentification à l'API

- "/login/login" : Méthode POST : Envoie les informations de connexion afin que l'utilisateur puisse répondre de son identité et ainsi utiliser l'API selon les droits lui étant attribués.






- "/register" : Méthode GET :  Retourne la page HTML d'enregistrement d'un nouvel utilisateur
 



- "/register/send" : Méthode POST : Envoie les informations du nouvel utilisateur à la base de donnée utilisateur afin que celui-ci vérifie celles-ci et l'inscrive



- "/logout" : Méthode GET : Permet la déconnexion d'un utilisateur 

  

## Gestion des projets

Cette partie est identifiée par le tag **"projets"**. La plupart de ces méthodes sont directement en contact avec d'autres micro-sercices telles que les microservices **Utilisateurs** ou **Importation-SBOM**.

- "/homepage" : Méthode GET : Retourne la page d'acceuil possédant la liste des projets que l'utilisateur a le droit de consulter mais aussi une possibilité d'ajouter des projets.

- "/projet/{id}" : Méthode GET : Retourne la page HTML possédant les détails d'un projet si l'utilisateur connecté à les droits. Cette page contiendra le nom, l'ID, la description, la possibilité de modifier si l'utilisateur à les droits ainsi que d'ajouter des utilisateurs ou de supprimer le projet.

- "/projet/json/{id}" : Méthode GET : Retourne le fichier json associé à un projet

- "/projet/add" : Méthode POST : Permet d'ajouter un projet. L'utilisateur sera automatiquement admin dessus. Il devra aussi lui-même fournir le SBOM associé au projet.

- "/projet/update" : Méthode PUT : Permet de mettre à jour un projet à partir de son ID et des nouvelles informations

- "/projet/delete" : Méthode DELETE : Supprimer un projet grâce à son ID.

- "/projet/projet/adduser" : Méthode POST : Ajoute un utilisateur au projet. Possibilité de lui attribuer des droits spécifiques : lecture, ecriture ou admin.


## Accès aux documents
Cette partie est identifiée par le tag **"doc"** dans le contrat d'interface. Celle-ci retourne dans chaque cas un fichier exploitable et téléchargeable.

- "/rapport/{id}" : Méthode GET : Retourne un fichier PDF contenant le rapport général du projet

- "/sbom/{id}" : Méthode GET : Retourne un fichier JSON contenant le SBOM*

- "/vulne/{id}" : Méthode GET : Retourne un fichier JSON contenant le rapport de vulnérabilité du projet


Ce contrat d'interface est par ailleurs consultable dans la branche. Il précise par ailleurs les différents codes d'erreurs des API. 


# Code python

## Liste des modules

## Liste des méthodes du micro-service : 

| Méthode                  | Fonctionnalité | Paramètres d'entrée | Sortie | Codes de sortie | Dépendances API |
|--------------------------|---------------|----------------------|--------|----------------|----------------------------------|
| `open_project_file` | Ouvre le fichier JSON des projets et le charge en mémoire. | Aucun | JSON des projets ou message d'erreur | `200`, `415` | Aucune |
| `save_project_file(dico)` | Sauvegarde les projets dans le fichier JSON. | `dico` (dictionnaire des projets) | Message de succès ou d'erreur | `200`, `404`, `415` | Aucune |
| `bienvenue()` | Affiche la page d'accueil avec les projets accessibles par l'utilisateur. | Aucun | Page HTML `index.html` ou redirection | `200`, `403` | Aucune |
| `login()` | Affiche la page de connexion. | Aucun | Page HTML `login.html` | `200` | Aucune |
| `checklogin()` | Vérifie les identifiants et récupère les permissions utilisateur. | `mail`, `password` via POST | Redirection vers `/homepage` ou `/` | `302`, `403` | `http://user:5000/login`, `http://user:5000/user/{mail}`, `http://user:5000/permissions-by-email/{mail}` |
| `get_project(id)` | Affiche les détails d'un projet si l'utilisateur a les droits de lecture. | `id` (ID du projet) | Page HTML `detail.html` ou message d'erreur | `200`, `404` | Aucune |
| `get_json(id)` | Récupère les informations d’un projet sous format JSON. | `id` (ID du projet) | Données JSON du projet ou message d'erreur | `200`, `404` | Aucune |
| `add_project()` | Ajoute un nouveau projet avec un fichier JSON et une description. | `name`, `json` (fichier), `description` | Redirection vers `/homepage` ou message d'erreur | `302`, `403`, `415`, `511`, `512`, `513` | `http://user:5000/add-permissions`, `http://import-sbom:5000/sbom` |
| `update_project()` | Met à jour un projet si l'utilisateur a les droits d'écriture. | `id`, `name`, `description` via POST | Redirection vers `/homepage` ou message d'erreur | `302`, `403`, `404`, `513` | Aucune |
| `remove_project(id)` | Supprime un projet si l'utilisateur a les droits d'administration. | `id` (ID du projet) | Redirection vers `/homepage` ou message d'erreur | `302`, `403`, `513` | `http://user:5000/permissions-by-project/{id}`, `http://user:5000/delete-permissions?project_id={id}&email={email}` |
| `ajouter_user()` | Ajoute un utilisateur à un projet avec des permissions spécifiques. | `email`, `id` (ID projet), `permissions` | Redirection vers la page du projet ou erreur | `302`, `511` | `http://user:5000/add-permissions` |
| `get_rapport(id)` | Télécharge un rapport PDF d'un projet. | `id` (ID du projet) | Fichier PDF ou message d'erreur | `200`, `404` | `http://rapport:5000/pdf/{id}` |
| `get_sbom(id)` | Télécharge le fichier SBOM JSON d'un projet. | `id` (ID du projet) | Fichier JSON ou message d'erreur | `200`, `404` | `http://consult-sbom:5000/sbom/{id}` |
| `get_vulne(id)` | Télécharge les vulnérabilités d'un projet sous format JSON. | `id` (ID du projet) | Fichier JSON ou message d'erreur | `200`, `404` | `http://vuln:5000/Vulnerability/sbom/{id}` |
| `enre()` | Affiche la page d'inscription. | Aucun | Page HTML `register.html` | `200` | Aucune |
| `send_user()` | Enregistre un nouvel utilisateur. | Données du formulaire d'inscription | Redirection vers `/` ou message d'erreur | `302`, `513` | `http://user:5000/register` |
| `logout()` | Déconnecte l'utilisateur en vidant ses données de session. | Aucun | Redirection vers `/` | `302` | Aucune |

# Template


# Améliorations possibles
 
Liste visible des utilisateurs

MAJ SBOM

Possibilité de modifier les utilisateurs

Interface utilisateur

# This is a Heading h1
## This is a Heading h2
###### This is a Heading h6

## Emphasis

*This text will be italic*  
_This will also be italic_

**This text will be bold**  
__This will also be bold__

_You **can** combine them_

## Lists

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b
    * Item 3a
    * Item 3b

### Ordered

1. Item 1
2. Item 2
3. Item 3
    1. Item 3a
    2. Item 3b

## Images

![This is an alt text.](/image/sample.webp "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.
