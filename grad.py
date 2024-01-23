import numpy as np
from golden import golden
def grad(F, GradF, x, d=0.5, tol=1e-10):
    """
    Градиентный метод для определения вектора x
    который минимизирует функцию F(x),
    GradF(x) - функция для grad(F),
    x - начальная точка.
    """
    # Линейная функция вдоль h
    def f(al):
        return F(x + al*h)
    gr0 = -GradF(x)
    h = gr0.copy()
    F0 = F(x)
    iterMax = 500
    for i in range(iterMax):
        # Минимизация одномерной функции
        al, fMin = golden(f, 0, d)
        x = x + al*h
        F1 = F(x)
        gr1 = -GradF(x)
        if (np.sqrt(np.dot(gr1,gr1)) <= tol) or (abs(F0 - F1) < tol):
            return x, i+1
        h = gr1
        gr0 = gr1.copy()
        F0 = F1
    print("Градиентный метод не сходится (500 итераций)")