import numpy as np
def relaxation(b, f, l1, l2, n1, n2, omega, tol = 1e-8):
    """
    Numetical Solution of the Dirichlet problem
    for convection-diffusion equation in a rectangle.
    Method of relaxation.
    """
    h1 = l1 / n1
    h2 = l1 / n2
    d = 2 / h1**2 + 2 / h2**2
    y = np.zeros((n1+1, n2+1))
    ff = np.zeros((n1+1, n2+1))
    bb = np.zeros((n1+1, n2+1))
    for j in range(1,n2):
        for i in range(1,n1):
            ff[i,j] = f(i*h1, j*h2)
            bb[i,j] = b(i*h1, j*h2)
    # the maximum number of iterations is 10000
    for k in range(10001):
        rn = 0
        for j in range(1,n2):
            for i in range(1,n1):
                rr = -(y[i-1,j] - 2*y[i,j] + y[i+1,j]) / h1**2 \
                -(y[i,j-1] - 2*y[i,j] + y[i,j+1]) / h1**2 \
                + bb[i,j] * (y[i+1,j] - y[i-1,j]) / (2*h1) - ff[i,j]
                rn = rn + rr**2
                y[i,j] = y[i,j] - omega * rr / d
        rn = rn*h1*h2
        if rn < tol**2: return y, k
    print('Relaxation method failed to converge:')
    print('ater 10000 iteration residual =', np.sqrt(rn))