# config.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Setup API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyB8RbC--YOAzcGgiaB3lyo1WgDAbe7tojc"  # Replace with your key

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)

# Data path
DATA_PATH = "./data/knowledge_base/"