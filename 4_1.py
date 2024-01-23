from numpy import *
from lu import decLU, solveLU
n = 10
A = -ones((n,n))
for i in range(0,n):
    # заполнение матрицы
    A[i,i] = 1
    A[n-1,i] = 1
    if i < n-1:
        A[i+1:n-1,i] = 0
print(f'A:\n{A}')
LU = decLU(A)
print(f'LU:\n{LU}')
f = ones(n)
print(f'b:\n{f}')
x = solveLU(A, f)
print(f'x:\n{x}')