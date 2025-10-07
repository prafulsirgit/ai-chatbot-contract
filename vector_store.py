# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS
# from cachetools import LRUCache
# import torch

# # Cache for query embeddings and retrieval results
# query_cache = LRUCache(maxsize=1000)

# def create_vector_store(documents):
#     """Create a new vector store from documents and save to disk."""
#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2",
#         model_kwargs={'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
#     )
#     vectordb = FAISS.from_documents(documents, embeddings, distance_strategy="COSINE")
#     vectordb.save_local("faiss_index")
#     return vectordb

# def load_vector_store():
#     """Load an existing vector store from disk."""
#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2",
#         model_kwargs={'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
#     )
#     vectordb = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    
#     # Wrap retriever with caching
#     def cached_retriever(query):
#         if query in query_cache:
#             return query_cache[query]
#         results = vectordb.as_retriever(search_kwargs={"k": 5}).invoke(query)
#         query_cache[query] = results
#         return results
    
#     return cached_retriever

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS  # Updated import
from langchain_core.runnables import RunnableLambda
from cachetools import LRUCache
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cache for query embeddings and retrieval results
query_cache = LRUCache(maxsize=1000)

def create_vector_store(documents):
    """Create a new vector store from documents and save to disk."""
    try:
        logger.info("Initializing embeddings...")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}  # Explicitly use CPU for faiss-cpu
        )
        logger.info(f"Creating FAISS vector store with {len(documents)} documents...")
        vectordb = FAISS.from_documents(documents, embeddings, distance_strategy="COSINE")
        vectordb.save_local("faiss_index")
        logger.info("Vector store created and saved to faiss_index")
        return vectordb
    except Exception as e:
        logger.error(f"Error creating vector store: {str(e)}")
        raise

def load_vector_store():
    """Load an existing vector store from disk and return a cached retriever."""
    try:
        logger.info("Loading embeddings...")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}  # Explicitly use CPU
        )
        logger.info("Loading FAISS vector store from faiss_index...")
        vectordb = FAISS.load_local(
            folder_path="faiss_index",
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )
        
        # Create base retriever
        base_retriever = vectordb.as_retriever(search_kwargs={"k": 5})
        
        # Wrap retriever with caching using RunnableLambda
        def cached_retriever(query):
            if query in query_cache:
                logger.info(f"Cache hit for query: {query}")
                return query_cache[query]
            logger.info(f"Retrieving for query: {query}")
            results = base_retriever.invoke(query)
            query_cache[query] = results
            return results
        
        logger.info("Vector store loaded successfully")
        return RunnableLambda(cached_retriever)
    except Exception as e:
        logger.error(f"Error loading vector store: {str(e)}")
        raise