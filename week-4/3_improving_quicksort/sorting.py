# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    
    c1 = l
    c2 = j
    
    while(c1 < c2):
        if a[c1] == x:
            while(c1 < c2):
                if a[c2] != x:
                    a[c1], a[c2] = a[c2], a[c1]
                    c2 -= 1
                    break
                else:
                    c2 -= 1
        if c1 != c2:
            c1 += 1
    
    if a[c1] == x:
        k = c1
    else: 
        k = c1 + 1
    
    return k, j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
