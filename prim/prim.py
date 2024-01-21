from class_for_dijkstra import PriorityQueue, Graph

def prim(G, start):
    pq = PriorityQueue()
    start.setDistacne(0)

    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getWeight(nextVert):
            newCost = currentVert.getWeight(nextVert)
            if nextVert in pq and newCost <nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)

if __name__ == "__main__":
    G1 = Graph()
    ndedge = [('a', 'B', 2), ('A', 'C', 3), ('B', 'C', 1),
              ('B', 'D', 1), ('B', 'E', 4), ('C', 'F', 5),
              ('D', 'E', 1), ('E', 'F', 1), ('F', 'G', 1)]

    for nd in ndedge:
        G1.addEdge(nd[0], nd[1], nd[2])
        G1.addEdge(nd[1], nd[0], nd[2])
    print("Shortest Paths in Figure 4:")
    G1.printShortestPaths(G1.getVertex('A'))
