import numpy
from matplotlib import pyplot

def basic_integral(f, a, b, N):
    x, dx = numpy.linspace(a, b, N+1, retstep=True)
    fx = f(x)
    return dx * numpy.sum(fx[:-1])
    
def trapezoidal(f, a, b, N):
    x, dx = numpy.linspace(a, b, N+1, retstep=True)
    fx = f(x)
    return dx * ( (fx[0] + fx[-1])/2 + numpy.sum(fx[1:-1]) )
    
if __name__=="__main__":
    print("Basic integral")
    I2 = basic_integral(numpy.sin, 0, numpy.pi/2, 2)
    print(I2)
    I20 = basic_integral(numpy.sin, 0, numpy.pi/2, 20)
    print(I20)
    I200 = basic_integral(numpy.sin, 0, numpy.pi/2, 200)
    print(I200)
    Npoints = 2**numpy.arange(1,20)
    dx_all = numpy.pi/2/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        I = basic_integral(numpy.sin, 0, numpy.pi/2, N)
        errors[i] = abs(I - 1)
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[-1]*(dx_all/dx_all[-1]), 'b-')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()
    
    print("Trapezoidal rule")
    I2 = trapezoidal(numpy.sin, 0, numpy.pi/2, 2)
    print(I2)
    I20 = trapezoidal(numpy.sin, 0, numpy.pi/2, 20)
    print(I20)
    I200 = trapezoidal(numpy.sin, 0, numpy.pi/2, 200)
    print(I200)
    Npoints = 2**numpy.arange(1,20)
    dx_all = numpy.pi/2/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        I = trapezoidal(numpy.sin, 0, numpy.pi/2, N)
        errors[i] = abs(I - 1)
    pyplot.loglog(dx_all, errors, 'kx')
    pyplot.loglog(dx_all, errors[-1]*(dx_all/dx_all[-1])**2, 'b-')
    pyplot.xlabel(r"$\Delta x$")
    pyplot.ylabel("Error")
    pyplot.show()