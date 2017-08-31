import numpy
from matplotlib import pyplot

def rk4(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    for n in range(N):
        k1 = dx * f(x[n]         , y[:,n]         )
        k2 = dx * f(x[n] + dx / 2, y[:,n] + k1 / 2)
        k3 = dx * f(x[n] + dx / 2, y[:,n] + k2 / 2)
        k4 = dx * f(x[n] + dx    , y[:,n] + k3    )
        y[:,n+1] = y[:,n] + (k1 + 2 * (k2 + k3) + k4) / 6
    return x, dx, y

A_am5 = numpy.array([ [1.0, 1, 1, 1, 1],
                      [4.0, 3, 2, 1, 0],
                      [12, 6, 2, 0, 0], 
                      [24, 6, 0, 0, 0],
                      [24, 0, 0, 0, 0]])
rhs_am5 = numpy.array([1.0, 1/2, -1/6, 1/4, -19/30])
b_am5 = numpy.linalg.solve(A_am5, rhs_am5)

A_ab5 = numpy.array([ [1.0, 1, 1, 1, 1],
                      [4.0, 3, 2, 1, 0],
                      [12, 6, 2, 0, 0], 
                      [24, 6, 0, 0, 0],
                      [24, 0, 0, 0, 0]])
rhs_ab5 = numpy.array([1.0, -1/2, 5/6, -9/4, 251/30])
b_ab5 = numpy.linalg.solve(A_ab5, rhs_ab5)

def am5(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    fn = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    x_rk4, dx_rk4, y_rk4 = rk4(f, 4*dx, y0, 4)
    y[:,:5] = y_rk4[:,:5]
    for n in range(5):
        fn[:,n] = f(x[n], y[:,n])
    for n in range(4,N):
        fn[:,n] = f(x[n], y[:,n])
        yp = y[:,n] + dx * (b_ab5[4] * fn[:,n] + 
                            b_ab5[3] * fn[:,n-1] + 
                            b_ab5[2] * fn[:,n-2] + 
                            b_ab5[1] * fn[:,n-3] + 
                            b_ab5[0] * fn[:,n-4])
        fp = f(x[n+1], yp)
        y[:,n+1] = y[:,n] + dx * (b_am5[4] * fp + 
                                  b_am5[3] * fn[:,n] + 
                                  b_am5[2] * fn[:,n-1] + 
                                  b_am5[1] * fn[:,n-2] + 
                                  b_am5[0] * fn[:,n-3])
    return x, dx, y

if __name__=="__main__":

    def f_sin(x, y):
        return -numpy.sin(x)
    print("RK4")
    x, dx, y = rk4(f_sin, 0.5, [1], 10)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    x, dx, y = rk4(f_sin, 0.5, [1], 100)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    Npoints = 5*2**numpy.arange(1,7)
    dx_all = 0.5/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        x, dx, y = rk4(f_sin, 0.5, [1], N)
        errors[i] = abs(y[0,-1] - numpy.cos(0.5))
        dx_all[i] = dx
    pyplot.figure(figsize=(12,6))
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[0]*(dx_all/dx_all[0])**4, 'b-',
                  label=r"$\propto \Delta x^4$")
    pyplot.legend(loc='upper left')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()
    
    print("Adams-Moulton 5")
    x, dx, y = am5(f_sin, 0.5, [1], 10)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    x, dx, y = am5(f_sin, 0.5, [1], 100)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    Npoints = 5*2**numpy.arange(1,7)
    dx_all = 0.5/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        x, dx, y = am5(f_sin, 0.5, [1], N)
        errors[i] = abs(y[0,-1] - numpy.cos(0.5))
        dx_all[i] = dx
    pyplot.figure(figsize=(12,6))
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[0]*(dx_all/dx_all[0])**5, 'b-',
                  label=r"$\propto \Delta x^5$")
    pyplot.legend(loc='upper left')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()
    