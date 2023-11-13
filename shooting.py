import numpy as np
from bisection import bisection
from rungeKutta import rungeKutta
def shooting(f, mu1, mu2, a, b, n, theta1, theta2):
    """
    Solution of the Dirichlet problem for
    second- order equation be the method of shooting.
    Bisection method for finding the boundary conditions.
    Runge-Kutta fourth order for the solution of the Cauchy problem.
    """
     h = (b - a) / n
     # Initial values
     def y0(theta):
         return np.array([mu1, theta])
     # Boundary conditions residual
     def r(theta):
         x, y = rungeKutta(f, a, y0(theta), b, h)
         yb = y [len(y) -1]
         r = yb[0] - mu2
         return r
     theta = bisection(r, theta1, theta2)
     x, y = rungeKutta(f, a, y0(theta), b, h)
     return x, y[:,0]