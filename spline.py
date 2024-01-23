import numpy as np
from lu3 import solveLU3
def spline(x, y, c, x0):
    """
    Оценивает кубический сплайн в точке x0.
    """
    def find(x, x0):
        """
        Нахождение отрезока, охватывающий x0
        """
        iL = 0
        iR = len(x) - 1
        while iR - iL > 1:
            i = int((iL + iR) / 2)
            if x0 < x[i]:
                iR = i
            else:
                iL = i
        return iL
    i = find(x, x0)
    h = x[i+1] - x[i]
    y0 = ((x[i+1] - x0)**3/h - (x[i+1] - x0)*h) * c[i] / 6 \
        + ((x0 -x[i])**3/h - (x0 -x[i])*h) * c[i+1] / 6 \
            + (y[i]*(x[i+1] - x0) + y[i+1]*(x0 - x[i])) / h
    return y0
def coefspline(x, y):
    """
    Вычисление коэффициентов кубического сплайна.
    """
    n = len(x) - 1
    a = np.ones(n+1)
    b = np.zeros(n+1)
    c = np.zeros(n+1)
    f = np.zeros(n+1)
    for i in range(1,n):
        a[i] = 2*(x[i+1] - x[i-1])
        b[i] = x[i+1] - x[i]
        c[i] = x[i] - x[i-1]
        f[i] = 6*(y[i+1] - y[i]) / (x[i+1] - x[i]) \
            - 6*(y[i] - y[i-1]) / (x[i] - x[i-1])
    return solveLU3(a, b, c, f)