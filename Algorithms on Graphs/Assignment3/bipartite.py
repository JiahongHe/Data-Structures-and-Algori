#Uses python3

import sys
import queue

class Graph:
    def __init__(self, adj_):
        self.adj = adj_
        self.color = [0 for _ in range(len(adj_))]

    def bipartite(self, s):
        self.color[s] = 1
        que = []
        for v in self.adj[s]:
            self.color[v] = -1
            que.append(v)
        while len(que) > 0:
            new_que = []
            while len(que) > 0:
                m = que.pop(0)
                colr = self.color[m]
                for v in adj[m]:
                    if self.color[v] == 0:
                        self.color[v] = - colr
                        new_que.append(v)
                    if self.color[v] == colr:
                        return 0
            que = new_que
        return 1




if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    data = [5, 4, 5, 2, 4, 2, 3, 4, 1, 4]
    #data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    g = Graph(adj)
    print(g.bipartite(0))
