# Utiliser l'image de base de Rasa pour les actions
FROM rasa/rasa-sdk:3.4.0


# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY ./actions /app/actions

# Installer les dépendances Python
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande d'exécution pour le serveur d'actions
CMD ["rasa", "run", "actions"]
