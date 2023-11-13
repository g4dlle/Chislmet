from numpy import *
def decLU3(a, b, c):
    """
    Input of diagonal matrix A:
        a[i] = A[i,i],
        b[i] = A[i,i+1],
        c[i] = A[i,i-1]
    Returns the decomposition LU for tridiagonal matrix:
        d[i] = L[i,i]
        u[i] = U[i,i+1]
        l[i] = L[i,i-1]
    """
    n = len(a)
    d = copy(a)
    u = copy(b)
    l = copy(c)
    for i in range(1,n):
        al = l[i] / d[i-1]
        d[i] = d[i] -al*u[i-1]
        l[i] = al
    return d, u, l
def solveLU3(a, b, c, f):
    """
    Solve the linear system Ax = b with tridiagonal matrix:
        a[i] = A[i,i],
        b[i] = A[i,i+1],
        c[i] = A[i,i-1]
    """
    n = len(a)
    # LU decomposition
    d, u, l = decLU3(a, b, c)
    x = copy(f)
    # forward substitution process
    for i in range(1,n):
        x[i] = x[i] - l[i]*x[i-1]
    # back substitution process
    x[n-1] = x[n-1] / d[n-1]
    for i in range(n-2,-1,-1):
        x[i] = (x[i] - u[i]*x[i+1]) / d[i]
    return x