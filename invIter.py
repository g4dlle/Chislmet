from numpy import *
from lu import decLU, solveLU
def invIter(A, tol = 1.0e-6):
    '''
    The inverse power method.
    Returns the smallest eigenvalue and
    the corresponding eigenvector.
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
    print('Method did not converge (100 iterations)')