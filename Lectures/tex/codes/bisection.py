import numpy

def bisection(f, interval, eps_abs = 1e-10, max_step = 100):
    """
    Use bisection to find x such that f(x) = 0.
    """
    
    x_lo, x_hi = interval
    x = (x_lo + x_hi) / 2.0
    f_lo = f(x_lo)
    if (abs(f_lo) < eps_abs):
        return x_lo
    f_hi = f(x_hi)
    if (abs(f_hi) < eps_abs):
        return x_hi
    #assert(f_lo*f_hi < 0), "f(Endpoints) must change sign!"
    if f_lo*f_hi > 0:
        print("Warning! f(endpoints) have same sign!")
    
    f_mid = f(x)
    step = 0
    while (step < max_step) and abs(f_mid) > eps_abs:
        step += 1
        if f_lo * f_mid < 0.0:
            x_hi = x
            f_hi = f(x_hi)
        else:
            x_lo = x
            f_lo = f(x_lo)
        x = (x_lo + x_hi) / 2.0
        f_mid = f(x)
    
    return x
    

if __name__ == "__main__":
    def f(x):
        return numpy.exp(x) + x - 2
    def g(x):
        return numpy.sin(x**2) - 0.1 * x
        
    interval = [0, 1]
    s = bisection(f, interval)
    print("s = {}, f(s) = {}".format(s, f(s)))
    for lower in range(1,9):
        interval = [lower, 10]
        try:
            s = bisection(g, interval)
            print("interval = [{}, 10], s = {}, g(s) = {}".format(lower, s, g(s)))
        except:
            pass
