from dijkstra import dijkstra_algo
from class_for_dijkstra import Graph
import networkx as nx
import matplotlib.pyplot as plt

def plot_shortest_paths(graph, start_vertex):
    # Create a directed graph
    G = nx.DiGraph()

    # Add edges to the graph
    for vertex in graph.getVertices():
        for neighbor, weight in vertex.connectedTo.items():
            G.add_edge(vertex.getId(), neighbor.getId(), weight=weight)

    # Extract positions of vertices for better layout
    pos = nx.spring_layout(G, k = 0.9)

    # Plot each shortest path in a different figure
    for vertex in graph.getVertices():
        path = []
        current = vertex
        while current.getPred():
            path.append(current.getId())
            current = current.getPred()
        path.append(start_vertex.getId())
        path.reverse()

        # Create a new graph for each path
        G_path = nx.DiGraph()
        for i in range(len(path) - 1):
            G_path.add_edge(path[i], path[i + 1], weight=G[path[i]][path[i + 1]]['weight'])

        # Draw all nodes
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
        nx.draw_networkx_labels(G, pos)

        # Draw all edges with weights
        edge_labels = {(edge[0], edge[1]): G[edge[0]][edge[1]]['weight'] for edge in G.edges()}
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black', width=2, arrows=False)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Highlight edges in the path with a different color
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        edge_colors = ['red' if G[path[i]][path[i + 1]]['weight'] == graph.getVertex(path[i]).getWeight(graph.getVertex(path[i + 1])) else 'black' for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors, width=2)

        # Annotate the total distance on the graph
        total_distance = vertex.getDistance()
        plt.annotate(f'Total distance: {total_distance}', xy=(0.5, -0.1), xycoords="axes fraction", ha="center", va="center", fontsize=10, bbox=dict(boxstyle="round", alpha=0.1, color="white"))

        # Show the plot for each path
        plt.title(f"Shortest Path from {start_vertex.getId()} to {vertex.getId()}")
        plt.show()


if __name__ == "__main__":

    ndege_fig_5 = [('a', 'b', 5), ('a', 'c', 10), ('b', 'c', 3),
                   ('b', 'd', 11), ('d', 'c', 2)]
    G5 = Graph()
    G5.addEdges(ndege_fig_5)
    dijkstra_algo(G5, G5.getVertex('a'))
    print("Shortest Paths in Figure 5:")
    plot_shortest_paths(G5, G5.getVertex('a'))
