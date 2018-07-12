# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))

def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    ans = max(lines)
    if realDestination == realSource:
        return ans
    if rank[realDestination] < rank[realSource]:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
    else:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        if rank[realSource] == rank[realDestination]:
            rank[realDestination] += 1
    ans = max(lines)
    return ans

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    ans = merge(destination - 1, source - 1)
    print(ans)
    
