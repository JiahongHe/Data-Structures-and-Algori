#Uses python3

import sys
import queue

class Node:
    def __init__(self, index, distance):
        self.ind = index
        self.dist = distance

    def __gt__(self, other):
        if self.dist > other.dist:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.dist == other.dist:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.dist < other.dist:
            return True
        else:
            return False


class Graph:
    def __init__(self,adj_, cost_):
        self.adj = adj_
        self.cost = cost_
        self.distance = [float("inf") for _ in range(len(self.adj))]
        self.prev = [-1 for _ in range(len(self.adj))]
        self.min_queue = []

    def relax(self, u, v):
        if self.distance[v] > self.distance[u] + self.cost[u][self.adj[u].index(v)]:
            self.distance[v] = self.distance[u] + self.cost[u][self.adj[u].index(v)]
            self.prev[v] = u
            self.min_queue.append(self.make_node(v, self.distance[v]))

    def extract_min(self, queue):
        queue = sorted(queue)
        val = queue[0]
        queue = queue[1:]
        return (val, queue)

    def make_node(self, v, cost):
        return Node(v, cost)

    def dijkstra(self, s):
        self.distance[s] = 0
        self.prev[s] = None

        for v in self.adj[s]:
            self.min_queue.append(self.make_node(v, cost[s][self.adj[s].index(v)]))
            self.relax(s, v)
        while len(self.min_queue) > 0:
            m, self.min_queue = self.extract_min(self.min_queue)
            for v in self.adj[m.ind]:
                self.relax(m.ind, v)

    def Distance(self, s, t):
        self.dijkstra(s)
        if self.distance[t] == float('inf'):
            return -1
        return self.distance[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3]
    #data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4, 4, 1, 5]
    #data = [3, 3, 1, 2,7, 1, 3, 5, 2, 3, 2, 3, 2]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    g = Graph(adj, cost)
    print(g.Distance(s, t))
