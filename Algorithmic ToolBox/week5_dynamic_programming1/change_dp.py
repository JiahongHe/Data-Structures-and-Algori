# Uses python3

# denominations: 1, 3, 4
import sys

dict = {0:0,
        1:1,
        2:2,
        3:1,
        4:1
        }

def get_change(m):
    if m in dict.keys():
        return dict[m]
    for i in range(5, m + 1):
        change_1 = get_change(i - 1) + 1
        change_3 = get_change(i - 3) + 1
        change_4 = get_change(i - 4) + 1
        change = min(change_1, change_3, change_4)
        dict[i] = change

    return dict[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    #print(get_change(10))

