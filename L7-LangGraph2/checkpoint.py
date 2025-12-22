import os

from dotenv import load_dotenv
# from langchain_community.chat_models import ChatOllama
from langchain_ollama.chat_models import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.mongodb import MongoDBSaver
from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnableConfig
from langgraph.graph.message import add_messages 
from typing import Annotated
from typing_extensions import TypedDict
from operator import add

load_dotenv()

class State(TypedDict):
    messages: Annotated[list, add_messages]

# llm = init_chat_model(model_provider="google_genai" , model="gemini-2.0-flash")
llm = ChatOllama(model="llama3")

def chat_node(state: State):
    response = llm.invoke(state["messages"])
    return {"messages" : [response]}


graphBuilder = StateGraph(State)

graphBuilder.add_node("chat_node", chat_node)

graphBuilder.add_edge(START, "chat_node")
graphBuilder.add_edge("chat_node", END)

graph = graphBuilder.compile()

def make_graph_with_checkpointer(checkpointer):
    graph_with_checkpointer = graphBuilder.compile(checkpointer=checkpointer)
    return graph_with_checkpointer

# checkpointer = InMemorySaver()
# graph = graphBuilder.compile(checkpointer=checkpointer)

# config: RunnableConfig = {"configurable": {"thread_id": "1"}}
# graph.invoke({"foo": ""}, config)

def main():
    DB_URI = "mongodb://admin:admin@localhost:27017"
    config = {"configurable": {"thread_id": "1"}} 
    with MongoDBSaver.from_conn_string(DB_URI) as mongo_checkpointer:
        graph_with_mongo = make_graph_with_checkpointer(mongo_checkpointer)
        query = input("> ")
        # if query.lower() in {"exit", "quit"}:
        #     break
        result = graph_with_mongo.invoke({"messages": [{"role": "user", "content": query}]}, config) 
        print(result["messages"][-1].content)


main()