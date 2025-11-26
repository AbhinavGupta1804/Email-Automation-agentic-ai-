import json
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

from src.ui.config import Config

PERSIST_DIR = "./tmp/chroma_db"
COLLECTION_NAME = "email_templates"

def build_vector_store():

    config = Config()

    with open("src/data/email.json", "r", encoding="utf-8") as f:
        emails = json.load(f)

    texts = [item["body"] for item in emails]

    # Load embedding model from config.ini
    embedding_model_name = config.get_embedding_model()

    embeddings = HuggingFaceEmbeddings(
        model_name=embedding_model_name
    )

    # Create & persist vector store
    vectordb = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIR
    )

    vectordb.persist()
    print("Vector store created & saved successfully!")

if __name__ == "__main__":
    build_vector_store()

