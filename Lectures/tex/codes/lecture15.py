import numpy
from matplotlib import pyplot

def euler(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    for n in range(N):
        y[:,n+1] = y[:,n] + dx * f(x[n], y[:,n])
    return x, dx, y

def euler_pc(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    for n in range(N):
        fn = f(x[n], y[:,n])
        yp = y[:,n] + dx * fn
        y[:,n+1] = y[:,n] + dx / 2 * (fn + f(x[n+1], yp))
    return x, dx, y

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
    
    def f_circle(x, y):
        dydx = numpy.zeros_like(y)
        dydx[0] = -y[1]
        dydx[1] = y[0]
        return dydx
    y0 = numpy.array([1, 0])
    x, dx, y = euler_pc(f_circle, 50, y0, 500)
    pyplot.figure(figsize=(8,8))
    pyplot.plot(y[0,:], y[1,:])
    pyplot.show()
    
    print("RK4")
    x, dx, y = rk4(f_sin, 0.5, [1], 5)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    x, dx, y = rk4(f_sin, 0.5, [1], 50)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    Npoints = 5*2**numpy.arange(1,10)
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
    
    y0 = numpy.array([1, 0])
    x, dx, y = rk4(f_circle, 50, y0, 500)
    pyplot.figure(figsize=(8,8))
    pyplot.plot(y[0,:], y[1,:])
    pyplot.show()