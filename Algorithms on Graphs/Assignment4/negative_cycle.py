#Uses python3

import sys

class Graph:
    def __init__(self, adj_, cost_):
        self.adj = adj_
        self.cost = cost_
        self.distance = [float('inf') for _ in range(len(adj_))]
        self.prev = [-1 for _ in range(len(adj_))]

    def relax(self, u, v):
        if self.distance[v] > self.distance[u] + self.cost[u][self.adj[u].index(v)]:
            self.distance[v] = self.distance[u] + self.cost[u][self.adj[u].index(v)]
            self.prev[v] = u



    def Bellman_Ford(self, s):
        self.distance[s] = 0
        self.prev[s] = None

        for i in range(len(self.adj) - 1):
            for i in range(len(self.adj)):
                for v in self.adj[i]:
                    self.relax(i, v)

        for i in range(len(self.adj)):
            for v in self.adj[i]:
                if self.distance[v] > self.distance[i] + self.cost[i][self.adj[i].index(v)]:
                    self.distance[v] = self.distance[i] + self.cost[i][self.adj[i].index(v)]
                    self.prev[v] = i
                    return 1
        return 0

    def negative_cycle(self):
        flag = self.Bellman_Ford(0)
        return flag

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    g = Graph(adj, cost)
    print(g.negative_cycle())
