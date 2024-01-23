import numpy as np
import matplotlib.pyplot as plt
from shooting import shooting
def f(x,y):
    f = np.zeros((2), 'float')
    f[0] = y[1]
    f[1] = 100*(y[0] - 1) * y[0]
    return f
mu1 = 0
mu2 = 2
a = 0
b = 1
theta1 = 0
theta2 = 10
nList = [5, 10, 100]
sglist = ['-', '--', ':']
# Построение графика
for k in range(len(nList)):
    n = nList [k]
    x, y = shooting(f, mu1, mu2, a, b, n, theta1, theta2)
    sl = 'n=' + str(n)
    sg = sglist[k]
    plt.plot(x, y, sg, label=sl)
plt.xlabel('x')
plt.grid(True)
plt.legend(loc=2)
plt.show()