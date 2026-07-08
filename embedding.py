from langchain_ollama import OllamaEmbeddings

from config import EMBEDDING_MODEL

def create_embeddings():
    embeddings = OllamaEmbeddings(
            model = EMBEDDING_MODEL
            )
    return embeddings

    

