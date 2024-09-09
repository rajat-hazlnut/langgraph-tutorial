from src.manually_updating_state.graph_builder import build_graph
from langgraph.graph import StateGraph

graph: StateGraph = build_graph()

while True:
    user_input = input("User: ")
    print("\n")
    config = {"configurable": {"thread_id": "1"}}
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
     
    events = graph.stream({"messages": [("user", user_input)]}, config, stream_mode="values")

    for event in events:
        print(f"Event: {event}\n\n")
        event["messages"][-1].pretty_print()
    
    snapshot = graph.get_state(config)
    print(f"\nSnapshot: {snapshot}\n")
    existing_message = snapshot.values["messages"][-1]
    existing_message.pretty_print()