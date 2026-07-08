from langchain_community.document_loaders import PyPDFLoader
from config import DOWNLOAD_FOLDER
import os 

def load_documents():
    documents =[]

    for file in os.listdir(DOWNLOAD_FOLDER):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(DOWNLOAD_FOLDER, file)

            print(pdf_path)


    loader = PyPDFLoader(pdf_path)
    pdf_documents = loader.load()

    print(type(pdf_documents))
    print(len(pdf_documents))

    documents.extend(pdf_documents)

    return documents 
