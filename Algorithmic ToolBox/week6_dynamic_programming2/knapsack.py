# Uses python3
import sys

def optimal_weight(W, w):

    items = [0]
    for item in w:
        if item <= W:
            items.append(item)

    dp = [[0 for j in range(len(items))] for i in range(W + 1)]

    for j in range(len(items)):
        for i in range(W + 1):
            prev = dp[i][j - 1]
            curr = dp[i - items[j]][j - 1] + items[j]
            if curr > i:
                dp[i][j] = prev
            else:
                dp[i][j] = max(prev, curr)
    return dp[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
