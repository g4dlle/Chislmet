import numpy as np
from bisection import bisection
from rungeKutta import rungeKutta
def shooting(f, mu1, mu2, a, b, n, theta1, theta2):
    """
    Решение задачи Дирихле для
    уравнения второго порядка методом стрельбы.
    Метод биссекции для нахождения граничных условий.
    Метод Рунге-Кутты четвертого порядка для решения задачи Коши.
    Метод стрельбы при приближенном решение краевой задачи
    основан на решении задач Коши для уравнений 1 порядка
    f - функция
    mu1 - нижняя граница
    mu2 - верхняя граница
    a - начало по x
    b - конец по x
    n - количество точек
    theta1 - первый аргумент для bisection
    theta2 - второй аргумент для bisection
    Возвращает точку и значение в точке
    """
    h = (b - a) / n
    # Начальные значения
    def y0(theta):
        return np.array([mu1, theta])
    # Остаточные граничные условия
    def r(theta):
        x, y = rungeKutta(f, a, y0(theta), b, h)
        yb = y [len(y) -1]
        r = yb[0] - mu2
        return r
    theta = bisection(r, theta1, theta2)
    x, y = rungeKutta(f, a, y0(theta), b, h)
    return x, y[:,0]