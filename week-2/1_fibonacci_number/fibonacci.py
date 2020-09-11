# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    
    previous = 0
    current = 1
    
    for i in range(1, n):
        temp = previous
        previous = current
        current += temp
        
    return current

n = int(input())
print(calc_fib(n))
