# chains.py
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

def create_conversational_chain(llm, retriever):
    """Create and return the conversational RAG chain."""
    # History-aware retriever prompt
    contextualize_prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("system", "Rewrite the latest user question into a self-contained question, using conversation history."),
        ("user", "{input}")
    ])
    
    history_aware_retriever = create_history_aware_retriever(
        llm=llm,
        retriever=retriever,
        prompt=contextualize_prompt
    )
    
    # Answer chain prompt
    answer_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an AI-powered student assistant for a technical educational institute.
Use ONLY the provided context to answer questions.
If the answer is not in the context, say: "I’m sorry, I don’t have that information in the knowledge base."
Be clear, concise, and professional.

Context:
{context}"""),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])
    
    doc_chain = create_stuff_documents_chain(llm=llm, prompt=answer_prompt)
    return create_retrieval_chain(history_aware_retriever, doc_chain)