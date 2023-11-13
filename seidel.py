from numpy import *
def seidel(A, f, tol = 1e-9):
    """
    Solve the linear system Ax = b by Seidel method
    """
    n = len(f)
    x = zeros(n)
    r = copy(f)
    # the maximum number of iterations is 10000
    for k in range(1, 10000):
        for i in range(n):
            x[i] = x[i] +(f[i] - dot(A[i,0:n], x[0:n])) / A[i,i]
        for i in  range(n):
            r[i] = f[i] - dot(A[i,0:n], x[0:n])
        if dot(r,r) < tol**2: return x, k
    print(f'Seidel method failed to converge:\nafter 10000 iteration residual = {sqrt(dot(r,r))}')
    return x, k