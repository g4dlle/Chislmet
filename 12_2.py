import numpy as np
import matplotlib.pyplot as plt
from oneStep import oneStep
def f(t, y):
    # Ввод функции
    f = np.zeros((2))
    f[0] = y[0] - y[0]*y[1]
    f[1] = -y[1] + y[0]*y[1]
    return f
t0 = 0.
tEnd = 10.
y0 = np.array([2., 2. ])
nTime = 50
theta = 0.5
t, y = oneStep(f, t0, y0, tEnd, nTime, theta)
# Построение графика
for n in range(0, 2):
    r = y [:, n]
    st = '$y_1$'
    sg = '-'
    if n == 1:
        st = '$y_2$'
        sg = '--'
    plt.plot(t, r, sg, label=st)
plt.legend(loc=0)
plt.xlabel ('$t$')
plt.grid(True)
plt.show()