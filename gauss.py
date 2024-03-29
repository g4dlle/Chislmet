import numpy as np
def gauss(f, a, b, n):
    """
    Интеграл f(x) от a до b, вычисленный с помощью 
    квадратуры Гаусса-Лежандра с использованием m узлов.
    """
    if n > 8 or n < 2:
        print('Количество узлов должно быть больше чем 2 и меньше чем 8')
        return 0
    x = np.zeros((n))
    c = np.zeros((n))
    # Ввод табличных значений
    if n == 2:
        x[0] = 0.57735027
        x[1] = -x[0]
        c[0] = 1
        c[1] = c[0]
    if n == 3:
        x[0] = 0.77459667
        x[1] = -x[0]
        x[2] = 0
        c[0] = 0.55555556
        c[1] = c[0]
        c[2] = 0.88888889
    if n == 4:
        x[0] = 0.86113631
        x[1] = -x[0]
        x[2] = 0.33998104
        x[3] = -x[2]
        c[0] = 0.34785485
        c[1] = c[0]
        c[2] = 0.65214515
        c[3] = c[2]
    if n == 5:
        x[0] = 0.90617985
        x[1] = -x[0]
        x[2] = 0.53846931
        x[3] = -x[2]
        x[4] = 0
        c[0] = 0.23692689
        c[1] = c[0]
        c[2] = 0.47862867
        c[3] = c[2]
        c[4] = 0.56888889
    if n == 6:
        x[0] = 0.93244951
        x[1] = -x[0]
        x[2] = 0.66120939
        x[3] = -x[2]
        x[4] = 0.23861919
        x[5] = -x[4]
        c[0] = 0.17132449
        c[1] = c[0]
        c[2] = 0.36076157
        c[3] = c[2]
        c[4] = 0.46791393
        c[5] = c[4]
    if n == 7:
        x[0] = 0.94910791
        x[1] = -x[0]
        x[2] = 0.74153119
        x[3] = -x[2]
        x[4] = 0.40584515
        x[5] = -x[4]
        x[6] = 0
        c[0] = 0.12948497
        c[1] = c[0]
        c[2] = 0.27970539
        c[3] = c[2]
        c[4] = 0.38183005
        c[5] = c[4]
        c[6] = 0.41795918
    if n == 8:
        x[0] = 0.96028986
        x[1] = -x[0]
        x[2] = 0.79666648
        x[3] = -x[2]
        x[4] = 0.52553241
        x[5] = -x[4]
        x[6] = 0.18343464
        x[7] = -x[6] 
        c[0] = 0.10122854
        c[1] = c[0]
        c[2] = 0.22238103
        c[3] = c[2]
        c[4] = 0.31370665
        c[5] = c[4]
        c[6] = 0.36268378
        c[7] = c[6]
    c1 = (b + a) / 2
    c2 = (b - a) / 2
    sum = 0
    for i in range(n):
        sum = sum + c[i] * f(c1 + c2*x[i])
    return c2*sum