d = {}
n= int(input())
for _ in range(n):
    i = input().split()
    d[i[0]+' '+i[1]] = i[2]
    d[i[2]] = i[0]+' '+i[1]
n = int(input())
for _ in range(n):
    i = input()
    if i in d:
        print(i,'-->',d[i])
    else:
        print(i,'-->','Not found')