import threading
import networkx as nx
from networkx import Graph
from input import *

graph: Graph = nx.Graph()
commandLoop(graph)