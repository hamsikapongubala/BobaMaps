import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.dist = None

    def printSolution(self):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", self.dist[node])

    def SmallWorldNum(self, src, friend):

        self.dijkstra(src)

        for node in range(self.V):
            if node == friend:
                result = self.dist[node]
        print(src, " is ", result, " edges aways from ", friend)


    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, sptSet):

        # Initilaize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if self.dist[v] < min and sptSet[v] == False:
                min = self.dist[v]
                min_index = v

        return min_index

        # Funtion that implements Dijkstra's single source

    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        self.dist = [sys.maxsize] * self.V
        self.dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        self.dist[v] > self.dist[u] + self.graph[u][v]:
                    self.dist[v] = self.dist[u] + self.graph[u][v]

        self.printSolution()

    # Driver program

def main():
    g = Graph(9)
    g.graph = [[0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 1, 0]
        ];

    g.dijkstra(0);

    g.SmallWorldNum(0, 8)

main()
