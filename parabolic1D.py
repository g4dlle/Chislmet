import numpy as np
from lu3 import solveLU3
def parabolic1D(k, f, v, l, tEnd, n, tau, sigma):
    """
    Численное решение задачи Дирихле
    для одномерного параболического уравнения.
    Используется двухслойная схема с весом сигма.
    """
    h = 1 / n
    a = np.ones(n+1)
    b = np.zeros(n+1)
    c = np.zeros(n+1)
    d = np.zeros(n+1)
    q = np.zeros(n+1)
    t0 = 0
    y0 = np.zeros(n+1)
    for i in range(1,n):
        x = i*h
        y0[i] = v(x)
        d[i] = k(x - h/2)
    d[n] = k(l - h/2)
    t = []
    y = []
    t.append(t0)
    y.append(y0)
    while t0 < tEnd - tau:
        for i in range(1,n):
            a[i] = 1 / tau + sigma * (d[i+1] + d[i])/h**2
            b[i] = -sigma*d[i+1]/h**2
            c[i] = -sigma*d[i]/h**2
            q[i] = f(i*h, t0 + tau/2) + y0[i]/tau \
            + (1 - sigma) * (d[i+1] * (y0[i+1] - y0[i]) \
                             - d[i] * (y0[i] - y0[i-1]))/h**2
        y0 = solveLU3(a, b, c, q)
        t0 = t0 + tau
        t.append(t0)
        y.append(y0)
    return np.array(t), np.array(y)