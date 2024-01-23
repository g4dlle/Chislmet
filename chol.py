from numpy import *
def decChol(A):
    """
    Возвращает разложение Холецкого для матрицы A
    (вычисляется нижняя треугольная матрица L)
    """
    n = len(A)
    L = copy(A)
    for j in range(n):
        try:
            L[j,j] = sqrt(L[j,j] - dot(L[j,0:j], L[j,0:j]))
        except ValueError:
            print('Matrix is not positive definite')
        for i in range(j+1,n):
            L[i,j] = (L[i,j]- dot(L[i,0:j], L[j,0:j])) / L[j,j]
    for j in range(1,n):
        L[0:j,j] = 0
    return L
def detChol(A):
    """
    Возвращает определитель матрицы A
    """
    n = len(A)
    L = decChol(A)
    det = 1
    for i in range(n):
        det *= L[i,i]**2
    return det