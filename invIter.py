from numpy import *
from lu import decLU, solveLU
def invIter(A, tol = 1.0e-6):
    '''
    Метод обратной мощности.
    Возвращает минимальное собственное значение и
    соответствующий собственный вектор.
    '''
    n = len(A)
    iterMax = 100
    x = random.rand(n)
    xNorn = sqrt(dot(x, x))
    x = x / xNorn
    for i in range(0, iterMax):
        x1 = x.copy()
        x = solveLU(A, x)
        xNorn = sqrt(dot(x, x))
        x= x / xNorn
        if sqrt(dot(x1-x, x1-x)) < tol:
            return 1 / xNorn, x
    print('Метод не сходится (100 итераций)')