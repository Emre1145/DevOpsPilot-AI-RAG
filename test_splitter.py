from loader import load_documents
from text_splitter import split_documents

documents = load_documents()

print(type(documents))
print(len(documents))



