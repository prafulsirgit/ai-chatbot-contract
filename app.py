# app.py
from langchain_core.messages import HumanMessage, AIMessage
from config import llm
from vector_store import load_vector_store
from chains import create_conversational_chain

# Initialize chat history
chat_history = []

def chat_fn(message):
    """Handles chat interaction with the conversational chain."""
    global chat_history
    response = conv_rag_chain.invoke({"chat_history": chat_history, "input": message})
    chat_history.append(HumanMessage(content=message))
    chat_history.append(AIMessage(content=response["answer"]))
    return response["answer"]

def main():
    """Main function to set up and run the command-line chat application."""
    global conv_rag_chain
    # Load existing vector store
    print("Loading vector database...")
    retriever = load_vector_store()
    
    # Create conversational chain
    conv_rag_chain = create_conversational_chain(llm, retriever)
    
    # Command-line chat loop
    print("AI Student Assistant: Ask a question (type 'exit' to quit)")
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_fn(message)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()