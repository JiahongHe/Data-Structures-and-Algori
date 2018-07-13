# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash_func(s):
    _multiplier = 263
    _prime = 1000000007
    ans = 0
    for c in reversed(s):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans

def get_occurrences(pattern, text):
    len_p = len(pattern)
    hash_p = hash_func(pattern)
    ans = []
    for i in range(0, len(text) - len_p + 1):
        sub_t = text[i: i + len_p]
        hash_t = hash_func(sub_t)
        if (hash_p == hash_t):
            if (sub_t == pattern):
                ans.append(i)
    return ans
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

