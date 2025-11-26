from langchain.embeddings import HuggingFaceEmbeddings   # old versions 
from langchain.vectorstores import Chroma


from src.ui.config import Config

PERSIST_DIR = "./tmp/chroma_db"
COLLECTION_NAME = "email_templates"

def retrieve_similar_email(user_query: str):
    config = Config()

    # Load embedding model from config.ini
    embedding_model_name = config.get_embedding_model()

    embeddings = HuggingFaceEmbeddings(
        model_name=embedding_model_name
    )

    # Load existing vector DB
    vectordb = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR
    )

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 1}
    )

    results = retriever.invoke(user_query)
    return [doc.page_content for doc in results]
