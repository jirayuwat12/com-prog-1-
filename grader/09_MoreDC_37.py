n = int(input())
number_of_dept = dict()
for _ in range(n):
    nm,nmb = input().split()
    number_of_dept[nm] = int(nmb)

n = int(input())
ret = []
data = []
for _ in range(n):
    inp = input().split()
    inp[1] = float(inp[1])
    inp[0],inp[1] = inp[1],inp[0]
    data.append(inp)
data = sorted(data)[::-1]
for student in data:
    ind = 2
    while True:
        if number_of_dept[student[ind]] > 0 :
            ret.append([student[1],student[ind]])
            number_of_dept[student[ind]] -= 1
            break
        ind +=1
ret = sorted(ret)
for x in ret:
    print(x[0],x[1])