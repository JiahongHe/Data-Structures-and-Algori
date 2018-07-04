# Uses python3

def edit_distance(s, t):
    m = len(s)
    n = len(t)
    matrix = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(m + 1):
        matrix[0][i] = i
    for j in range(n + 1):
        matrix[j][0] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                matrix[j][i] = min(matrix[j - 1][i - 1], matrix[j - 1][i] + 1, matrix[j][i - 1] + 1)
            else:
                matrix[j][i] = min(matrix[j - 1][i - 1] + 1, matrix[j - 1][i] + 1, matrix[j][i - 1] + 1)
    return matrix[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
