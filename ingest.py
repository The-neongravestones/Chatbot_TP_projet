import os
import pdfplumber
from LLM import read_pdf
from langchain_chroma import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings.ollama import OllamaEmbeddings


def load_documents_from_directory(directory_path):
    files = [
        os.path.join(directory_path, file)
        for file in os.listdir(directory_path)
        if file.endswith(".pdf")
    ]
    return [Document(page_content=read_pdf(file)) for file in files]


def ingest_into_vector_store(documents):
    text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    doc_splits = text_splitter.split_documents(documents)

    db = Chroma(
        persist_directory="./TP_db",
        embedding_function=OllamaEmbeddings(model="mxbai-embed-large:latest"),
        collection_name="rag-chroma",
    )
    db.add_documents(doc_splits)
    #db.persist()


def main():
    directory = "./documents"
    documents = load_documents_from_directory(directory)
    ingest_into_vector_store(documents)


if __name__ == "__main__":
    main()
