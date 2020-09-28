# Uses python3
import sys

def optimal_weight(W, w):
    col = len(w) + 1
    
    value = {}
    
    for i in range(W+1):
        value[i, 0] = 0
        
    for j in range(col):
        value[0, j] = 0
    
    for j in range(1, col):
        for i in range(1, W+1):
            value[i, j] = value[i, j-1]
            if w[j-1] <= i:
                val = value[i-w[j-1], j-1] + w[j-1]
                if value[i, j] < val:
                    value[i, j] = val
                    
    return value[W, col-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
