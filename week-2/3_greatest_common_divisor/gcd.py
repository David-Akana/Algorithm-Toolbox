# Uses python3
import sys

def gcd_naive(a, b):
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
        return gcd_naive(num2, remainder)
    
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
