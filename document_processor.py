# document_processor.py
import glob
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import DATA_PATH

def load_and_split_documents():
    """Load and split documents from the knowledge base."""
    files = glob.glob(DATA_PATH + "*")
    docs = []
    
    for file in files:
        if file.endswith(".pdf"):
            loader = PyPDFLoader(file)
            docs.extend(loader.load())
        elif file.endswith(".txt"):
            loader = TextLoader(file, encoding="utf-8")
            docs.extend(loader.load())
        elif file.endswith(".csv"):
            from langchain.document_loaders.csv_loader import CSVLoader
            loader = CSVLoader(file_path=file, encoding="utf-8")
            docs.extend(loader.load())

    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    return text_splitter.split_documents(docs)