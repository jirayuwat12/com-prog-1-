c = [str(x) for x in input().split(' ')]
mode = input().upper()
for x in mode:
    if x in ['C','S']:
        if x == 'C':
            c = c[len(c)//2:] + c[:len(c)//2]
        else:
            a = c[:len(c)//2]
            b = c[len(c)//2:]
            d = []
            for y in range(len(c)//2):
                d.append(a[y]) 
                d.append(b[y])
            c = d
for x in c:
    print(x,end=' ')