from document_processor import load_and_split_documents
from vector_store import create_vector_store
from langchain.text_splitter import RecursiveCharacterTextSplitter
import torch

def main():
    """Create or update the vector database from knowledge base documents."""
    print("Loading and splitting documents...")
    documents = load_and_split_documents()
    
    # Optimize chunking (assumes document_processor.py returns raw text)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # Smaller chunks for faster indexing
        chunk_overlap=50,
        length_function=len
    )
    chunked_docs = text_splitter.split_documents(documents)
    
    print(f"Creating vector database with {len(chunked_docs)} chunks...")
    create_vector_store(chunked_docs)
    
    print("Vector database created successfully!")

if __name__ == "__main__":
    main()