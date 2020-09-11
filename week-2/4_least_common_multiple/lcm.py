# Uses python3
import sys

def gcd(a, b):
    if a > b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a
    
    remainder = num1 % num2
    
    if remainder == 0:
        return num2
    else:
        return gcd(num2, remainder)
    
def lcm_naive(a, b):
    num_gcd = gcd(a, b)

    return int((a*b)/num_gcd)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

