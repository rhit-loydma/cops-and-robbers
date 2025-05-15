import networkx as nx
import pickle
from networkx.classes.graph import Graph
from viz import draw_graph
from algorithm import set_attributes

def addEdge(graph: Graph, node: int, node2: int) -> bool:
    if graph.has_edge(node, node2) == True:
        return False
    graph.add_edge(node, node2)
    return True

def removeEdge(graph: Graph, node: int, node2: int) -> bool:
    if graph.has_edge(node, node2) == False:
        return False
    graph.remove_edge(node, node2)
    return True

def addNextNode(graph: Graph) -> int:
    nodeIndex: int = len(graph.nodes())
    graph.add_node(nodeIndex)
    return nodeIndex

def commandLoop(graph: Graph):
    while True:
        print("q - quit, n - add node, e NODE1 NODE2 - add edge, r NODE1 NODE2 - remove edge, d - draw graph, s NAME - save graph, l NAME - load graph")
        commands = input().split(" ")
        command = commands[0]
        if command == 'q' and len(commands) == 1:
            exit()
        if command == 'n' and len(commands) == 1:
            index: int = addNextNode(graph)
            print("Added node index " + str(index))
        if command == 'e' and len(commands) == 3:
            node = int(commands[1])
            node2 = int(commands[2])
            success: bool = addEdge(graph, node, node2)
            if success: 
                print("Added edge from " + str(node) + " to " + str(node2))
            else:
                print("Edge from " + str(node) + " to " + str(node2) + " already exists")
        if command == 'r' and len(commands) == 3:
            node = int(commands[1])
            node2 = int(commands[2])
            success: bool = removeEdge(graph, node, node2)
            if success: 
                print("Removed edge from " + str(node) + " to " + str(node2))
            else:
                print("Edge from " + str(node) + " to " + str(node2) + " doesn't exist")
        if command == "d" and len(commands) == 1:
            if graph.number_of_edges() == 0:
                print("You need to add an edge before drawing the graph.")
                continue
            print("Drawing graph. Close window to continue editing the graph.")
            set_attributes(graph)
            draw_graph(graph)
        if command == "s" and len(commands) == 2:
            file = commands[1]
            with open(file, "wb") as f:
                pickle.dump(graph, f)
        if command == "l" and len(commands) == 2:
            file = commands[1]
            with open(file, 'rb') as file:
                graph = pickle.load(file)