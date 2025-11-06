import os 
from dotenv import load_dotenv

from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.constants import START, END

load_dotenv()

class state(TypedDict):
    query: str
    llm_result: str | None

def chat_bot(state: state):
    # calls
    query = state['query']
    result = "how can i help you"
    state['llm_result'] = result

    return state

graph_builder = StateGraph(state)
graph_builder.add_node("chat_bot" , chat_bot)

graph_builder.add_edge(START, "chat_bot")
graph_builder.add_edge("chat_bot", END)

graph = graph_builder.compile()

def main():
    user = input("> ")

    # invoke the graph
    _state = {
        "query": user,
        "llm_result": str | None
    }

    graph_result = graph.invoke(_state)
    print("result ", graph_result)
    
main()