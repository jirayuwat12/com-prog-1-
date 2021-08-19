import math

def findU(x):
    u = 1
    while x>0:
        x/=10
        u+=1
    return u 

a = float(input())
l = 0 
u = findU(a)
x = (u)/2
while abs(10**x - a) > max(a,10**x)*10**-10:
    if 10**x > a:
        u = x
    else:
        l = x
    x = l + (u-l)/2

print(format(x,".6f"))
