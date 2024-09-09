from src.manually_updating_state.graph_builder import build_graph

try:
    graph = build_graph()
    graph_path = "./src/manually_updating_state/visualize_graph.png"
    graph.get_graph().draw_png(graph_path)
except Exception:
    pass