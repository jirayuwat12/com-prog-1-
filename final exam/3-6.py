def pattern1(N):
    ret = []
    h = 1
    for i in range(N):
        ret.append([])
        for j in range(N):
            ret[i].append(0)
            if (N-j) <= i+1 :
                ret[i][j] = h
                h+=1
    return ret

def pattern2(N):
    ret = []
    for i in range(N):
        ret.append([])
        for j in range(N):
            ret[i].append(0)
    h = 1
    for i in range(N):
        for j in range(N):
            if j < N-i:
                ret[j][i] = h
                h+=1
    return ret
