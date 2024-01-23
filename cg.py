from numpy import *
def cg(A, f, tol = 1e-9):
    """
    Решите линейную систему Ax = b методом сопряженного градиента
    Возвращает приближенное решение и число итераций
    """
    n = len(f)
    x = zeros(n)
    r = copy(f)
    for i in range(n):
        r[i] = dot(A[i,0:n], x[0:n]) - f[i]
    s = copy(r)
    As = zeros(n)
    for k in range(n):
        for i in range(n):
            As[i] = dot(A[i,0:n], s[0:n])
        alpha = dot(r,r) / dot(s,As)
        x = x - alpha*s
        for i in range(n):
            r[i] = dot(A[i,0:n], x[0:n]) - f[i]
        if dot(r,r) < tol**2:
            break
        else:
            beta = -dot(r, As) / dot(s, As)
            s = r + beta*s
    return x, k