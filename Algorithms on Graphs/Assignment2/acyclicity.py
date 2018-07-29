#Uses python3

import sys

class Graph:
    def __init__(self, adj_):
        self.adj = adj_
        self.visited = []
        self.flag = False

    def DFS(self, i):
        if self.flag:
            return
        self.visited[i] = 0
        for v in self.adj[i]:
            if self.visited[v] == -1:
                self.DFS(v)
                self.visited[v] = 1;
            if (self.visited[v] == 0):
                self.flag = True

    def acyclic(self):
        for i in range(len(self.adj)):
            self.visited = [-1 for _ in range(len(self.adj))]
            self.DFS(i)
            if self.flag:
                return 1
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    g = Graph(adj)
    print(g.acyclic())
