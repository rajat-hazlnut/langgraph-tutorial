from src.with_memory.graph_builder import build_graph

try:
    graph = build_graph()
    graph_path = "./src/with_memory/visualize_graph.png"
    graph.get_graph().draw_png(graph_path)
except Exception:
    pass