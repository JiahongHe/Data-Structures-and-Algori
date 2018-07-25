#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    res = []
    def inOrderTraverse(i):
        if tree[i][1] != -1:
            inOrderTraverse(tree[i][1])
        res.append(tree[i][0])
        if tree[i][2] != -1:
            inOrderTraverse(tree[i][2])
    inOrderTraverse(0)
    for i in range(len(res) - 1):
        if res[i] > res[i + 1]:
            return False
    return True

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if nodes == 0:
        print("CORRECT")
    elif IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
