result =0
i = [int(x) for x in input().split()]
result = i[0] > i[1] + i[-1] > i[-2]
for x in range(1,len(i)-1):
    if i[x-1] < i[x] and i[x+1]<i[x]:
        result+=1
print(result)
