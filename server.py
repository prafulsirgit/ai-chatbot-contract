from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage
from config import llm
from vector_store import load_vector_store
from chains import create_conversational_chain
import asyncio
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Pydantic model for request body
class ChatRequest(BaseModel):
    message: str

# Initialize chat history (shared across requests)
chat_history = []

# Initialize conversational chain globally (loaded once at startup)
retriever = load_vector_store()
conv_rag_chain = create_conversational_chain(llm, retriever)

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Handle chat requests from the frontend."""
    try:
        message = request.message
        start_time = time.time()
        
        # Offload synchronous LangChain invoke to a thread to prevent blocking
        response = await asyncio.to_thread(
            conv_rag_chain.invoke,
            {"chat_history": chat_history, "input": message}
        )
        
        # Calculate processing time and log status only
        elapsed = (time.time() - start_time) * 1000  # Convert to milliseconds
        logger.info(f"Request processed successfully in {elapsed:.2f}ms")
        
        # Update chat history with user message and AI response
        chat_history.append(HumanMessage(content=message))
        chat_history.append(AIMessage(content=response["answer"]))
        
        # Return the assistant's response
        return {"reply": response["answer"]}
    except Exception as e:
        elapsed = (time.time() - start_time) * 1000 if 'start_time' in locals() else 0
        logger.error(f"Request failed: {str(e)} (elapsed: {elapsed:.2f}ms)")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)