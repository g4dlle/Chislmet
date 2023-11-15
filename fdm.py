import numpy as np
from lu3 import solveLU3
def fdm(v, f, mu1, mu2, a, b, n, p):
    """
    Finite defference method for solving the Dirichlet problem
    for the convection-diffusion equation.
    When p = 0 we use the scheme with upwind
    difference approximation,
    when p = 1 - central-difference approximation.
    """
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    a = np.ones(n+1)
    b = np.zeros(n+1)
    c = np.zeros(n+1)
    r = np.zeros(n+1)
    if p == 0:
        for i in range(1, n):
            vp = max(0, v(x[i]))
            vm = min(0, v(x[i]))
            a[i] = 2 + (vp - vm)*h
            b[i] = -1 + h*vm
            c[i] = -1 -h*vp
            r[i] = f(x[i])*h**2
    else:
        for i in range(1, n):
            a[i] = 2
            b[i] = -1 + h * v(x[i]) / 2
            c[i] = -1 - h * v(x[i]) / 2
            r[i] = f(x[i])*h**2
    r[0] = mu1
    r[n] = mu2
    y = solveLU3(a, b, c, r)
    return x, y