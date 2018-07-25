# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        result = []
        def inOrderTraverse(i):
            if self.left[i] != -1:
                inOrderTraverse(self.left[i])
            result.append(self.key[i])
            if self.right[i] != -1:
                inOrderTraverse(self.right[i])
        inOrderTraverse(0)
        return result

    def preOrder(self):
        result = []
        def preOrderTraverse(i):
            result.append(self.key[i])
            if self.left[i] != -1:
                preOrderTraverse(self.left[i])
            if self.right[i] != -1:
                preOrderTraverse(self.right[i])
        preOrderTraverse(0)
        return result

    def postOrder(self):
        result = []
        def postOrderTraverse(i):
            if self.left[i] != -1:
                postOrderTraverse(self.left[i])
            if self.right[i] != -1:
                postOrderTraverse(self.right[i])
            result.append(self.key[i])
        postOrderTraverse(0)
        return result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
