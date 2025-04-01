# User Management API

L'API User Management permet la gestion des utilisateurs, y compris l'enregistrement, la connexion, la déconnexion, la suppression et la gestion des permissions.

## Serveurs

- **Serveur principal**: [http://api.rt.lan/](http://api.rt.lan/)
- **Serveur Docker**: [http://user:5000](http://user:5000)

## Fonctionnalités

### Gestion des utilisateurs

- **Enregistrement d'un nouvel utilisateur**
  - **Endpoint**: `POST /register`
  - **Description**: Enregistre un nouvel utilisateur.
  - **Requête**:

    ```json
    {
      "last_name": "Doe",
      "first_name": "John",
      "email": "john.doe@example.com",
      "password": "securepassword123",
      "birth_date": "01-01-1990"
    }
    ```

  - **Réponses**:
    - `200 OK`: Utilisateur créé avec succès.
    - `400 Bad Request`: Champ manquant.
    - `409 Conflict`: Un utilisateur avec cette adresse e-mail existe déjà.
    - `415 Unsupported Media Type`: Type de contenu invalide, JSON attendu.

- **Connexion utilisateur**
  - **Endpoint**: `POST /login`
  - **Description**: Authentifie un utilisateur.
  - **Requête**:

    ```json
    {
      "email": "john.doe@example.com",
      "password": "securepassword123"
    }
    ```

  - **Réponses**:
    - `200 OK`: Connexion réussie.
    - `400 Bad Request`: Champ manquant.
    - `401 Unauthorized`: Mot de passe incorrect.
    - `404 Not Found`: Utilisateur non trouvé.
    - `415 Unsupported Media Type`: Type de contenu invalide, JSON attendu.

- **Informations utilisateur**
  - **Endpoint**: `GET /user/{email}`
  - **Description**: Récupère les informations d'un utilisateur.
  - **Paramètres**:
    - `email` (chemin): Adresse e-mail de l'utilisateur.
  - **Réponses**:
    - `200 OK`: Utilisateur trouvé.
    - `409 Conflict`: Utilisateur non trouvé.

- **Modification des informations utilisateur**
  - **Endpoint**: `PUT /modify`
  - **Description**: Met à jour les informations d'un utilisateur.
  - **Requête**:

    ```json
    {
      "last_name": "Doe",
      "first_name": "John",
      "email": "john.doe@example.com",
      "password": "securepassword123",
      "birth_date": "01-01-1990"
    }
    ```

  - **Réponses**:
    - `200 OK`: Informations utilisateur mises à jour.
    - `400 Bad Request`: Requête invalide.
    - `409 Conflict`: Utilisateur n'existe pas.

- **Suppression d'un utilisateur**
  - **Endpoint**: `DELETE /delete-user/{email}`
  - **Description**: Supprime un utilisateur.
  - **Paramètres**:
    - `email` (chemin): Adresse e-mail de l'utilisateur à supprimer.
  - **Réponses**:
    - `200 OK`: Utilisateur supprimé avec succès.
    - `400 Bad Request`: Requête invalide.

### Gestion des permissions

- **Ajout de permissions utilisateur**
  - **Endpoint**: `POST /add-permissions`
  - **Description**: Ajoute des permissions pour un utilisateur.
  - **Requête**:

    ```json
    {
      "project_id": "1",
      "email": "john.doe@example.com",
      "write": true,
      "read": true,
      "admin": false
    }
    ```

  - **Réponses**:
    - `200 OK`: Permissions ajoutées avec succès.
    - `400 Bad Request`: Requête invalide.
    - `404 Not Found`: Utilisateur non trouvé.
    - `409 Conflict`: Permissions existent déjà.

- **Modification des permissions utilisateur**
  - **Endpoint**: `PUT /modify-permissions`
  - **Description**: Met à jour les permissions d'un utilisateur.
  - **Requête**:

    ```json
    {
      "project_id": "1",
      "email": "john.doe@example.com",
      "write": true,
      "read": true,
      "admin": false
    }
    ```

  - **Réponses**:
    - `200 OK`: Permissions mises à jour avec succès.
    - `400 Bad Request`: Requête invalide.
    - `404 Not Found`: Permissions non trouvées.

- **Suppression des permissions utilisateur**
  - **Endpoint**: `DELETE /delete-permissions`
  - **Description**: Supprime les permissions d'un utilisateur pour un projet.
  - **Paramètres**:
    - `project_id` (query): ID du projet.
    - `email` (query): Adresse e-mail de l'utilisateur.
  - **Réponses**:
    - `200 OK`: Permissions supprimées avec succès.
    - `400 Bad Request`: Requête invalide.
    - `404 Not Found`: Utilisateur ou permissions non trouvés.

- **Récupération des permissions par projet**
  - **Endpoint**: `GET /permissions-by-project/{project_id}`
  - **Description**: Récupère les permissions des utilisateurs pour un projet.
  - **Paramètres**:
    - `project_id` (chemin): ID du projet.
  - **Réponses**:
    - `200 OK`: Permissions récupérées avec succès.
    - `400 Bad Request`: Requête invalide.
    - `409 Conflict`: Aucune permission trouvée pour ce projet.

- **Récupération des permissions par e-mail**
  - **Endpoint**: `GET /permissions-by-email/{email}`
  - **Description**: Récupère les permissions d'un utilisateur.
  - **Paramètres**:
    - `email` (chemin): Adresse e-mail de l'utilisateur.
  - **Réponses**:
    - `200 OK`: Permissions récupérées avec succès.
    - `400 Bad Request`: Requête invalide.
    - `409 Conflict`: Aucune permission trouvée pour cet utilisateur.
