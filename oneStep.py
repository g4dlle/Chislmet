import numpy as np
from newton import newton
def oneStep(f, t0, y0, tEnd, nTime, theta):
    """
    Solve the initial value problem y’ = f(t,y)
    by one-step methods implisit method.
    t0,y0 are the initial conditions,
    tEnd is the terminal value of t,
    nTime is the number of steps.
    """
    tau = (tEnd - t0) / nTime
    def f1(y1):
        f1 = y1 - tau * theta * f(t0+tau,y1) \
            - y0 - tau * (1.-theta) * f(t0+tau,y0)
        return f1
    t = []
    y = []
    t.append(t0)
    y.append(y0)
    for i in range(nTime):
        r = y0 - tau * f(t0+tau,y0)
        y1, iter = newton(f1, r)
        y0 = y1
        t0 = t0 + tau
        t.append(t0)
        y.append(y0)
    return np.array(t), np.array(y)