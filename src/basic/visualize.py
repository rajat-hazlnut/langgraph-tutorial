from src.basic.graph_builder import build_graph

try:
    graph = build_graph()
    graph_path = "./src/basic/visualize_graph.png"
    graph.get_graph().draw_png(graph_path)
except Exception:
    pass