import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def draw_graph(G):
    pos = nx.spring_layout(G, seed=0)
    G = color_graph(G)
    edge_colors = [data["color"] for u, v, data in G.edges(data=True)]
    node_colors = [data["color"] for v, data in G.nodes(data=True)]
    node_labels = {v: data["degree_minus_one"] + 1 for v, data in G.nodes(data=True)}
    edge_labels = {(u,v): data["triangle_count"] for u, v, data in G.edges(data=True)}

    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, width=2.0, edge_color=edge_colors)
    nx.draw_networkx_labels(G, pos, node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)
    plt.show()

def color_graph(G):
    triangle_counts = nx.get_edge_attributes(G, "triangle_count").values()
    degrees_minus_one = nx.get_node_attributes(G, "degree_minus_one").values()
    
    # define color mapping based on the max of above values
    try: 
        max_value = max(max(triangle_counts), max(degrees_minus_one))
        min_value = min(min(triangle_counts), min(degrees_minus_one))
        divisor = max(max_value - min_value, 1)
    except ValueError:
        divisor = 1

    edge_attrs = {e: {"color": cm.rainbow((G[e[0]][e[1]]["triangle_count"] - min_value) / divisor)} for e in G.edges()}
    nx.set_edge_attributes(G, edge_attrs)

    node_attrs = {v: {"color": cm.rainbow((G.degree[v] - 1.0 - min_value) / divisor)} for v in G.nodes()}
    nx.set_node_attributes(G, node_attrs)
    return G