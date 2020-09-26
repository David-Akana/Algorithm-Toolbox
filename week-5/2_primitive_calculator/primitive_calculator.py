# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 3]
    
    sequence = [0] * (n+1)
    sequence[0] = -1
    sequence[1] = 0
    sequence[2] = 1
    sequence[3] = 1
    steps = [n]

    
    for i in range(4, n+1):    
        comp1 = sequence[i-1] + 1
        comp2 = n
        comp3 = n
        
        if i % 2 == 0:
            comp2 = sequence[int(i/2)] + 1
        if i % 3 == 0:
            comp3 = sequence[int(i/3)] + 1

        comp = min(comp1, comp2, comp3)
        
        sequence[i] = comp
    
    num = n
    while num != 1:
        comp1 = sequence[num-1] + 1
        comp2 = n
        comp3 = n
        if num % 2 == 0:
            comp2 = sequence[int(num/2)] + 1
        if num % 3 == 0:
            comp3 = sequence[int(num/3)] + 1
            
        comp = min(comp1, comp2, comp3)
        
        if comp == comp1:
            num -= 1
            steps.append(num)
        elif comp == comp2:
            num = int(num/2)
            steps.append(num)
        elif comp == comp3:
            num = int(num/3)
            steps.append(num)
            
    return reversed(steps)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
