#Uses python3

import sys

class Graph:

    def __init__(self, adj_):
        self.adj = adj_
        self.visited = []
        self.connected = []
        self.reachable = []

    def DFS(self, i):
        self.reachable.append(i)
        self.visited.append(i)
        for v in adj[i]:
            if v not in self.visited:
                self.DFS(v)

    def all_connected(self, i):
        self.reachable = []
        self.DFS(i)
        return self.reachable

    def all_components(self):
        self.connected = []
        self.visited = []
        for i in range(len(self.adj)):
            if i not in self.visited:
                self.connected.append(self.all_connected(i))
        print(self.connected)

def number_of_components(adj):
    result = 0
    #write your code here
    return result

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    data = [4, 2, 1, 2, 3, 2]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    g = Graph(adj)
    g.all_components()
    print(len(g.connected))
