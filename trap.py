def trap(f, a, b, tol=1e-6):
    """
    Возвращает приближенное значение интеграла f(x) от a до b,
    ывычисленный по правилу трапеций
    """
    h = b - a
    Iold = h - (f(a) + f(b)) / 2
    m = 1
    kMax = 25
    for k in range(1, kMax):
        x = a + h / 2
        sum = 0
        for i in range(m):
            sum = sum + f(x)
            x = x + h
        Inew = (Iold + h*sum) / 2
        if (k > 1) and (abs(Inew - Iold) < tol): break
        Iold = Inew
        m = m * 2
        h = h / 2
    return Inew