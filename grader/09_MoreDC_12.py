n = int(input())
SL = []
U = set()
I = set()
for _ in range(n):
    SL.append(set(input().split()))
    U = U.union(SL[-1])
I = set(U)
for x in SL:
    I = I.intersection(x)
print(len(U),'\n',len(I),sep='')