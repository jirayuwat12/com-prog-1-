from math import *

a = float(input())
b = float(input())
c = float(input())

x = (-b + sqrt(b**2 - 4*a*c) ) / (2*a)
y = (-b - sqrt(b**2 - 4*a*c) ) / (2*a)

print(round(y,3),round(x,3))