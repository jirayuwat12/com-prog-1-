name1,m1,d1,y1 = [str(x) for x in input().split(' ')]
name2,m2,d2,y2 = [str(x) for x in input().split(' ')]
d1 = d1[:-1]
d2 = d2[:-1]
dict = {
    'January':1,
    'February':2,
    'March':3,
    'April':4,
    'May':5,
    'June':6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'December':12,
}
y1 = int(y1)
y2 = int(y2)
m1 = dict[m1]
m2 = dict[m2]
d1 = int(d1)
d2 = int(d2)
if y1 < y2:
    print(name1)
elif y1 > y2:
    print(name2)
else:
    if m1 < m2 : 
        print(name1)
    elif m1 > m2:
        print(name2)
    else:
        if d1 < d2:
            print(name1)
        elif d1 > d2:
            print(name2)
        else:
            print(name1,name2)