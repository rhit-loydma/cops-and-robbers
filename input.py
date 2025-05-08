import networkx as nx
from networkx.classes.graph import Graph


def addEdge(graph: Graph, node: int, node2: int):
    graph.add_edge(node, node2)
    graph.add_edge(node2, node)

def removeEdge(graph: Graph, node: int, node2: int):
    graph.remove_edge(node, node2)
    graph.remove_edge(node2, node)

def addNextNode(graph: Graph):
    graph.add_node(len(graph.nodes()) + 1)

def commandLoop(graph: Graph):
    while True:
        print("q - quit, n - add node, e - add edge")
        command = input()
        if command == 'q':
            break
        if command == 'n':
            addNextNode(graph)
        if command == 'e':
            print("Input index of first node")
            node = int(input())
            print("Input index of second node")
            node2 = int(input())
            addEdge(graph, node, node2)
        if command == 'r':
            print("Input index of first node")
            node = int(input())
            print("Input index of second node")
            node2 = int(input())
            removeEdge(graph, node, node2)