import numpy
from matplotlib import pyplot

def trapezoidal(f, a, b, N):
    x, dx = numpy.linspace(a, b, N+1, retstep=True)
    fx = f(x)
    return dx * ( (fx[0] + fx[-1])/2 + numpy.sum(fx[1:-1]) )
    
def simpsons(f, a, b, N):
    x, dx = numpy.linspace(a, b, N+1, retstep=True)
    fx = f(x)
    return dx/3 * ( (fx[0] + fx[-1]) + \
        2*numpy.sum(fx[2:-1:2]) + 4*numpy.sum(fx[1:-1:2]) )
    
def richardson(f, a, b, N):
    I_h = simpsons(f, a, b, N)
    I_2h = simpsons(f, a, b, N//2)
    return (2**4*I_h - I_2h) / (2**4 - 1)    
    
if __name__=="__main__":
    print("Trapezoidal rule")
    print(trapezoidal(numpy.sin, 0, numpy.pi/2, 2))
    print(trapezoidal(numpy.sin, 0, numpy.pi/2, 4))
    Npoints = 2**numpy.arange(1,20)
    dx_all = numpy.pi/2/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        I = trapezoidal(numpy.sin, 0, numpy.pi/2, N)
        errors[i] = abs(I - 1)
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[0]*(dx_all/dx_all[0])**2, 'b-',
                  label=r"$\propto \Delta x^2$")
    pyplot.legend(loc='upper left')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()
    
    print("Simpson's rule")
    print(simpsons(numpy.sin, 0, numpy.pi/2, 2))
    print(simpsons(numpy.sin, 0, numpy.pi/2, 4))
    Npoints = 2**numpy.arange(1,20)
    dx_all = numpy.pi/2/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        I = simpsons(numpy.sin, 0, numpy.pi/2, N)
        errors[i] = abs(I - 1)
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[0]*(dx_all/dx_all[0])**4, 'b-',
                  label=r"$\propto \Delta x^4$")
    pyplot.legend(loc='upper left')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()
    
    print("Richardson extrapolation")
    print(richardson(numpy.sin, 0, numpy.pi/2, 4))
    print(richardson(numpy.sin, 0, numpy.pi/2, 8))
    Npoints = 2**numpy.arange(2, 10)
    dx_all = numpy.pi/2/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        I = richardson(numpy.sin, 0, numpy.pi/2, N)
        errors[i] = abs(I - 1)
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[0]*(dx_all/dx_all[0])**6, 'b-',
                  label=r"$\propto \Delta x^6$")
    pyplot.legend(loc='upper left')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()
    