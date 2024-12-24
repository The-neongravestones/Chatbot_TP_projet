FROM rasa/rasa:3.0.0-full

# Installer des dépendances supplémentaires
RUN apt-get update && apt-get install -y poppler-utils && \
    pip install pdfplumber langchain langchain_community

# Copier les actions dans le conteneur
COPY actions /app/actions
WORKDIR /app

# Installer les actions
RUN pip install -r /app/requirements.txt

# Démarrage des actions Rasa
CMD ["rasa", "run", "actions"]
