
import os
from dotenv import load_dotenv
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from typing_extensions import TypedDict
from langchain_ollama.chat_models import ChatOllama

load_dotenv()

# state
class State(TypedDict):
    query: str
    llm_result: str | None
    query_type: str | None    # 'g' or 'c'

# nodes
def query_check(state: State):
    """Classify query as general (g) or coding (c)."""
    SYS_PROMPT = (
        "You are a query checker that takes an input and decides if the query "
        "is general or coding-related. If it's general, respond ONLY with 'g'. "
        "If it's coding-related, respond ONLY with 'c'."
    )

    llm = ChatOllama(model="llama3")

    response = llm.invoke([
        {"role": "system", "content": SYS_PROMPT},
        {"role": "user", "content": state["query"]},
    ])

    query_type = response.content.strip().lower()
    print(f"Query type: {query_type}")
    state["query_type"] = query_type
    return state


def route_query(state: State):
    """Route query to the appropriate node."""
    if state["query_type"] == "g":
        return "general_query"
    elif state["query_type"] == "c":
        return "coding_query"
    else:
        # fallback to general
        return "general_query"


def general_query(state: State):
    """Handle general questions using Ollama."""
    llm = ChatOllama(model="llama3")

    response = llm.invoke([
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": state["query"]},
    ])

    answer = response.content
    print(f"General query response: {answer}")
    state["llm_result"] = answer
    return state


def coding_query(state: State):
    """Use Ollama for generating coding answers."""
    llm = ChatOllama(model="llama3")

    response = llm.invoke([
        {"role": "system", "content": "You are an expert coding assistant."},
        {"role": "user", "content": state["query"]},
    ])

    answer = response.content
    print(f"Coding response: {answer}")
    state["llm_result"] = answer
    return state


def coding_validation_query(state: State):
    """Validate code output using Ollama."""
    llm = ChatOllama(model="llama3")

    validation_prompt = (
        "You are a code reviewer. Check the following code or explanation "
        "for correctness, logic errors, or missing context. Give a concise verdict "
        "like 'Looks good' or 'Needs improvement' with reason.\n\n"
        f"Code/Answer:\n{state['llm_result']}"
    )

    response = llm.invoke([
        {"role": "user", "content": validation_prompt}
    ])

    validation = response.content
    print(f"Validation result: {validation}")
    state["llm_result"] += "\n\n✅ Validation Result:\n" + validation
    return state

# ---------- GRAPH ----------
graph_builder = StateGraph(State)

# add nodes
graph_builder.add_node("query_check", query_check)
graph_builder.add_node("route_query", route_query)
graph_builder.add_node("general_query", general_query)
graph_builder.add_node("coding_query", coding_query)
graph_builder.add_node("coding_validation_query", coding_validation_query)

# edges
graph_builder.add_edge(START, "query_check")
graph_builder.add_conditional_edges("query_check", route_query)
graph_builder.add_edge("coding_query", "coding_validation_query")
graph_builder.add_edge("general_query", END)
graph_builder.add_edge("coding_validation_query", END)

# compile graph
graph = graph_builder.compile()

# ---------- MAIN ----------
def main():
    user_query = input("> ")
    initial_state = {"query": user_query, "llm_result": None, "query_type": None}
    for event in graph.stream(initial_state):
        print("event", event)

    final_state = graph.invoke(initial_state)
    print("\nFinal Answer:\n", final_state["llm_result"])


if __name__ == "__main__":
    main()
