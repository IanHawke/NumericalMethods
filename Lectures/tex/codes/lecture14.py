import numpy
from matplotlib import pyplot

def forward_difference(f, x0, h):
    return (f(x0+h) - f(x0)) / h
def backward_difference(f, x0, h):
    return (f(x0) - f(x0-h)) / h
def central_difference(f, x0, h):
    return (f(x0+h) - f(x0-h)) / (2*h)

def euler(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    for n in range(N):
        y[:,n+1] = y[:,n] + dx * f(x[n], y[:,n])
    return x, dx, y

if __name__=="__main__":
    h = 0.5
    print("Forward difference, h=",h, "y'=", 
          forward_difference(numpy.exp, 0, h))
    print("Backward difference, h=",h, "y'=", 
          backward_difference(numpy.exp, 0, h))
    print("Central difference, h=",h, "y'=", 
          central_difference(numpy.exp, 0, h))
    h = 0.05
    print("Forward difference, h=",h, "y'=", 
          forward_difference(numpy.exp, 0, h))
    print("Backward difference, h=",h, "y'=", 
          backward_difference(numpy.exp, 0, h))
    print("Central difference, h=",h, "y'=", 
          central_difference(numpy.exp, 0, h))
    h_all = 0.5/2**numpy.arange(1,10)
    errors_forward = numpy.zeros_like(h_all)
    errors_backward = numpy.zeros_like(h_all)
    errors_central = numpy.zeros_like(h_all)
    for i, h in enumerate(h_all):
        errors_forward[i] = abs(1 - forward_difference(numpy.exp, 0, h))
        errors_backward[i] = abs(1 - backward_difference(numpy.exp, 0, h))
        errors_central[i] = abs(1 - central_difference(numpy.exp, 0, h))
    pyplot.figure(figsize=(12,6))
    pyplot.loglog(h_all, errors_forward, 'kx', label="Forward")
    pyplot.loglog(h_all, errors_backward, 'bo', label="Backward")
    pyplot.loglog(h_all, errors_central, 'r^', label="Central")
    pyplot.loglog(h_all, h_all/h_all[0]*errors_forward[0], 'b-',
                  label=r"$\propto h$")
    pyplot.loglog(h_all, (h_all/h_all[0])**2*errors_central[0], 'g-',
                  label=r"$\propto h^2$")
    pyplot.xlabel(r"$h$")
    pyplot.ylabel("Error")
    pyplot.legend(loc="upper left")
    pyplot.show()
    

    def f_sin(x, y):
        return -numpy.sin(x)
    print("Euler's Method")
    x, dx, y = euler(f_sin, 0.5, [1], 5)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    x, dx, y = euler(f_sin, 0.5, [1], 50)
    print("dx=", dx, "y(0.5)=", y[0,-1])
    Npoints = 5*2**numpy.arange(1,10)
    dx_all = 0.5/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        x, dx, y = euler(f_sin, 0.5, [1], N)
        errors[i] = abs(y[0,-1] - numpy.cos(0.5))
        dx_all[i] = dx
    pyplot.figure(figsize=(12,6))
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[0]*(dx_all/dx_all[0])**1, 'b-',
                  label=r"$\propto \Delta x$")
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
    x, dx, y = euler(f_circle, 50, y0, 500)
    pyplot.figure(figsize=(8,8))
    pyplot.plot(y[0,:], y[1,:])
    pyplot.show()
    x, dx, y = euler(f_circle, 50, y0, 5000)
    pyplot.figure(figsize=(8,8))
    pyplot.plot(y[0,:], y[1,:])
    pyplot.show()