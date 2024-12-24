Bienvenue dans le projet Chatbot TP
==================================

.. image:: im.jpg
   :width: 80%
  

Introduction
============
Le **Chatbot TP** est un assistant virtuel conçu pour aider les étudiants de l'**ENSAM** dans leurs travaux pratiques (TP). Il est capable de fournir des réponses rapides et précises sur des modules tels que :

- Gestion de production  
- Systèmes de production  
- Informatique industrielle  
- Mécanique vibratoire  
- Turbomachinerie  

**Objectif principal**
Améliorer l'efficacité des sessions de TP en mettant à disposition un outil intelligent, personnalisé et facile à utiliser.

**Fonctionnalités principales**
- **Intégration de Rasa** pour la gestion avancée des dialogues.  
- **Modèle LLM Mistral** et **RAG** (Retrieval-Augmented Generation) pour des réponses contextuelles.  
- **Déploiement avec Docker** pour une installation simple et portable.  
- Personnalisation complète grâce aux fichiers **stories**, **domain**, **rules**, et **nlu**.  

Installation
============
**Pré-requis**
Pour utiliser le Chatbot TP, il faut installer les éléments suivants :  
- **Docker** : pour le déploiement.  
- **Python** (version 3.8 ou ultérieure).  
- **Rasa** : framework utilisé pour la gestion des dialogues.  

**Étapes d'installation**
1. **Cloner le dépôt GitHub** :  
   **git clone https://github.com/The-neongravestones/Chatbot_TP_projet.git**
2. **Naviguer dans le dossier du projet** :
  **cd Chatbot_TP_projet**
3. **Construire l'image Docker** :
    **docker-compose up --build.**
4. **Lancer le conteneur Docker** :
    **docker run -p 5005:5005 chatbot_tp **
5. **Accéder au chatbot** : ouvrir navigateur et se rendre à l'adresse suivante :
http://localhost:5005.


Utilisation
============

**Démarrer le chatbot**
Après avoir installé et lancé le conteneur Docker, nous pouvons interagir avec le chatbot via une interface Web ou un terminal.

**Commandes principales**
- **Poser une question** : Entrez une question liée à vos travaux pratiques, et le chatbot vous répondra.  
- **Réinitialiser la conversation** : Taper `reset` pour recommencer la session.  

---

Architecture
============

Le projet est structuré autour des éléments suivants :

- **Rasa** : pour gérer les intentions, les réponses et le flux des conversations.  
- **Domain.yml** : contient les actions, intentions et réponses prédéfinies.  
- **NLU.yml** : configure les données d'entraînement des intentions.  
- **Stories.yml** : décrit les scénarios de conversation.  
- **Actions** : permet de définir des réponses personnalisées ou de récupérer des données dynamiques.  

---

Personnalisation
================

Nous pouvons adapter le Chatbot TP à nos besoins spécifiques en modifiant les fichiers suivants :  
- **domain.yml** : ajouter ou supprimer des intentions ou actions.  
- **nlu.yml** : entraîner le chatbot avec de nouvelles phrases d'exemple.  
- **stories.yml** : créer des scénarios pour guider le chatbot dans des conversations spécifiques.  

**Entraîner le chatbot**
Après avoir apporté des modifications, exécuter cette commande pour réentraîner le modèle :  

 **rasa train **

