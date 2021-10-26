def factor(N):
    dic ={}
    x = 2
    while x<= N and N > 0 :
        if N% x ==0:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
            N /= x
        else:
            x+=1
    ret = []
    for x in dic:
        ret += [[x,dic[x]]]
    return ret
# exec(input().strip())
print(factor(2*3*5*7*11*13*17*19))