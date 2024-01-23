import numpy as np
import matplotlib.pyplot as plt
from interpolation import interpolation, coef
def f(x):
    # Ввод функции
    return 1 / (1 + 25*x**2)
a = -1
b = 1
x1 = np.linspace(a, b, 200)
y1 = f(x1)
plt.plot(x1, y1)
nList = [4, 6, 10] # Количество точек
sgList = ['--', '-.', ':'] # вид графика
for k in range(len(nList)):
    n = nList[k]
    x = np.linspace(a, b, n+1)
    y = f(x)
    plt.scatter(x, y, marker='o')
    c = coef(x, y)
    y1 = interpolation(c, x, x1)
    sl = 'n=' + str(n)
    sg = sgList[k]
    plt.plot(x1, y1, sg, label = sl)
plt.xlabel('x')
plt.grid()
plt.legend(loc=0)
plt.show()