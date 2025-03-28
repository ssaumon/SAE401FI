# Utiliser une image Python officielle comme image de base
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /tmp

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
# Copier le reste du code de l'application dans le conteneur
COPY ./code/ .

# Exposer le port sur lequel l'application écoute
EXPOSE 5000

# Définir la commande par défaut pour exécuter l'application
CMD ["python", "app.py"]
