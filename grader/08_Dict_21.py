t = input()
d = {}
for x in t:
    if ord('A') <= ord(x) <= ord('z'):
        x = x.lower()
        if x in d:
            d[x] +=1
        else:
            d[x] = 1
l = []
for x in d:
    l.append([-d[x],x])
l = sorted(l)
for x in l:
    print(x[1],'->',-x[0])