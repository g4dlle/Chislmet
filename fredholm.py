import numpy as np
from lu import solveLU
def fredholm(k, f, a, b, n):
    """
    Решение интегрального уравнения Фредгольма второго рода.
    k(x,s) - ядро интегрального уравнения,
    f(x) - правая часть, 0 < x, s < b.
    Метод с квадратурной формулой трапеции.
    """
    h = (b - a) / n
    A = np.identity(n+1)
    r = np.zeros((n+1))
    for i in range(n+1):
        x = a + i*h
        A[i,0] = A[i,0] - k(x,a)*h/2
        for j in range(1,n):
            s = a + j*h
            A[i,j] = A[i,j] - k(x,s)*h
        A[i,n] = A[i,n] - k(x,b)*h/2
        r[i] = f(x)
    y = solveLU(A,r)
    return y