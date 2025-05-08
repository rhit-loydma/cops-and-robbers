import networkx as nx
from networkx.classes.graph import Graph


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
        print("q - quit, n - add node, e - add edge, r - remove edge")
        command = input()
        if command == 'q':
            break
        if command == 'n':
            index: int = addNextNode(graph)
            print("Added node index " + str(index))
        if command == 'e':
            print("Input index of first node")
            node = int(input())
            print("Input index of second node")
            node2 = int(input())
            success: bool = addEdge(graph, node, node2)
            if success: 
                print("Added edge from " + str(node) + " to " + str(node2))
            else:
                print("Edge from " + str(node) + " to " + str(node2) + " already exists")
        if command == 'r':
            print("Input index of first node")
            node = int(input())
            print("Input index of second node")
            node2 = int(input())
            success: bool = removeEdge(graph, node, node2)
            if success: 
                print("Removed edge from " + str(node) + " to " + str(node2))
            else:
                print("Edge from " + str(node) + " to " + str(node2) + " doesn't exist")