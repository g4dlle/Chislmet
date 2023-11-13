from math import *
from trap import trap
def f(x):
    return 2*exp(-x**2) / sqrt(pi)
a = 0
b = 1
for n in range(5, 11):
    er = 10**(-n)
    Inew = trap(f, a, b, tol=er)
    print(f'tol = {er}\nIntegral = {Inew}')