import numpy as np
import matplotlib.pyplot as plt
from fredholm import fredholm
def k(x,s):
    # Ввод интегрального уравнения
    return 1 / (np.pi * (1 + (x - s) ** 2))
def f(x):
    # Правая часть уравнения
    return 1
a = -1
b = 1
nList = [5, 10, 50]
sgList = ['-', '--', ':']
for kk in range(len(nList)):
    n = nList[kk]
    x = np.linspace(a, b, n+1)
    y = fredholm(k, f, a, b, n)
    sl = 'n = ' + str(n+1)
    sg = sgList[kk]
    plt.plot(x, y, sg, label=sl)
plt.xlabel('x')
plt.grid()
plt.legend(loc=0)
plt.show()