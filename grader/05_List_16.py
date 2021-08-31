n = int(input())
L = [n]
while n!=1:
    if not n&1:
        n //=2
    else:
        n = 3*n+1
    L.append(n)

if len(L) >15:
    print(L[-15],end='')
    for x in L[-14:]:
        print('->',x,sep='',end='')
else:
    print(L[0],end='')
    for x in L[1:]:
        print('->',x,sep='',end='')
