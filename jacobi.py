import numpy as np
def elemMax(A):
    '''
    Нахождение наибольшего (по абсолютной величине)
    внедиагонального элемента A[k,l] в верхней половине A
    '''
    n = len(A)
    aMax = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(A[i,j]) >= aMax:
                aMax = abs(A[i,j])
                k = i
                l = j
    return aMax, k, l

def rotate(A, P, k, l):
    '''
    Поворот A, чтобы сделать A[k,l]
    '''
    n = len(A)
    d = A[l,l] - A[k,k]
    if abs(A[k,l]) < abs(d)*1.0e-36:
        t = A[k,l] / d
    else:
        phi = d / (2*A[k,l])
        t = 1 / (abs(phi) + np.sqrt(1 + phi**2))
        if phi < 0:
            t = -t
    c = 1 / np.sqrt(1 + t**2)
    s = t*c
    tau = s / (1 + c)
    # Изменение элементов матрицы
    tt = A[k,l]
    A[k,l] = 0
    A[k,k] = A[k,k] - t*tt
    A[l,l] = A[l,l] + t*tt
    for i in range(k):
        tt = A[i,k]
        A[i,k] = tt - s*(A[i,l] + tau*tt)
        A[i,l] = A[i,l] + s*(tt - tau*A[i,l])
    for i in range(k+1,l):
        tt = A[k,i]
        A[k,i] = tt - s*(A[i,l] + tau*A[k,i])
        A[i,l] = A[i,l] + s*(tt - tau*A[i,l])
    for i in range(l+1,n):
        tt = A[k,i]
        A[k,i] = tt - s*(A[l,i] + tau*tt)
        A[l,i] = A[l,i] + s*(tt - tau*A[l,i])
    # Обновление преобразованной матрицы
    for i in range(n):
        tt = P[i,k]
        P[i,k] = tt - s*(P[i,l] + tau*P[i,k])
        P[i,l] = P[i,l] + s*(tt - tau*P[i,l])

def jacobi(A, tol = 1.0e-12):
    '''
    Решение задачи на собственные значения методом Якоби.
    Возвращает собственные значения в виде вектора lam
    и собственные векторы в виде столбцов матрицы.
    '''
    n = len(A)
    # Ограничение количества оборотов
    rotMax = 5*(n**2)
    P = np.identity(n)
    # Вращательный контур Якоби
    for i in range(rotMax) :
        aMax, k, l = elemMax(A)
        if aMax < tol:
            return np.diagonal(A), P
        rotate(A, P, k, l)
    print('Метод Якоби не сходится')