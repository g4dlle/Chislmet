from numpy import *
def golden(f, a, b, tol = 1e-10):
    """
    Метод сечения Голдена для определения x
    который минимизирует скалярную функцию f(x).
    Обеспечивает нахождение минимума функции 
    одной переменной на интервале [a,b].
    Возвращает координаты минимума функции
    """
    c1 = (sqrt(5.) - 1.) / 2.
    c2 = 1. - c1
    nIt = int(ceil(log(tol / abs(b-a)) / log(c1)))
    x1 = c1*a + c2*b
    x2 = c2*a + c1*b
    f1 = f(x1)
    f2 = f(x2)
    # Итерационное уточнение интевала
    for i in range(nIt):
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = c2*a + c1*b
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = c1*a + c2*b
            f1 = f(x1)
    if f1 < f2:
        return x1, f1
    else:
        return x2, f2