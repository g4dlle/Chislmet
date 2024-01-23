from numpy import *
from cg import cg
n = 4
A = zeros((n,n))
for i in range(n):
    for j in range(n):
        # заполнение матрицы Гилберта
        A[i,j] = 1/(i+j+1)
print(f'A:\n{A}')
f = ones(n)
for i in range(n):
    f[i] = 0
    for j in range(n):
        # Заполнение правой части
        f[i] = f[i] + A[i,j]
print(f'f:\n{f}')
x, iter = cg(A, f)
print(f'iter = {iter}\nx:\n{x}')