d = int(input())
m = int(input())
y = int(input())
ml = [31,28,31,30,31,30,31,31,30,31,30,31]
sum = 0
for x in range(m-1):
    sum += ml[x]
if m>2 :
    if ((y-543) %400 == 0 or ((y-543)%4==0 and (y-543)%100 !=0)):
        sum+=1

print(sum+d)
