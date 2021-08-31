i = [int(x) for x in input().split()]
L = []
i = sorted(i)
L.append(i[0])
i = i[1:]
for x in i:
    if x != L[-1]:
        L.append(x)
print(len(L))
print(L[:10])