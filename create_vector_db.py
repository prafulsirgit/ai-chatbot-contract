# create_vector_db.py
from document_processor import load_and_split_documents
from vector_store import create_vector_store

def main():
    """Create or update the vector database from knowledge base documents."""
    print("Loading and splitting documents...")
    documents = load_and_split_documents()
    
    print("Creating vector database...")
    create_vector_store(documents)
    
    print("Vector database created successfully!")

if __name__ == "__main__":
    main()