from langgraph.graph import StateGraph, START, END
from src.basic.state import State
from src.lead_agent import lead_agent
from langgraph.prebuilt.tool_node import ToolNode, tools_condition
from src.math_agent import math_agent
from src.add_tool import AddTool
from src.multiply_tool import MultiplyTool

def build_graph() -> StateGraph:
    graph = StateGraph(State)

    math_tools = ToolNode(tools=[AddTool,MultiplyTool])
    
    graph.add_node("lead_agent", lead_agent)
    graph.add_node("math_agent", math_agent)
    graph.add_node("math_tools", math_tools)

    graph.add_edge(START, "lead_agent")
    graph.add_conditional_edges("lead_agent", END)
    graph.add_conditional_edges("lead_agent", math_agent)
    graph.add_conditional_edges("math_agent", tools_condition)
    graph.add_edge("math_tools", "math_agent")


    compiled_graph = graph.compile()
    return compiled_graph

def build_math_graph() -> StateGraph:
    graph = StateGraph(State)

    math_tools_node = ToolNode(tools=[AddTool,MultiplyTool])
    
    
    graph.add_node("math_agent", math_agent)
    graph.add_node("math_tools_node", math_tools_node)

    graph.add_edge(START, "math_agent")
    graph.add_edge("math_agent", END)
    graph.add_conditional_edges("math_agent", tools_condition)
    graph.add_edge("math_tools_node", "math_agent")


    compiled_graph = graph.compile()
    return compiled_graph

