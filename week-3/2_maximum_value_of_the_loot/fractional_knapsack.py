# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    units = []
    for i in range(len(weights)):
        units.append((values[i]/weights[i], i))
        
    units.sort(key=lambda x: x[0], reverse=True)
    n = len(units)
    
    opt_value = 0
    i = 0
    while capacity != 0 and i < n:
        item = units[i]
        
        if weights[item[1]] > capacity:
            opt_value += capacity * item[0]
            capacity = 0
            i += 1
        elif weights[item[1]] == capacity:
            capacity = 0
            opt_value += values[item[1]]
            i += 1
        else:
            capacity -= weights[item[1]]
            opt_value += values[item[1]]
            i += 1
            
    return opt_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
