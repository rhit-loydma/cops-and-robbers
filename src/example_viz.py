import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import itertools

def draw_graph(G):
    pos = nx.spring_layout(G, seed=0)
    edge_colors = [data["color"] for u, v, data in G.edges(data=True)]
    node_colors = [data["color"] for v, data in G.nodes(data=True)]

    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, width=2.0, edge_color=edge_colors)
    plt.show()

def color_graph(G):
    # find how many triangles each edge particpate in
    G = get_edge_counts(G)
    triangle_counts = nx.get_edge_attributes(G, "triangle_count").values()

    # find the degree of each vertex minus one
    degrees_minus_one = [G.degree[i] - 1 for i in G.nodes()]
    attrs = {n: {"degree_minus_one": degrees_minus_one[i]} for i, n in enumerate(G.nodes())}
    nx.set_node_attributes(G, attrs)
    
    # define color mapping based on the max of above values
    max_value = max(max(triangle_counts), max(degrees_minus_one))
    min_value = min(min(triangle_counts), min(degrees_minus_one))
    divisor = max(max_value - min_value, 1)

    edge_attrs = {e: {"color": cm.rainbow((G[e[0]][e[1]]["triangle_count"] - min_value) / divisor)} for e in G.edges()}
    nx.set_edge_attributes(G, edge_attrs)

    node_attrs = {v: {"color": cm.rainbow((G.degree[v] - 1.0 - min_value) / divisor)} for v in G.nodes()}
    nx.set_node_attributes(G, node_attrs)
    return G

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

G = nx.gnm_random_graph(10, 20, seed=0)
G = color_graph(G)
draw_graph(G)