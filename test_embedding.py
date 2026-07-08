from loader import load_documents
from text_splitter import split_documents
from embedding import create_embeddings

documents = load_documents()

chunks = split_documents(documents)

embeddings = create_embeddings(chunks)

print(type(documents))
print(len(documents))

print("=" * 60)

print(type(chunks))
print(len(chunks))


print("=" * 60)


print(type(embeddings))



