import numpy
from matplotlib import pyplot

def simpsons(f, a, b, N):
    x, dx = numpy.linspace(a, b, N+1, retstep=True)
    fx = f(x)
    return dx/3 * ( (fx[0] + fx[-1]) + \
        2*numpy.sum(fx[2:-1:2]) + 4*numpy.sum(fx[1:-1:2]) )
        
def simpson_one_interval(f, a, b, h, points, fpoints, tol):
    # Simpson on one interval with three points
    I_2h = 2 * h / 3 * (fpoints[0] + fpoints[2] + 4*fpoints[1])
    # Add new points (and integrand evaluations) for error check
    new_points = [points[0], points[0]+h, points[1], points[1]+h, points[2]]
    f_new_points = [fpoints[0], f(new_points[1]), fpoints[1], f(new_points[3]), fpoints[2]]
    # Simpson over two subintervals
    I_h = h / 3 * (fpoints[0] + fpoints[2] + 2 * fpoints[1] + \
                    4 * (f_new_points[1] + f_new_points[3]))
    # Computable error estimate
    error = abs(I_2h - I_h) / (2**4 - 1)
    # If error on subinterval too big, and interval width not too small,
    # subdivide this subinterval
    if error > tol * (points[2] - points[0]) / (b - a) and (points[2] - points[0])/(b-a) > 1e-3:
        left_I, left_points = simpson_one_interval(f, a, b, h/2, new_points[:3], f_new_points[:3], tol)
        right_I, right_points = simpson_one_interval(f, a, b, h/2, new_points[2:], f_new_points[2:], tol)
        return left_I + right_I, left_points + right_points[1:]
    else:
        return I_h, new_points

def adaptive_quad(f, a, b, tol=1e-6):
    h = (b - a) / 2
    points = [a, a+h, b]
    fpoints = f(numpy.array(points))
    return simpson_one_interval(f, a, b, h/2, points, fpoints, tol)
    
def gauss_legendre(f, a, b, degree):
    nodes, weights = numpy.polynomial.legendre.leggauss(degree)
    x = (b - a) * (nodes + 1) / 2 + a
    fx = f(x)
    return numpy.sum(fx * weights) * (b - a) / 2
    
if __name__=="__main__":
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
    
    print("Adaptive quadrature")
    I, points = adaptive_quad(numpy.sin, 0, numpy.pi/2)
    print(I, len(points))
    x = numpy.linspace(0, numpy.pi/2, 1000)
    pyplot.plot(x, numpy.sin(x), 'b-')
    pyplot.plot(points, numpy.sin(points), 'kx')
    pyplot.show()
    
    def g(x):
        return numpy.where(numpy.pi > x, numpy.ones_like(x), numpy.zeros_like(x))
    I, points = adaptive_quad(g, 0, 5)
    x = numpy.linspace(0, 5, 1000)
    pyplot.plot(x, g(x), 'b-')
    pyplot.plot(points, g(numpy.array(points)), 'kx')
    pyplot.ylim(-0.1, 1.1)
    pyplot.show()
    
    
    print("Gauss-Legendre")
    print(gauss_legendre(numpy.sin, 0, numpy.pi/2, 2))
    print(gauss_legendre(numpy.sin, 0, numpy.pi/2, 4))
    Npoints = numpy.arange(2,10)
    dx_all = numpy.pi/2/Npoints
    errors = numpy.zeros_like(dx_all)
    for i, N in enumerate(Npoints):
        I = gauss_legendre(numpy.sin, 0, numpy.pi/2, N)
        errors[i] = abs(I - 1)
    pyplot.semilogy(Npoints, errors, 'kx')
    pyplot.xlabel(r"$N$")
    pyplot.ylabel("Error")
    pyplot.show()
    
    