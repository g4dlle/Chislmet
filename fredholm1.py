import numpy as np
from cg import cg
def fredholm1(k, f, a, b, n, tol = 1e-9):
    """
    Solution Fredholm integral equation of the first kind.
    k(x,s) is the kernel of the integral equation,
    f(x) is the right part, 0 < x, s < b.
    CG iteratibe method with
    rectangle quadrature formula.
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
    # Symmetrization
    B = np.copy(A)
    rr = np.copy(r)
    for i in range(n):
        r[i] = np.dot(B[i,0:n], rr[0:n])
        for j in range(n):
            A[i,j] = np.dot(B[i,0:n], B[0:n,j])
    y, iter = cg(A, r, tol = tol)
    return y, iter