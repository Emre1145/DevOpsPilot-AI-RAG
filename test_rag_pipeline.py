from embedding import create_embeddings
from vector_store import load_vector_store
from retriever import get_retriever
from rag_pipeline import generate_response


question = input("user asking the question(type exit to out )....")
embedding = create_embeddings()
vector_store = load_vector_store(embedding)
retriever = get_retriever(vector_store)

response  = generate_response(retriever, question)

print("Question:", question)
print("\nAnswer:")
print(response)


