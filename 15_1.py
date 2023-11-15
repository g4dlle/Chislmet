import numpy as np
from parabolic1D import parabolic1D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def k(x): return 1
def f(x, t):  return 0 # np.exp(x)
def v(x): return np.sin(np.pi*x) + np.sin(4*np.pi*x)
l = 1
n = 50
h = l / n
tEnd = 0.1
u = np.zeros(n+1)
tauList = [0.01, 0.005, 0.0025]
for tau in tauList:
    print('tau =', tau)
    for sigma in [0.5, 1]:
        t, y = parabolic1D(k, f, v, l, tEnd, n, tau, sigma)
        erMax = 0
        for m in range(len(t)):
            yk = y[m,:]
            for i in range(1,n):
                x = i*h
                pt = np.pi**2*t[m]
                u[i] = np.sin(np.pi*x)*np.exp(-pt) \
                    + np.sin(4*np.pi*x)*np.exp(-16*pt)
            er = np.sqrt(np.dot(yk-u, yk-u)*h)
            if er > erMax:
                erMax = er
        print('sigma =', sigma, 'er =', erMax)
fig = plt.figure()
ax = Axes3D(fig)
xx = np.linspace(0, l, n+1)
t, y = parabolic1D(k, f, v, l, tEnd, n, tau=0.001, sigma=0.5)
X, T = np.meshgrid(xx, t)
ax.plot_surface(X, T, y, rstride=1, cstride=1)
plt.show()