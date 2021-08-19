p = float(input())
k = t = 1
t = (t*(365 - (k-1)))/365
while not 1-t>=p:
    k+=1
    t = (t*(365 - (k-1)))/365
print(k)