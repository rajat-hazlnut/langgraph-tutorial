from langgraph.graph import StateGraph, START, END
from src.memory.state import State
from src.memory.agent import agent
from langgraph.checkpoint.memory import MemorySaver

def build_graph() -> StateGraph:
    graph = StateGraph(State)

    # Memory
    memory = MemorySaver()
    config = {"configurable": {"thread_id": "1"}}
 
    # Create Nodes
    graph.add_node("agent", agent)
    
    # Create Edges
    graph.set_entry_point("agent")
    graph.add_edge("agent", END)

    # Compile Graph
    compiled_graph = graph.compile(checkpointer=memory)
    return compiled_graph

