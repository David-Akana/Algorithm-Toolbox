# Uses python3
import sys

def get_change(m):
    if m < 5:
        return m
    
    elif m >= 5 and m < 10:
        return ((m % 5) + 1)
    
    elif m >= 10:
        tens = int(m/10)
        ones = m % 10
        if ones >= 5:
            fives_and_ones = (ones % 5) + 1
            return (tens + fives_and_ones)
        else:
            return (tens + ones)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
