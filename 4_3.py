from numpy import *
from lu3 import decLU3, solveLU3
n = 50
h = 1 / (n + 1)
a = 2*ones(n)
b = -ones(n)
c = -ones(n)
f = h**2*2*ones(n, dtype=float)
# solution
x = solveLU3(a, b, c, f)
# test function
y = zeros(n)
# LU decomposition
d, u, l = decLU3(a, b, c)
er = 0
det = 1
for i in range(n):
    y[i] = (i + 1) * h * (1 - (i + 1) * h)
    er = er + (y[i] - x[i])**2*h
    det = det * d[i]
    det = round(det, 10)
er = sqrt(er)
print(f'error = {er}')
print(f'determinant calculated = {det}\nexact = {n+1}')