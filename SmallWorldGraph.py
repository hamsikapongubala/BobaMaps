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
    g = Graph(26)
    edges = [[] for i in range(26)]

    g.addEdge(1, 4)
    g.addEdge(1, 9)
    g.addEdge(1, 20)
    g.addEdge(2, 14)
    g.addEdge(2, 21)
    g.addEdge(3, 18)
    g.addEdge(3, 7)
    g.addEdge(4, 1)
    g.addEdge(4, 6)
    g.addEdge(5, 24)
    g.addEdge(5, 10)
    g.addEdge(6, 16)
    g.addEdge(6, 17)
    g.addEdge(6, 18)
    g.addEdge(7, 15)
    g.addEdge(7, 14)
    g.addEdge(8, 20)
    g.addEdge(8, 21)
    g.addEdge(8, 3)
    g.addEdge(8, 15)
    g.addEdge(10, 14)
    g.addEdge(10, 25)
    g.addEdge(10, 21)
    g.addEdge(12, 24)
    g.addEdge(12, 18)
    g.addEdge(12, 16)
    g.addEdge(13, 17)
    g.addEdge(13, 19)
    g.addEdge(15, 19)
    g.addEdge(15, 24)
    g.addEdge(17, 19)
    g.addEdge(18, 22)
    g.addEdge(20, 23)
    g.addEdge(20, 1)
    g.addEdge(21, 25)

    print("This is the result:", g.minDistBFS(12, 13))

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
