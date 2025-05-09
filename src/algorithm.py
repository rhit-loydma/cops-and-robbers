import networkx as nx
import itertools
from viz import draw_graph

def get_edge_counts(G):
    # initialize all edge counts
    nx.set_edge_attributes(G, 0, "triangle_count")

    # find traingles
    for clique in nx.enumerate_all_cliques(G):
        if len(clique) == 3:
            for u, v in list(itertools.combinations(clique, 2)):
                attr = {(u, v): {"triangle_count": G[u][v]["triangle_count"] + 1}}
                nx.set_edge_attributes(G, attr)
        elif len(clique) > 3:
            break
    return G

def get_degree_counts(G):
    # find the degree of each vertex minus one
    degrees_minus_one = [G.degree[i] - 1 for i in G.nodes()]
    attrs = {n: {"degree_minus_one": degrees_minus_one[i]} for i, n in enumerate(G.nodes())}
    nx.set_node_attributes(G, attrs)
    return G

def set_attributes(G):
    G = get_edge_counts(G)
    G = get_degree_counts(G)
    return G

# G = nx.gnm_random_graph(10, 20, seed=0)
# G = set_attributes(G)
# draw_graph(G)
