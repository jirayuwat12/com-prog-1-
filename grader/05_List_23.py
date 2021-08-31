n = int(input())
dictt = {}
for _ in range(1,n+1):
    x,y = [float(x) for x in input().split()]
    dictt[((x**2+y**2)**(1/2))] = (_,(x,y))
i = 0
for x in sorted(dictt.keys()):
    i+=1
    if i == 3:
        print("#{0}: {1}".format(dictt[x][0],dictt[x][1]))
    else:
        continue