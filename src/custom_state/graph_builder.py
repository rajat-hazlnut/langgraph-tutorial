from langgraph.graph import StateGraph, START, END
from src.custom_state.state import State
from src.custom_state.agent import agent, human_node
from src.custom_state.tools import get_tools
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

def build_graph() -> StateGraph:
    graph = StateGraph(State)
    memory = MemorySaver()
 
    # Create Nodes
    graph.add_node("agent", agent)
    tool_node = ToolNode(tools=get_tools())
    graph.add_node("tools", tool_node)
    graph.add_node("human", human_node)
    
    # Create Edges
    graph.set_entry_point("agent")
    graph.add_conditional_edges(
        "agent",
        tools_condition 
    )
    graph.add_edge("tools", "agent")
    graph.add_edge("agent", END)
    graph.add_conditional_edges("agent", select_next_node, {"human": "human", "tools": "tools", "__end__": "__end__"})
    graph.add_edge("human", "agent")

    # Compile Graph
    compiled_graph = graph.compile(checkpointer=memory, interrupt_before=["human"])
    return compiled_graph

def select_next_node(state: State):
    if state["ask_human"]:
        return "human"
    # Otherwise, we can route as before
    return tools_condition(state)

