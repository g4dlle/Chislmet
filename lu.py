from numpy import *
def decLU(A):
    """
    Возвращает LU-разложение для матрицы A
    """
    n = len(A)
    LU = copy(A)
    for j in range(n-1):
        for i in range(j+1,n):
            if LU[i,j] != 0.:
                u = LU[i,j] / LU[j,j]
                LU[i,j+1:n] = LU[i,j+1:n] - u*LU[j,j+1:n]
                LU[i,j] = u
    return LU

def solveLU(A,f):
    """
    Решение линейной системы Ax = b
    """
    n = len(A)
    LU = decLU(A)
    x = copy(f)
    # forward substition process
    for i in range(1,n):
        x[i] = x[i] - dot(LU[i,0:i], x[0:i])
    # back substition process
    for i in range(n-1,-1,-1):
        x[i] = (x[i] - dot(LU[i,i+1:n], x[i+1:n])) / LU[i,i]
    return x