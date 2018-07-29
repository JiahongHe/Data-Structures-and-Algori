#Uses python3

import sys

class Graph:

    def __init__(self, adj):
        self.__adj = adj
        self.__visited = []
        self.__topnum = []
        self.__n = len(adj)

    def DFS(self, i):
        self.__visited[i] = 0
        for v in self.__adj[i]:
            if self.__visited[v] == -1:
                self.DFS(v)
        self.__topnum[i] = self.__n
        self.__n -= 1


    def toposort(self):
        self.__topnum = [-1 for _ in range(len(self.__adj))]
        self.__visited = [-1 for _ in range(len(self.__adj))]
        for i in range(len(adj)):
            if self.__visited[i] == -1:
                self.DFS(i)
        order = [-1 for _ in range(len(self.__adj))]
        for num in self.__topnum:
            order[num-1] = self.__topnum.index(num)
        return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 3, 1, 2, 4, 1, 3, 1]
    #data = [5, 7, 2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5, 3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    g = Graph(adj)
    order = g.toposort()
    for x in order:
        print(x + 1, end=' ')

