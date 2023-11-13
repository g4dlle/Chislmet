from numpy import *
def golden(f, a, b, tol = 1e-10):
    """
    Gloden section method for determining x
    that minimizes the scalar function f(x).
    The minimum must be bracketed in(a,b).
    """
    c1 = (sqrt(5.) - 1.) / 2.
    c2 = 1. - c1
    nIt = int(ceil(log(tol / abs(b-a)) / log(c1)))
    # First step
    x1 = c1*a + c2*b
    x2 = c2*a + c1*b
    f1 = f(x1)
    f2 = f(x2)
    # Iteration
    for i in range(nIt):
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = c2*a + c1*b
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = c1*a + c2*b
            f1 = f(x1)
    if f1 < f2:
        return x1, f1
    else:
        return x2, f2
