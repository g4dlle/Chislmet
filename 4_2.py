from numpy import *
from chol import decChol, detChol
n = 4
A = zeros((n,n))
for i in range(n):
    for j in range(n):
        # заполнение матрицы a[i,j] = 1 / (i+j-1)
        A[i,j] = 1/(i+j+1) 
print(f'A:\n{A}')
L = decChol(A)
print(f'L:\n{L}')
det = detChol(A)
print(f'det = {det}')