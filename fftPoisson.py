import numpy as np
import  math as mt
from lu3 import solveLU3
def fftPoisson(f,l1,l2,n1,n2):
    """
    Численное решение задачи Дирихле
    для уравнения Пуассона в прямоугольнике.
    Быстрое преобразование Фурье по переменной x.
    f - функция
    l1 - верхняя граница
    l2 - правая граница
    n1 - 32 (сетка)
    n2 - 16 (сетка)
    """
    h1 = l1/n1
    h2 = l2/n2
    # Коэффициенты Фурье правой части
    y = np.zeros((n1+1,n2+1),'float')
    r = np.zeros((2*n1),'float')
    tt = np.zeros((n1+1),'cfloat')
    for j in range(1,n2):
        for i in range(1,n1):
            r[i] = f(i*h1,j*h2)
            r[2*n1-i] = -r[i]
        rt = np.fft.rfft(r).imag # Прямое преобразование
        y[0:n1+1,j] = rt[0:n1+1]
    a = np.ones((n2+1),'float')
    b = np.zeros((n2+1),'float')
    c = np.zeros((n2+1),'float')
    q = np.zeros((n2+1),'float')
    for i in range(1,n1):
        for j in range(1,n2):
            a[j] = 2.+(2.*mt.sin(i*mt.pi/(2*n1))/h1)**2*h2**2
            b[j] = -1.
            c[j] = -1.
            q[j] = y[i,j]*h2**2
        p = solveLU3(a,b,c,q)
        y[i,:] = p
    for j in range(1,n2):
        for i in range(1,n1):
            tt[i] = y[i,j]*1.j
        yt = np.fft.irfft(tt) # Обратное преобразование
        y[0:n1,j] = yt[0:n1]
    return y