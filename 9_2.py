import numpy as np
import matplotlib.pyplot as plt
from spline import spline, coefspline
def f(x):
    # Ввод функции Рунге
    return 1 / (1+25*x**2)
a = -1
b = 1
m = 200
x1 = np.linspace(a, b, m)
y1 = f(x1)
plt.plot(x1, y1)
nList = [4, 6, 10] # Количество точек
sgList = ['--', '-.', ':'] # вид графика
for k in range(len(nList)):
    n = nList[k]
    x = np.linspace(a, b, n+1)
    y = f(x)
    plt.scatter(x, y, marker='o')
    c = coefspline(x, y)
    for i in range(m):
        y1[i] = spline(x, y, c, x1[i])
    sl = 'n=' + str(n)
    sg = sgList[k]
    plt.plot(x1, y1, sg, label = sl)
plt.xlabel('x')
plt.grid()
plt.legend(loc=0)
plt.show()