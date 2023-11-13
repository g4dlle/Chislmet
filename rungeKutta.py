import numpy as np
def rungeKutta(f,t0,y0,tEnd,tau):
    """
    Solve the initial value problem y'=f(t,y)
    by 4th-order Runge-Kutta method.
    t0,y0 are the initial conditions
    tEnd is the terminal value of t,
    tau is the step.
    """
    def increment(f, t, y, tau):
        k0 = tau * f(t,y)
        kl = tau * f(t + tau/2, y + k0/2)
        k2 = tau * f(t + tau/2, y + kl/2)
        k3 = tau * f(t + tau, y + k2)
        return (k0 + 2*kl + 2*k2 + k3) / 6
    t = []
    y = []
    t.append(t0)
    y.append(y0)
    while t0 < tEnd:
        tau = min(tau, tEnd - t0)
        y0 = y0 + increment(f, t0, y0, tau)
        t0 = t0 + tau
        t.append(t0)
        y.append(y0)
    return np.array(t), np.array(y)