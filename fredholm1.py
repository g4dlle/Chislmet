import numpy as np
from cg import cg
def fredholm1(k, f, a, b, n, tol = 1e-9):
    """
    Решение интегрального уравнения Фредгольма первого рода.
    k(x,s) - ядро интегрального уравнения,
    f(x) - правая часть, 0 < x, s < b.
    Метод итераций CG с
    формулой прямоугольной квадратуры.
    """
    h = (b - a) / n
    A = np.zeros((n,n))
    r = np.zeros((n))
    for i in range(n):
        x = a + h / 2 + i * h
        r[i] = f(x)
        for j in range(n):
            s = a + h / 2 + j * h
            A[i,j] = k(x,s)*h
    # Симметризация
    B = np.copy(A)
    rr = np.copy(r)
    for i in range(n):
        r[i] = np.dot(B[i,0:n], rr[0:n])
        for j in range(n):
            A[i,j] = np.dot(B[i,0:n], B[0:n,j])
    y, iter = cg(A, r, tol = tol)
    return y, iter