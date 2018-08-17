# python3
import sys

NA = -1


class Node:
    def __init__(self):
        self.next = [NA] * 4

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    node_count = 1
    for pattern in patterns:
        curr_node = 0
        for c in pattern:
            if c not in tree[curr_node].keys():
                tree[curr_node][c] = node_count
                tree[node_count] = {}
                node_count += 1
            curr_node = tree[curr_node][c]
        tree[curr_node] = {"end"}
    return tree

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    print(trie)
    for i in range(len(text)):
        print("i: ", i)
        if text[i] in trie[0]:
            curr_node = trie[0][text[i]]
            j = i + 1
            flag = True
            while j < len(text) - 1:
                if trie[curr_node] == ""

    print(result)
    return []


if __name__ == "__main__":
    #text = sys.stdin.readline().strip()
    #n = int(sys.stdin.readline().strip())
    #patterns = []
    text = "AATCGGGTTCAATCGGGGT"
    n = 2
    patterns = ["ATCG", "GGGT"]
    '''
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
    '''
    ans = solve(text, n, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')
