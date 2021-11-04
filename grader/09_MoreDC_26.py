n = int(input())
D = dict()
for _ in range(n):
    k,name = input().split(': ')
    D[k] = set(name.split(', '))
t = input().strip()
S = set()
for x in D:
    if x == t:
        continue
    for y in D[x]:
        if y in D[t]:
            S.add(x)
if len(S) == 0:
    print("Not Found")
else:
    for x in S:
        print(x)