L = []
n = int(input())
c = 0
for x in range(n):
    i = int(input())
    if c==0:
        L.append(i)
        c^=1
    else:
        L.insert(0,i)
        c^=1
i = str(input())
i = i.split()
for x in i:
    x = int(x)
    if c==0:
        L.append(x)
        c^=1
    else:
        L.insert(0,x)
        c^=1
i = int(input())
while i != -1:
    if c==0:
        L.append(i)
        c^=1
    else:
        L.insert(0,i)
        c^=1
    i = int(input())
print(L)