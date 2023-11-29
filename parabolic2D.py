import numpy as np
from lu3 import solveLU3
def parabolic2D(f, v, l1, l2, tEnd, n1, n2, tau, k):
    """
    Numerical Solution of the Dirichlet problem
    for two-demensional parabolic equation.
    Use additive difference scheme of alternating directions.
    """
    h1 = l1 / n1
    h2 = l2 / n2
    a1 = np.ones(n1+1)
    b1 = np.zeros(n1+1)
    c1 = np.zeros(n1+1)
    q1 = np.zeros(n1+1)
    a2 = np.ones(n2+1)
    b2 = np.zeros(n2+1)
    c2 = np.zeros(n2+1)
    q2 = np.zeros(n2+1)

    d1 = np.zeros((n1+1, n2+1))
    d2 = np.zeros((n2+1, n1+1))
    t0 = 0
    y0 = np.zeros((n1+1, n2+1))
    for i in range(1,n1):
        for j in range(1,n2):
            y0[i,j] = v(i*h1, j*h2)
    y = np.copy(y0)
    while t0 < tEnd * 0.001*tau:
        tau = min(tau, tEnd - t0)
        # x1 direction
        for j in range(1,n2):
            for i in range(1,n1):
                b1[i] = -d1[i+1,j]/h1**2
                c1[i] = -d1[i,j]/h1**2
                a1[i] = 2/tau - b1[i] - c1[i]
                q1[i] = 4*f(i*h1, j*h2, t0)/tau + 2*y[i,j]/tau + ((d2[i,j]/h2**2)*y[i,j-1] - ((d2[i,j+1]/h2**2) + (d2[i,j]/h2**2)) * y[i,j] + (d2[i,j+1]/h2**2) * y[i,j+1])
            y0[:,j] = solveLU3(a1, b1, c1, q1)
        # x2 direction
        for i in range(1,n1):
            for j in range(1,n2):
                b2[j] = -d2[i,j+1]/h2**2
                c2[j] = -d2[i,j]/h2**2
                a2[j] = 2/tau - b2[j] - c2[j]
                q2[j] = 4*f(i*h1, j*h2, t0)/tau + 2*y0[i,j]/tau + ((d1[i,j]/h1**2)*y0[i-1,j] - ((d1[i+1,j]/h1**2) + (d1[i,j]/h1**2)) * y0[i,j] + (d1[i+1,j]/h1**2) * y0[i+1,j])
            y[i,:] = solveLU3(a2, b2, c2, q2)
        t0 = t0 + tau
    return t0, y