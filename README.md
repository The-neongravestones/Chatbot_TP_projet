# Chatbot TP - Rasa & Docker

## Description du Projet

Ce projet consiste en la création d'un **chatbot** conçu pour assister les étudiants lors des **travaux pratiques (TP)** dans divers domaines d'ingénierie à l'**ENSAM Meknès**. Le chatbot utilise des outils avancés tels que des **modèles de langage (LLM)** et une architecture hybride basée sur **RAG (Retrieval-Augmented Generation)** pour offrir des réponses pertinentes et précises.

Une base de données simplifiée, sous forme de **PDF** d’un fascicule de TP en gestion de production, est utilisée pour tester le chatbot et évaluer ses performances dans le cadre des sessions pratiques.

---

## Structure des Fichiers

Voici la structure du projet et une brève description de chaque fichier/dossier :

![image](https://github.com/user-attachments/assets/6f838f15-5786-4d8e-ad6c-95b6e47f389e)


---

## Modules Clés

### 1. NLU et Gestion des Dialogues (Rasa)

- Permet de comprendre les **intentions** des utilisateurs à l'aide de l'entraînement NLU.
- Gère les **flux de conversation** et les interactions avec les utilisateurs via les fichiers `nlu.yml`, `stories.yml` et `rules.yml`.
- Utilisation du modèle pré-entraîné dans le fichier `model.tar.gz` pour effectuer des prédictions et générer des dialogues.

### 2. LLM (Fichier `LLM.py`)

- Exploitation du modèle **Mistral** pour générer des réponses plus riches et **précises**.
- Utilisation de la **langue naturelle** pour traiter les requêtes complexes des utilisateurs et retourner des réponses adaptées au contexte du TP.

### 3. RAG (Fichier `ingest.py`)

- **Retrieval-Augmented Generation** (RAG) utilise une approche hybride pour intégrer les informations du fascicule de TP dans les réponses du chatbot.
- L'**indexation des données PDF** permet une recherche rapide et efficace des informations dans le fascicule TP (`tp_gp.pdf`).

### 4. Base de Données (PDF)

- Le fichier `tp_gp.pdf` sert de base de données pour simuler des bases de données plus complexes. Il contient des informations essentielles utilisées pour générer des réponses sur des questions techniques liées aux TP.

### 5. Déploiement Dockerisé

- Le projet est **entièrement conteneurisé** avec **Docker** pour garantir une exécution fiable et reproductible.
- **Docker Compose** est utilisé pour orchestrer les services (chatbot, base de données, etc.).

---

## Installation

### Prérequis

- **Docker** et **Docker Compose** installés sur votre machine.

### Étapes d'Installation

1. **Cloner le projet**

   Clonez le dépôt GitHub pour obtenir tous les fichiers du projet :

   ```bash
   git clone https://github.com/The-neongravestones/Chatbot_TP_project.git
   cd Chatbot_TP_project
2. **Configurer les Dépendances**

Les dépendances Python sont gérées automatiquement avec Docker. Le fichier requirements.txt est inclus et sera utilisé pour installer toutes les bibliothèques nécessaires à l'exécution du chatbot.

3. **Démarrer le Chatbot avec Docker Compose**

Lancez les services avec la commande suivante :


Cela construira les images Docker et lancera les services nécessaires à l'exécution du chatbot.

Accéder au Chatbot

Une fois les services démarrés, vous pouvez accéder au chatbot via votre navigateur à l'adresse suivante :

http://localhost:5005

Le chatbot sera disponible et prêt à répondre aux questions des TP.
