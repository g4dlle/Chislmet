from numpy import *
from seidel import seidel
n = 10
al = 0.5
A = zeros((n,n))
for i in range(n):
    A[i,i] = 2
    if i > 0:
        A[i,i-1] = -1 + al
    if i < n-1:
        A[i,i+1] = -1 - al
print(f'A:\n{A}')
f = zeros(n)
f[0] = 1 - al
f[n-1] = 1 + al 
print(f'f:\n{f}')
x, iter = seidel(A,f)
print(f'iter = {iter}\nx:\n{x}')