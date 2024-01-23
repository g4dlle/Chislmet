from math import *
from gauss import gauss
def f(x):
    return -log(x) / (1 - x)
a = 0
b = 1
for n in range(2,9):
    I = gauss(f, a, b, n)
    print('n =', n, 'Integral =', I)
Iexact = pi**2 / 6
print('Точное значение = ', Iexact)