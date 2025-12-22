import os
from dotenv import load_dotenv
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from typing_extensions import TypedDict
from langchain_ollama.chat_models import ChatOllama

load_dotenv()

