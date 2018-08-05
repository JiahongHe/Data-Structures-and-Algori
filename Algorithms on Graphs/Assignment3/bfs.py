#Uses python3

import sys
import queue

class Graph:
    def __init__(self, adj_):
        self.adj = adj_
        self.queue = []
        self.dist = [ -1 for _ in range(len(self.adj))]
        self.prev = [ None for _ in range(len(self.adj))]

    def BFS(self, s):
        self.dist[s] = 0
        for v in self.adj[s]:
            if self.dist[v] == -1:
                self.prev[v] = s
                self.dist[v] = 1
                self.queue.append(v)
        while len(self.queue) > 0:
            new_queue = []
            while len(self.queue) > 0:
                m = self.queue.pop(0)
                for v in self.adj[m]:
                    if self.dist[v] == -1:
                        self.prev[v] = m
                        self.dist[v] = self.dist[m] + 1
                        new_queue.append(v)
            self.queue = new_queue

    def distance(self, s, t):
        self.BFS(s)
        return self.dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1, 2, 4]
    #data = [5, 4, 5, 2, 1, 3, 3, 4, 1, 4, 3, 5]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    g = Graph(adj)
    print(g.distance(s, t))
