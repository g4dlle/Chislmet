import numpy as np
from jacobi import jacobi
n = 8
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i < j:
            A[i,j] = (i+1)/(j+1)
        else:
            A[i,j] = (j+1)/(i+1)
print(f'A:\n{A}')
lam, x = jacobi(A)
print('Все собственные значения:\n', lam)