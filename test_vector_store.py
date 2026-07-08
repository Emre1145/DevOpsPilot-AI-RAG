from loader import load_documents
from text_splitter import split_documents
from embedding import create_embeddings
from vector_store import create_vector_store


documents = load_documents()

chunks = split_documents(documents)

embedding = create_embeddings()

vector_store = create_vector_store(chunks, embedding)


print(vector_store)
print("Vector Store Created Successfully!")
print(f"Total vectors stored: {vector_store._collection.count()}")



