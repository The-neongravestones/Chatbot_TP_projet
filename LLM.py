import os
import PyPDF2
import pdfplumber
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


# Utilitaire : Lire le contenu d'un PDF
def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


# Utilitaire : Initialiser la base vectorielle
def initialize_vector_store():
    db = Chroma(
        persist_directory="./TP_db",
        embedding_function=OllamaEmbeddings(model="mxbai-embed-large:latest"),
        collection_name="rag-chroma",
    )
    return db


# Action personnalisée : Extraire les réponses
class ActionRetrieveAnswer(Action):
    def name(self) -> Text:
        return "action_retrieve_answer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> None:
        question = tracker.latest_message.get("text")
        db = initialize_vector_store()

        retriever = db.as_retriever(k=2)
        docs = retriever.retrieve(question)

        # Modèle et prompt
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

        response = after_rag_chain.invoke({"context": docs, "question": question})

        # Envoyer la réponse à l'utilisateur
        dispatcher.utter_message(text=response)
        return []
