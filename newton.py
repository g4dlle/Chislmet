from numpy import *
from lu import solveLU
def jacobian(f, x):
    """
    Вычисление якобиана методом конечных разностей
    """
    h = 1e-4
    n = len(x)
    Jac = zeros((n,n))
    f0 = f(x)
    for i in range(n):
        tt = x[i]
        x[i] = tt + h
        f1 = f(x)
        x[i] = tt
        Jac[:,i] = (f1 - f0) / h
    return Jac, f0
def newton(f, x, tol = 1e-9):
    """
    Решает систему уравнений f(x) = 0 методом Ньютона,
    используя {x} в качестве начального предположения
    Решает линейную систему Ax = b по модулю lu
    Возвращает решение и количество итераций
    """
    iterMax = 50
    for i in range(iterMax):
        Jac, f0 = jacobian(f,x)
        if sqrt(dot(f0,f0) / len(x)) < tol:
            return x, i
        dx = solveLU(Jac, f0)
        x = x - dx
    print('Слишком много итераций для метода Ньютона')