from src.memory.graph_builder import build_graph

graph = build_graph()

while True:
    user_input = input("User: ")
    print("\n")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        print(f"Event: {event}\n\n")
        for value in event.values():
            response = value['messages'][-1].content
            print(f"Assistant: {response}\n\n")