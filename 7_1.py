from numpy import *
import matplotlib.pyplot as plt
from bisection import bisection
def f(x):
    # Ввод уравнения
    return (1 + x**2) * exp(-x) + sin(x)
x = linspace(0, 10, 100)
y = f(x)
plt.plot(x, y)
plt.xlabel('x')
plt.grid()
xRoot1 = bisection(f, 2, 4)
print(f'root(1) = {xRoot1}')
xRoot2 = bisection(f, 6, 8)
print(f'root(2) = {xRoot2}')
xRoot3 = bisection(f, 8, 10)
print(f'root(3) = {xRoot3}')
plt.show()