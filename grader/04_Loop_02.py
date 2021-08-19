import math

a = float(input())
l = 0 
u = a
x = (u)/2
while abs(10**x - a) > max(a,10**x)*10**-10:
    if 10**x > a:
        u = x
    else:
        l = x
    x = l + (u-l)/2

print(format(x,".6f"))