# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minMax(i, j, m, M, op):
    min_num = 1000000
    max_num = -1000000

    for k in range (i, j):
        a = evalt(M[i, k], M[k+1, j], op[k])
        b = evalt(M[i, k], m[k+1, j], op[k])
        c = evalt(m[i, k], M[k+1, j], op[k])
        d = evalt(m[i, k], m[k+1, j], op[k])
        max_num =   max(max_num, a, b, c, d)
        min_num =   min(min_num, a, b, c, d)
    
    return min_num, max_num


def get_maximum_value(dataset):
    op = dataset[1::2]
    d =  dataset[0::2]
    len_d = len(d)
    
    m = {}
    M = {}

    for i in range(len_d):
        m[i, i] = int(d[i])
        M[i, i] = int(d[i])

    for q in range(1, len_d):
        for i in range(len_d - q):
            j = i + q
            m[i, j], M[i, j] = minMax(i, j, m, M, op)

    return M[0, len_d - 1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
