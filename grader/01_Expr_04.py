from math import *

m = float(input())
h = float(input())

print(sqrt(m*h)/60)
print(0.024265 * m**(0.5378) * h**(0.3964))
print(0.0333 * m**(0.6157 - 0.0188*log10(m))*h**0.3)