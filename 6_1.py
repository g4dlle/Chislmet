from numpy import *
from invIter import invIter
print('n собственное значение')
for n in range(2, 11):
    A= zeros((n, n))
    for i in range(n):
        for j in range(n):
            # Заполнение матрицы Гилберта
            A[i,j] = 1/(i+j+1)
    lam, x = invIter(A)
    print(n, lam)