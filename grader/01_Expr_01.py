from math import *

n = float(input())

l = sqrt(2*pi) * n**(n+(1/(2)))*e**(-n+1/(12*n+1))
u = sqrt(2*pi) * n**(n+(1/(2)))*e**(-n+1/(12*n))

print(l,u,sep='\n')