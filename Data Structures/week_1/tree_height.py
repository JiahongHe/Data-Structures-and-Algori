# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height_original(self):
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

        def path_len(self, node_id):
            parent = self.parent[node_id]
            if parent == -1:
                return 1

            if self.cache[node_id]:
                return self.cache[node_id]

            self.cache[node_id] = 1 + self.path_len(self.parent[node_id])
            return self.cache[node_id]

        def compute_height_new(self):
            return max([self.path_len(i) for i in range(self.n)])

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height_new())

threading.Thread(target=main).start()
