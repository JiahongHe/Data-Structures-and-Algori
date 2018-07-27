#Uses python3

import sys

class Reachability:
    def __init__ (self, adj_):
        self.adj = adj_
        self.reachable = []
    def DFS(self, i):
        self.reachable.append(i)
        for v in adj[i]:
            if v in self.reachable:
                continue
            self.DFS(v)

    def reach(self, x, y):
        self.reachable = []
        self.DFS(x)
        if y in self.reachable:
            return 1;
        return 0



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    reach = Reachability(adj)
    print(reach.reach(x, y))
