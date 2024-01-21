from class_for_dijkstra import Graph, PriorityQueue
import matplotlib as plt

def dijkstra_algo(G, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G.getVertices()])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert[1].getConnections():
            newDist = currentVert[1].getDistance() + currentVert[1].getWeight(nextVert)
            if newDist<nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert[1])
                pq.decreaseKey(nextVert, newDist)

if __name__ == "__main__":
    ndege_fig_1 = [('u', 'v', 2), ('u', 'w', 5), ('u', 'x', 1),
                   ('v', 'x', 2), ('v', 'w', 3), ('x', 'w', 3),
                   ('y', 'z', 1), ('w', 'y', 1), ('w', 'z', 5),]
    G1 = Graph()
    G1.addEdges(ndege_fig_1)
    dijkstra_algo(G1, G1.getVertex('u'))
    print("Shortest Paths in Figure 1:")
    # G1.printShortestPaths(G1.getVertex('u'))
    # G1.printShortestPaths()
    G1.plotGraph()
    plt.title("Graph Figure 1")
    plt.show()
# #==============================================================
    print("\n\n\n")
    ndege_fig_2 = [('a', 'b', 3), ('a', 'e', 1), ('a', 'f', 6),
                   ('f', 'e', 2), ('e', 'b', 1), ('b', 'c', 4),
                   ('c', 'd', 9), ('d', 'e' , 1)]
    G2 = Graph()
    G2.addEdges(ndege_fig_2)
    dijkstra_algo(G2, G2.getVertex('a'))
    print("Shortest Paths in Figure 2:")
    G2.printShortestPaths(G2.getVertex('a'))
# #==============================================================
    print("\n\n\n")
    ndege_fig_3 = [('u', 'v', 3), ('u', 'w', 2), ('v', 'y', 2),
                   ('v', 'x', 1), ('w', 'x', 1), ('w', 's', 4),
                   ('y', 'z', 1), ('x', 'z', 4), ('x', 't', 5),
                   ('t', 's', 3)]
    G3 = Graph()
    G3.addEdges(ndege_fig_3)
    dijkstra_algo(G3, G3.getVertex('u'))
    print("Shortest Paths in Figure 3:")
    G3.printShortestPaths(G3.getVertex('u'))
# #==============================================================
    print("\n\n\n")
    ndege_fig_4 = [('a', 'b', 2), ('a', 'c', 3), ('b', 'c', 1),
                   ('b', 'd', 1), ('b', 'e', 4), ('d', 'e', 1),
                   ('e', 'f', 1), ('c', 'f', 5), ('f', 'g', 1)]
    G4 = Graph()
    G4.addEdges(ndege_fig_4)
    dijkstra_algo(G4, G4.getVertex('a'))
    print("Shortest Paths in Figure 4:")
    G4.printShortestPaths(G4.getVertex('a'))
# #==============================================================
    print("\n\n\n")
    ndege_fig_5 = [('a', 'b', 5), ('a', 'c', 10), ('b', 'c', 3),
                   ('b', 'd', 11), ('d', 'c', 2)]
    G5 = Graph()
    G5.addEdges(ndege_fig_5)
    dijkstra_algo(G5, G5.getVertex('a'))
    print("Shortest Paths in Figure 5:")
    G5.printShortestPaths(G5.getVertex('a'))
