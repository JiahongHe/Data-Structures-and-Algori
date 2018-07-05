# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_min_max(i, j, M, m, ops):
    Max = float("-inf")
    Min = float("inf")
    for k in range(i, j):
        m1 = evalt(M[i][k], M[k + 1][j], ops[k])
        m2 = evalt(M[i][k], m[k + 1][j], ops[k])
        m3 = evalt(m[i][k], M[k + 1][j], ops[k])
        m4 = evalt(m[i][k], m[k + 1][j], ops[k])
        Max = max(Max, m1, m2, m3, m4)
        Min = min(Min, m1, m2, m3, m4)
    return (Max, Min)

def get_maximum_value(dataset):
    nums = [int(dataset[i]) for i in range(0, len(dataset) + 1, 2)]
    n = len(nums)
    ops = [dataset[i] for i in range(1, len(dataset), 2)]
    M = [[0 for _ in range(n)] for _ in range(n)]
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] = nums[i]
        m[i][i] = nums[i]

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            M[i][j], m[i][j] = get_min_max(i, j, M, m, ops)
    return M[0][-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
