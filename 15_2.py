import numpy as np
from parabolic2D import parabolic2D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
l1 = 1
l2 = 1
def f(x, y, t): return x*(l1-x)*y*(l2-y)+2*t*(x*(l1-x)+y*(l2-y))
def v(x, y): return 0
def u(x, y, t): return t*x*(l1-x)*y*(l2-y)
n1 = 50
n2 = 50
tEnd = 1
x = np.linspace(0, l1, n1+1)
y = np.linspace(0, l2, n2+1)
ut = np.zeros((n1+1, n2+1))
for i in range(1,n1):
    for j in range(1,n2):
        ut[i,j] = u(x[i], y[j], tEnd)
tauList = [0.1, 0.05, 0.025]
for tau in tauList:
    t, U = parabolic2D(f, v, l1, l2, tEnd, n1, n2, tau)
    print(f'tau = {tau} erroe = {abs(np.amax(ut-U))}')
fig = plt.figure()
ax = Axes3D(fig)
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, U, rstride=1, cstride=1)
plt.show()