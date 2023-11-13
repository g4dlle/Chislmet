def interpolation(c, x, x0):
    """
    Evaluates Newton's polynomial at x0.
    c: data points at x
    x: data points at y
    x0: evaluation point(s)
    """
    # Degree of polynomial
    n = len(x) - 1
    y0 = c[n]
    for k in range(1, n+1):
        y0 = c[n-k] + (x0 - x[n-k]) * y0
    return y0
def coef(x, y):
    """
    Computes the coefficients of Newton's polynomial.
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """
    # Number of data points
    m = len(x)
    c = y.copy()
    for k in range(1,m):
        c[k:m] = (c[k:m] - c[k-1]) / (x[k:m] - x[k-1])
    return c