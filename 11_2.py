import numpy as np
import matplotlib.pyplot as plt
from fredholm1 import fredholm1
def k(x,s):
    return abs(x-s)
def f(x):
    return x**2
a = -1
b = 1
n = 100
h = (b - a) / n
x = np.linspace(a+h/2, b-h/2, n)
erList = [1e-3, 1e-5, 1e-10]
sgList = ['-', '--', ':']
for kk in range(len(erList)):
    er = erList[kk]
    y, iter = fredholm1(k, f, a, b, n, tol = er)
    print('iteration =', iter, 'tolerance = ', er)
    sl = 'tolerance =' + str(er)
    sg = sgList[kk]
    plt.plot(x, y, sg, label=sl)
plt.xlabel('$x$')
plt.ylim(-2, 3)
plt.grid()
plt.legend(loc = 8)
plt.show()