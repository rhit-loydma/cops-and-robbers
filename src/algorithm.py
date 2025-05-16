import networkx as nx
import itertools
from os import makedirs
from viz import draw_graph, create_gif

def is_cop_win(G, filepath="greedy_algorithm.gif"):
    makedirs("temp", exist_ok=True)
    pos = nx.spring_layout(G, seed=0)
    i = 0
    b = True
    is_cop_win = False
    while b:
        draw_graph(G, pos, f"temp/{i}.png")
        i += 1
        G, b = iterate(G)
        if len(G.nodes()) == 1:
            is_cop_win = True
            break
    draw_graph(G, pos, f"temp/{i}.png")
    create_gif(filepath, "temp", i+1)
    return is_cop_win

def iterate(G):
    # get attributes
    G = set_attributes(G)

    # find node to remove
    for (u,v,a) in G.edges(data=True):
        if G.nodes[u]["degree_minus_one"] == a["triangle_count"]:
            G.remove_node(u)
            return G, True
        if G.nodes[v]["degree_minus_one"] == a["triangle_count"]:
            G.remove_node(v)
            return G, True
        
    # no node found, not cop-win
    return G, False   

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