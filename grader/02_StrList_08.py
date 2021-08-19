import math

a,b,c = [str(x) for x in input().split(',')]

# print(a,b,c)
if b == '':
    s = int(c)
    h = int('9'*len(c))
    s += int(a)*h
    gcd=  math.gcd(s,h)
    print(s//gcd,h//gcd,sep='/')
else:
    print(s//gcd,h//gcd,sep='/')