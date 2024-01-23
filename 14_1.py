import numpy as np
from fftPoisson import fftPoisson
import matplotlib.pyplot as plt
l1 = 2.
l2 = 1.
def f(x,y):
    # Функция
    return 32.*(x*(l1-x)+y*(l2-y))/(l1*l2)**2
n1 = 32
n2 = 16
y = fftPoisson(f,l1,l2,n1,n2).T
print('max y =',np.amax(y))
x1 = np.linspace(0.,l1,n1+1)
x2 = np.linspace(0.,l2,n2+1)
X1,X2 = np.meshgrid(x1,x2)
plt.contourf(X1,X2,y)#,cmap=plt.cm.gray)
plt.colorbar()
plt.show()