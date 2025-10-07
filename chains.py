# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain.chains.history_aware_retriever import create_history_aware_retriever
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.chains.retrieval import create_retrieval_chain
# from functools import lru_cache

# @lru_cache(maxsize=500)
# def create_conversational_chain(llm, retriever):
#     """Create and return the conversational RAG chain."""
#     # History-aware retriever prompt
#     contextualize_prompt = ChatPromptTemplate.from_messages([
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("system", "Rewrite the latest user question into a self-contained question, using conversation history."),
#         ("user", "{input}")
#     ])
    
#     history_aware_retriever = create_history_aware_retriever(
#         llm=llm,
#         retriever=retriever,
#         prompt=contextualize_prompt
#     )

#     # Answer chain prompt with Markdown formatting instructions
#     answer_prompt = ChatPromptTemplate.from_messages([
#         ("system", """You are an educational chatbot for all engineering colleges in Nagpur district.  
# Your job is to answer student queries related to admissions, courses, fees, results, placements, cutoffs, and facilities.  

# When handling queries:
# 1. If the student clearly mentions a specific college, refine their query and answer using the provided context.
# 2. If the student does not mention a college, first check if the query is general:
#    - If it is a general fact (true for almost all Nagpur engineering colleges), answer directly without searching the context. 
#    - If it requires college-specific details, politely ask which engineering college they are referring to.
# 3. If the query is vague, incomplete, or ambiguous, reformulate it and/or ask a clarifying question.
# 4. If no answer is found in the context, provide the best accurate general answer you know instead of leaving the query unanswered.
# 5. Always reply in a clear, supportive, and strict professional help desk assistant manner.
# 6. Format the response in Markdown with clear headings (###), bullet points (-), and bold text (**text**) for key terms or emphasis to ensure readability and structure.
# 7. Do not start or end with casual greetings like 'hey,' 'hello,' or 'hi'; keep the message concise and professional.

# Context:
# {context}"""),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("user", "{input}")
#     ])
    
#     doc_chain = create_stuff_documents_chain(llm=llm, prompt=answer_prompt)
#     return create_retrieval_chain(history_aware_retriever, doc_chain)

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

def create_conversational_chain(llm, retriever):
    """Create and return the conversational RAG chain."""
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

    answer_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an educational chatbot for all engineering colleges in Nagpur district.  
Your job is to answer student queries related to admissions, courses, fees, results, placements, cutoffs, and facilities.  

When handling queries:
1. If the student clearly mentions a specific college, refine their query and answer using the provided context.
2. If the student does not mention a college, first check if the query is general:
   - If it is a general fact (true for almost all Nagpur engineering colleges), answer directly without searching the context. 
   - If it requires college-specific details, politely ask which engineering college they are referring to.
3. If the query is vague, incomplete, or ambiguous, reformulate it and/or ask a clarifying question.
4. If no answer is found in the context, provide the best accurate general answer you know instead of leaving the query unanswered.
5. Always reply in a clear, supportive, and strict professional help desk assistant manner.
6. Format the response in Markdown with clear headings (###), bullet points (-), and bold text (**text**) for key terms or emphasis to ensure readability and structure.
7. Do not start or end with casual greetings like 'hey,' 'hello,' or 'hi'; keep the message concise and professional.

Context:
{context}"""),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])
    
    doc_chain = create_stuff_documents_chain(llm=llm, prompt=answer_prompt)
    return create_retrieval_chain(history_aware_retriever, doc_chain)