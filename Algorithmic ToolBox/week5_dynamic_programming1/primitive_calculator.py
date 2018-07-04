# Uses python3
import sys

def optimal_sequence(n):
    table = [None] * (n + 1)
    table[1] = [1]
    for i in range(1, n):
        if table[i] is None:
            continue
        if i * 3 <= n and (table[i * 3] is None or len(table[i * 3]) > len(table[i]) + 1):
            table[i * 3] = table[i] + [i * 3]
        if i * 2 <= n and (table[i * 2] is None or len(table[i * 2]) > len(table[i]) + 1):
            table[i * 2] = table[i] + [i * 2]
        if i + 1 <= n and (table[i + 1] is None or len(table[i + 1]) > len(table[i]) + 1):
            table[i + 1] = table[i] + [i + 1]
    return table[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
