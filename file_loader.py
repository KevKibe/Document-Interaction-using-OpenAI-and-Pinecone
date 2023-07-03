import langchain
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader

class DocumentLoader:
    def load_file(self, file_path):
        documents = []

        if file_path is not None:
            file_name = file_path.name
            if file_name.endswith(".pdf"):
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())
            elif file_name.endswith('.docx') or file_name.endswith('.doc'):
                loader = Docx2txtLoader(file_path)
                documents.extend(loader.load())
            elif file_name.endswith('.txt'):
                loader = TextLoader(file_path)
                documents.extend(loader.load())

        return documents