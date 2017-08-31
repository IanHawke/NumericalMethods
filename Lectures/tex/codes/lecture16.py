import numpy
from matplotlib import pyplot

def euler_pc(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    for n in range(N):
        fn = f(x[n], y[:,n])
        yp = y[:,n] + dx * fn
        y[:,n+1] = y[:,n] + dx / 2 * (fn + f(x[n+1], yp))
    return x, dx, y

def ab2(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    fn = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    fn[:,0] = f(x[0], y[:,0])
    x_epc, dx_epc, y_epc = euler_pc(f, dx, y0, 1)
    y[:,1] = y_epc[:,1]
    for n in range(1,N):
        fn[:,n] = f(x[n], y[:,n])
        y[:,n+1] = y[:,n] + dx * (3 * fn[:,n] - fn[:,n-1]) / 2
    return x, dx, y

if __name__=="__main__":

    def f_sin(x, y):
        return -numpy.sin(x)
    print("Euler Predictor-Corrector")
    x, dx, y = euler_pc(f_sin, 0.5, [1], 5)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    x, dx, y = euler_pc(f_sin, 0.5, [1], 50)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    Npoints = 5*2**numpy.arange(1,10)
    dx_all = 0.5/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        x, dx, y = euler_pc(f_sin, 0.5, [1], N)
        errors[i] = abs(y[0,-1] - numpy.cos(0.5))
        dx_all[i] = dx
    pyplot.figure(figsize=(12,6))
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[0]*(dx_all/dx_all[0])**2, 'b-',
                  label=r"$\propto \Delta x^2$")
    pyplot.legend(loc='upper left')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()
    
    print("Adams-Bashforth 2")
    x, dx, y = ab2(f_sin, 0.5, [1], 5)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    x, dx, y = ab2(f_sin, 0.5, [1], 50)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    Npoints = 5*2**numpy.arange(1,10)
    dx_all = 0.5/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        x, dx, y = ab2(f_sin, 0.5, [1], N)
        errors[i] = abs(y[0,-1] - numpy.cos(0.5))
        dx_all[i] = dx
    pyplot.figure(figsize=(12,6))
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[0]*(dx_all/dx_all[0])**2, 'b-',
                  label=r"$\propto \Delta x^2$")
    pyplot.legend(loc='upper left')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()
    