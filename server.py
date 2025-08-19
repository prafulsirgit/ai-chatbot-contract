# backend/server.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage
from config import llm
from vector_store import load_vector_store
from chains import create_conversational_chain

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Pydantic model for request body
class ChatRequest(BaseModel):
    message: str

# Initialize chat history
chat_history = []

# Initialize conversational chain
retriever = load_vector_store()
conv_rag_chain = create_conversational_chain(llm, retriever)

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Handle chat requests from the frontend."""
    try:
        # Get user message
        message = request.message
        
        # Invoke the conversational chain
        response = conv_rag_chain.invoke({"chat_history": chat_history, "input": message})
        
        # Update chat history
        chat_history.append(HumanMessage(content=message))
        chat_history.append(AIMessage(content=response["answer"]))
        
        # Return the assistant's response
        return {"reply": response["answer"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)