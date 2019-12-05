import queue
import random
import time
import matplotlib.pyplot as plt


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.edges = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistBFS(self, u, v):
        # visited[n] for keeping track
        # of visited node in BFS
        visited = [0] * self.V

        # Initialize distances as 0
        distance = [0] * self.V

        # queue to do BFS.
        Q = queue.Queue()
        distance[u] = 0

        Q.put(u)
        visited[u] = True
        while not Q.empty():
            x = Q.get()

            for i in range(len(self.edges[x])):
                if visited[self.edges[x][i]]:
                    continue

                # update distance for i
                distance[self.edges[x][i]] = distance[x] + 1
                Q.put(self.edges[x][i])
                visited[self.edges[x][i]] = 1
        return distance[v]

    def addEdge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)


# Driver  Code
if __name__ == '__main__':
    g = Graph(9)
    edges = [[] for i in range(9)]
    g.addEdge(0, 1)
    g.addEdge(0, 7)
    g.addEdge(1, 7)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(2, 8)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 7)
    g.addEdge(7, 8)

    print("This is the result:", g.minDistBFS(5, 0))

    # graphing

    # iteration
    set_szs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    timing = []

    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = Graph(9)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.minDistBFS(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # plotting the time complexity for the SmallWorldGraph

    plt.plot(set_szs, timing)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()
