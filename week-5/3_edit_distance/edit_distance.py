# Uses python3
def edit_distance(s, t):
    n = len(s) + 1
    m = len(t) + 1
    
    distance = {}
    
    for i in range(n):
        distance[i, 0] = i
        
    for j in range(m):
        distance[0, j] = j
        
    for j in range(1, m):
        for i in range(1, n):
            insertion = distance[i, j-1] + 1
            deletion = distance[i-1, j] + 1
            match = distance[i-1, j-1]
            mismatch = distance[i-1, j-1] + 1
            
            if s[i-1] == t[j-1]:
                distance[i, j] = min(insertion, deletion, match)
            else:
                distance[i, j] = min(insertion, deletion, mismatch)
        
    return distance[n-1, m-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
