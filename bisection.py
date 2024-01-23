from numpy import *
def bisection(f, x1, x2, tol = 1e-10):
    """
    Находит корень из f(x) = 0
    между аргументами x1 и x2 методом бисекции
    f(x1) и f(x2) не могут иметь одинаковые знаки
    """
    f1 = f(x1)
    f2 = f(x2)
    if f1*f2 > 0:
        print("f(x1) и f(x2) имеют одинаковые знаки")
    n = int(ceil(log(abs(x2 - x1) / tol) / log(2.)))
    for i in range(n):
        x3 = 0.5 * (x1 + x2)
        f3 = f(x3)
        if f2*f3 < 0:
            x1 = x3
            f1 = f3
        else:
            x2 = x3
            f2 = f3
    return (x1 + x2) / 2