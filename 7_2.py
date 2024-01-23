from numpy import *
from newton import newton
n = 10
def f(x):
    # ВВод системы нелинейных уравнений
    f = zeros(n)
    for i in range(1, n-1):
        f[i] = (3 + 2*x[i]) * x[i] - x[i-1] - 2*x[i+1] - 2
    f[0] = (3 + 2*x[0]) * x[0] - 2*x[1] - 3
    f[n-1] = (3 + 2*x[n-1]) * x[n-1] - x[n-2] - 4
    return f
x0 = zeros(n)
x, iter = newton(f, x0)
print(f'Количество итераций Ньютона = {iter}\nРешение:\n{x}')