inp = input()
d,m,y = [int(x)for x in inp.split(' ')]
d += 15
if m in [1,3,5,7,8,10,12] and d>31:
    m+=1
    d-=31
elif m==2 and d>28:
    if ((y-543) %400 == 0 or ((y-543)%4==0 and (y-543)%100 !=0)):
        if d>29:
            m+=1
            d-=29
    elif d>28:
        m+=1
        d-=28
elif d>30:
    m+=1
    d-=30

if m>12:
    m=1
    y+=1
print(d,m,y,sep='/')