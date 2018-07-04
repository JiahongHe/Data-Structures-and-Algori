# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n

    m = [[1,1],
         [1,0]]

    for _ in range(2, n+1):
        m00 = m[0][0] % 10
        m10 = m[1][0] % 10
        m = [[m00 + m[0][1] % 10, m00],
             [m10 + m[1][1] % 10, m10]]
    return m[0][1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))

#print(get_fibonacci_last_digit(4))