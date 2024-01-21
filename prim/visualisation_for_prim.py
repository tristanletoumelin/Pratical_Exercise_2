import networkx as nx
import matplotlib.pyplot as plt
from prim import Graph

def visualize_minimum_spanning_tree(graph, minimum_spanning_tree):
    G = nx.Graph()

    for edge in minimum_spanning_tree:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    pos = nx.spring_layout(G)  # Layout algorithm (you can use other layouts)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Minimum Spanning Tree")
    plt.show()

# Example usage:
if __name__ == "__main__":
    ndege_fig_1 = [('u', 'v', 2), ('u', 'w', 5), ('u', 'x', 1),
                   ('v', 'x', 2), ('v', 'w', 3), ('x', 'w', 3),
                   ('y', 'z', 1), ('w', 'y', 1), ('w', 'z', 5),]

    G1 = Graph()
    for edge in ndege_fig_1:
        G1.addEdge(*edge)

    minimum_spanning_tree = G1.prim_algorithm('u')
    visualize_minimum_spanning_tree(G1, minimum_spanning_tree)
