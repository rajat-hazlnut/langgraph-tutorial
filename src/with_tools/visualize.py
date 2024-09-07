from src.with_tools.graph_builder import build_graph

try:
    graph = build_graph()
    graph_path = "./src/with_tools/visualize_graph.png"
    graph.get_graph().draw_png(graph_path)
except Exception:
    pass