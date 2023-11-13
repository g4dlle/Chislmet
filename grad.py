import numpy as np
from golden import golden
def grad(F, GradF, x, d=0.5, tol=1e-10):
    """
    Gradient method for determining vector x
    that minimizes the function F(x),
    GradF(x) is function for grad(F),
    x is starting point.
    """
    # Line function along h
    def f(al):
        return F(x + al*h)
    gr0 = -GradF(x)
    h = gr0.copy()
    F0 = F(x)
    iterMax = 500
    for i in range(iterMax):
        # Minimization 1D function
        al, fMin = golden(f, 0, d)
        x = x + al*h
        F1 = F(x)
        gr1 = -GradF(x)
        if (np.sqrt(np.dot(gr1,gr1)) <= tol) or (abs(F0 - F1) < tol):
            return x, i+1
        h = gr1
        gr0 = gr1.copy()
        F0 = F1
    print("Gradient method didn't converge (500 iterations)")
