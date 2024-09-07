from langgraph.graph import StateGraph, START, END
from src.with_tools.state import State
from src.with_tools.agent import agent
from src.with_tools.tools import get_tools
from src.with_tools.tool_node import ToolNode
from langgraph.prebuilt import ToolNode, tools_condition

def build_graph() -> StateGraph:
    graph = StateGraph(State)
 
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
    compiled_graph = graph.compile()
    return compiled_graph

