# Uses python3
import sys
def gcd_efficient(a, b):
    if b == 0:
        return a
    if a < b:
        temp = b
        b = a
        a = temp
    reminder = a % b
    return gcd_efficient(b, reminder)

def lcm_efficient(a, b):
    gcd = gcd_efficient(a, b)
    lcm = int(a * b // gcd)
    return lcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_efficient(a, b))


#print(lcm_efficient(226553150, 1023473145))