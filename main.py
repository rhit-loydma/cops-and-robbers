import threading
import networkx as nx
from networkx import Graph
from input import *
from src.example_viz import *

graph: Graph = nx.Graph()
commandLoop(graph)