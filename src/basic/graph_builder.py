from langgraph.graph import StateGraph, START, END
from src.basic.state import State
from src.basic.agent import agent

def build_graph() -> StateGraph:
    graph = StateGraph(State)
 
    # Create Nodes
    graph.add_node("agent", agent)
    
    # Create Edges
    graph.set_entry_point("agent")
    graph.add_edge("agent", END)

    # Compile Graph
    compiled_graph = graph.compile()
    return compiled_graph

