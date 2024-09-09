from src.diy.graph_builder import build_graph
from langgraph.graph import StateGraph

try:
    graph: StateGraph = build_graph()
    graph_path = "./visualize_graph.png"
    graph.get_graph().draw_mermaid_png(graph_path)
except Exception:
    pass