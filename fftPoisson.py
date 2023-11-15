import numpy as np
from lu3 import solveLU3
def fftPoisson(f, l1, l2, n1, n2):
    """
    Numerical Solution of the Dirichlet problem
    for Poisson equation in a rectangle.
    Fast Fourier transform in the variable x.
    """
    h1 = l1 / n1
    h2 = l2 / n2
    # Fourier coefficients of the right side.
    y = np.zeros((n1+1, n2+1))
    r = np.zeros(2*n1)
    tt = np.zeros(n1+1)
    for j in range(1,n2):
        for i in range(1,n1):
            r[i] = f(i*h1, j*h2)
            r[2*n1-i] = -r[i]
        rt = np.fft.rfft(r).imag
        y[0:n1+1, j] = rt[0:n1+1]
    # Fourier coefficients for the solution.
    a = np.ones(n2+1)
    b = np.zeros(n2+1)
    c = np.zeros(n2+1)
    q = np.zeros(n2+1)
    for i in range(1,n1):
        for j in range(1,n2):
            a[j] = 2 + (2 * np.sin(i*np.pi/(2*n1))/h1)**2*h2**2
            b[j] = -1
            c[j] = -1
            q[j] = y[i,j]*h2**2
        p = solveLU3(a, b, c, q)
        y[i,:] = p
    # Inverse Fourier transform.
    for j in range(1,n2):
        for i in range(1,n1):
            tt[i] = y[i,j]*1.j#################
        yt = np.fft.irfft(tt)
        y[0:n1, j] = yt[0:n1]
    return y