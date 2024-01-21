class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = float('inf')
        self.pred = None

    def addNeighbor(self, nbr, weight):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance

    def getPred(self):
        return self.pred

    def setPred(self, pred):
        self.pred = pred


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, key):
        return self.vertices.get(key)

    def addEdge(self, start, end, weight):
        if start not in self.vertices:
            self.addVertex(start)
        if end not in self.vertices:
            self.addVertex(end)
        self.vertices[start].addNeighbor(self.vertices[end], weight)

    def addEdges(self, edgeList):
        for edge in edgeList:
            self.addEdge(edge[0], edge[1], edge[2])

    def getVertices(self):
        return self.vertices.values()

    def printShortestPaths(self, start):
        for vertex in self.vertices.values():
            print(f"Shortest path from {start.getId()} to {vertex.getId()}:")
            self.printPath(start, vertex)
            print(f"Total distance: {vertex.getDistance()}\n")

    def printPath(self, start, end):
        if end == start:
            print(start.getId(), end="")
        elif end.getPred() is None:
            print("No path from {} to {}".format(start.getId(), end.getId()))
        else:
            self.printPath(start, end.getPred())
            print(" ->", end.getId(), end="")


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def buildHeap(self, items):
        self.heap = items
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapifyDown(i)

    def isEmpty(self):
        return len(self.heap) == 0

    def delMin(self):
        if not self.isEmpty():
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            minElement = self.heap.pop()
            self.heapifyDown(0)
            return minElement

    def decreaseKey(self, vertex, newDist):
        for i, (dist, v) in enumerate(self.heap):
            if v == vertex:
                self.heap[i] = (newDist, vertex)
                self.heapifyUp(i)
                break

    def heapifyDown(self, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapifyDown(smallest)

    def heapifyUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i][0] < self.heap[parent][0]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2
