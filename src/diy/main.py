from src.graph_builder import build_math_graph

graph = build_math_graph()

while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        print(event)
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)