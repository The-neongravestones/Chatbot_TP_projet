import os
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_models import ChatOllama
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, Text
from ingest import load_documents_from_directory  # Importer la fonction du fichier ingest.py


# Action personnalisée : Extraire les réponses à partir des documents indexés
class ActionRetrieveAnswer(Action):
    def name(self) -> Text:
        return "action_retrieve_answer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> None:
        question = tracker.latest_message.get("text")
        directory = "./documents"  # Dossier où sont stockés les PDF
        documents = load_documents_from_directory(directory)  # Charger les documents depuis le dossier

        # Initialisation du store vectoriel
        db = Chroma(
            persist_directory="./TP_db",
            embedding_function=OllamaEmbeddings(model="mxbai-embed-large:latest"),
            collection_name="rag-chroma",
        )
        
        # Créer un récupérateur pour retrouver les documents les plus pertinents
        retriever = db.as_retriever(k=2)  # Limiter le nombre de documents récupérés
        docs = retriever.retrieve(question)

        # Créer le prompt pour l'IA
        model = ChatOllama(model="mistral")
        after_rag_prompt = ChatPromptTemplate.from_template(
            """Answer the question based only on the following context:
            {context}
            Question: {question}
            If there is no answer, reply with: "I'm sorry, I cannot answer based on the provided context."
            """
        )

        after_rag_chain = (
            {"context": docs, "question": RunnablePassthrough()}
            | after_rag_prompt
            | model
        )

        # Obtenir la réponse générée par le modèle
        response = after_rag_chain.invoke({"context": docs, "question": question})

        # Envoyer la réponse à l'utilisateur
        dispatcher.utter_message(text=response)
        return []
