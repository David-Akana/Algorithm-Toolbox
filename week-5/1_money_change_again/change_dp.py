# Uses python3
import sys

def get_change(m):
    min_num_coins = [0] * (m+1)
    coins = [1, 3, 4]
    
    for i in range(1, (m+1)):
        min_num_coins[i] = m
        for coin in coins:
            if coin <= i:
                num_coins = min_num_coins[i-coin] + 1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins
    
    return min_num_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
