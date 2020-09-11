# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    curr_refill = 0
    
    
    stops = [0] + stops + [distance]
    n = len(stops) - 2
    
    while curr_refill <= n:
        last_refill = curr_refill
        while curr_refill <= n and stops[curr_refill + 1] - stops[last_refill] <= tank:
            curr_refill = curr_refill + 1
        
        if curr_refill == last_refill:
            return -1
        
        if curr_refill <= n:
            num_refills = num_refills + 1
            
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
