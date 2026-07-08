from langchain_chroma import Chroma
from config import CHROMA_DB_PATH
def create_vector_store(chunks, embedding):

    vector_store = Chroma.from_documents(
            documents = chunks,
            embedding = embedding,
            persist_directory = CHROMA_DB_PATH
            )
    return vector_store

def load_vector_store(embedding):
    vector_store = Chroma(
            persist_directory = CHROMA_DB_PATH,
            embedding_function = embedding
            )
    return vector_store



