# vector_store.py
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def create_vector_store(documents):
    """Create a new vector store from documents and save to disk."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Chroma.from_documents(documents, embeddings, persist_directory="./chroma_db")
    return vectordb

def load_vector_store():
    """Load an existing vector store from disk."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    return vectordb.as_retriever(search_kwargs={"k": 3})