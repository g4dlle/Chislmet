import numpy as np
from relaxation import relaxation
import matplotlib.pyplot as plt
bcList = [0, 10]
sgList = ['-', '--']
kk = 0
for bc in bcList:
    l1 = 1
    l2 = 1
    def f(x,y): return 1
    def b(x,y): return bc
    n1 = 25
    n2 = 25
    m = 20
    om = np.linspace(1, 1.95, m)
    it = np.zeros((m))
    for k in range(m):
        omega = om[k]
        y, iter = relaxation(b, f, l1, l2, n1, n2, omega, tol=1e-6)
        it[k] = iter
    sl = 'b =' + str(bc)
    sg = sgList[kk]
    kk += 1
    plt.plot(om, it, sg, label=sl)
plt.xlabel('$\\omega$')
plt.ylabel('iterations')
plt.legend(loc=0)
plt.grid()
plt.show()
