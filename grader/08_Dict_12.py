n = int(input())
d = {}
for _ in range(n):
    a,b= input().split()
    d[a] = b
    d[b] = a
n = int(input())
for _ in range(n):
    t = input()
    if t in d:
        print(d[t])
    else:
        print("Not found")