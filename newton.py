from numpy import *
from lu import solveLU
def jacobian(f, x):
    """
    Calculation of the Jacobian using finite differences
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
    Solves the system equations f(x) = 0 by
    the Newton method using {x} as the initial guess
    Solve th elinear system Ax = b by lu module
    """
    iterMax = 50
    for i in range(iterMax):
        Jac, f0 = jacobian(f,x)
        if sqrt(dot(f0,f0) / len(x)) < tol:
            return x, i
        dx = solveLU(Jac, f0)
        x = x - dx
    print('Too many iteratios for the Newton method')