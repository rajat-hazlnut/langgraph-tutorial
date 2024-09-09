from langgraph.graph import StateGraph, START, END
from src.manually_updating_state.state import State
from src.manually_updating_state.agent import agent
from src.manually_updating_state.tools import get_tools
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

def build_graph() -> StateGraph:
    graph = StateGraph(State)
    memory = MemorySaver()
 
    # Create Nodes
    graph.add_node("agent", agent)
    tool_node = ToolNode(tools=get_tools())
    graph.add_node("tools", tool_node)
    
    # Create Edges
    graph.set_entry_point("agent")
    graph.add_conditional_edges(
        "agent",
        tools_condition 
    )
    graph.add_edge("tools", "agent")
    graph.add_edge("agent", END)

    # Compile Graph
    compiled_graph = graph.compile(checkpointer=memory, interrupt_before=["tools"])
    return compiled_graph

