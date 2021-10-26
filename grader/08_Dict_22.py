n = int(input())
d ={}
dd  = {}
for _ in range(n):
    a,n = input().split()
    n = int(n)
    d[a] = n
sum  = 0
n = int(input())
for _ in range(n):
    n,m = input().split()
    
    m = int(m)
    if n in d:
        sum += d[n]*m
        if n in dd:
            dd[n] += d[n]*m
        else:
            dd[n] = d[n]*m
if sum == 0:
    print("No ice cream sales")
else:
    print("Total ice cream sales: {0:.1f}".format(sum))
    l = []
    for x in dd:
        l.append([-dd[x],x])
    l = sorted(l)
    M = l[0][0]
    ind =0
    print("Top sales: ",end = '')
    while l[ind][0] == M:
        if ind != 0:
            print(', ',end ='')
        print(l[ind][1],end='')
        ind +=1
        if ind == len(l):
            break