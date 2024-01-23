from numpy import *
import matplotlib.pyplot as plt
from grad import grad
def F(x):
    # Ввод функции
    return 10*(x[1] - x[0]**2)**2 + (1 - x[0])**2
def GradF(x):
    gr = zeros(2)
    gr[0] = -40*(x[1] - x[0]**2)*x[0] - 2*(1 - x[0])
    gr[1] = 20*(x[1] - x[0]**2)
    return gr
# Построение графика
x = linspace(-2, 2, 101)
y = linspace(-1, 3, 101)
X, Y = meshgrid(x, y)
z = F([X,Y])
v = linspace(0, 10, 21)
plt.contourf(x, y, z, v)#, cmap=plt.cm.gray)
plt.colorbar()
# Точка минимума
x0 = array([0, 0.1])
xMin, nIt = grad(F, GradF, x0)
print(f'xMin = {xMin}\nКоличество итераций = {nIt}')
plt.show()