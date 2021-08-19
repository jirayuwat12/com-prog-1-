x = str(input())
m = 1
m1=999999999999999999999999
M1=-999999999999999999999999
m2=999999999999999999999999
M2=-999999999999999999999999
while x != 'Zig-Zag' and x != 'Zag-Zig':
    a,b = [int(i) for i in x.split(' ')]
    if m==1:
        m1 = min(m1,a)
        M1 = max(M1,a)
        m2 = min(m2,b)
        M2 = max(M2,b)
    else:
        m1 = min(m1,b)
        M1 = max(M1,b)
        m2 = min(m2,a)
        M2 = max(M2,a)
    m*=-1
    x = str(input())
if x=='Zig-Zag':
    print(m1,M2)
else:
    print(m2,M1)