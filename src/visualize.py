from IPython.display import Image, display
from src.graph_builder import build_graph
from langgraph.graph import StateGraph

try:
    graph: StateGraph = build_graph()
    graph_path = "./graph_output.png"
    graph.get_graph().draw_png(graph_path)
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    pass