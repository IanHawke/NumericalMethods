import numpy
from matplotlib import pyplot

def bisection(f, interval, max_steps=100, tol=1e-10):

    x_lo, x_hi = interval
    x = (x_lo + x_hi)/2
    f_lo = f(x_lo)
    f_hi = f(x_hi)
    fx = f(x)
    steps = 0
    
    while steps < max_steps and abs(fx) > tol and (x_hi - x_lo) > tol:
        steps = steps + 1
        if fx*f_hi < 0: # Root lies in right-hand half
            x_lo = x
            f_lo = fx
        else: # Root lies in left-hand half
            x_hi = x
            f_hi = fx
        x = (x_lo + x_hi) / 2
        fx = f(x)
    print("Nsteps", steps)
    return x
    
if __name__=="__main__":
    def f(x):
        return numpy.exp(x) + x - 2
    def g(x):
        return numpy.sin(x**2) - 0.1*x
        
    interval = [0,1]
    s = bisection(f, interval)
    print("s = ", s, "f(s) = ", f(s))
    
    x = numpy.linspace(0, 10, 1000)
    pyplot.plot(x, g(x))
    pyplot.show()
    s = bisection(g, [1,10])
    print("s = ", s, "g(s) = ", g(s))
    s = bisection(g, [1,9])
    print("s = ", s, "g(s) = ", g(s))
    s = bisection(g, [1,8.5])
    print("s = ", s, "g(s) = ", g(s))
    s = bisection(g, [1,8])
    print("s = ", s, "g(s) = ", g(s))
    