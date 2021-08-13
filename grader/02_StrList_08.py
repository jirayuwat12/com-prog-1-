import math

a,b,c = input().split(',')
a = int(a)
if b!='':
    b = int(b)
    c = int(c)
    tung = int(str(b)+str(c)) -  int(b)
    harn = int('9'*len(str(c)) + '0'*len(str(b)))
    tung += a * int(harn)

    gcd = math.gcd(tung,harn)

else:
    c = int(c)
    tung = int(str(c))
    harn = int('9'*len(str(c)))
    tung += a * int(harn)

    gcd = math.gcd(tung,harn)

# tung //= gcd
# harn //= gcd
print(tung,harn,sep=" / ")