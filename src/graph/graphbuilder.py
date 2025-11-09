from src.state.state import State
from src.nodes.router import router_node
from src.nodes.subject import subject_node
from src.nodes.body import body_node
from src.nodes.aggregator import aggregator_node
from langgraph.graph import StateGraph, START, END


# Build the state graph
graph = StateGraph(State)

graph.add_node("Router_node", router_node)
graph.add_node("Subject_node", subject_node)
graph.add_node("Body_node", body_node)
graph.add_node("Aggregator_node", aggregator_node)

graph.add_edge(START, "Router_node")
graph.add_edge("Router_node", "Subject_node")
graph.add_edge("Router_node", "Body_node")
graph.add_edge("Subject_node", "Aggregator_node")
graph.add_edge("Body_node", "Aggregator_node")
graph.add_edge("Aggregator_node", END)

final_graph =graph.compile()








