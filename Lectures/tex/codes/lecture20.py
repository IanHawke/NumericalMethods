import numpy
import matplotlib
from matplotlib import pyplot
from scipy.optimize import fsolve

matplotlib.rcParams.update({'font.size':18, 'figure.figsize':(10,6)})

def relax_dirichlet(p, q, f, interval, bcs, N):
    x, dx = numpy.linspace(interval[0], interval[1], N+2, retstep=True)
    x_interior = x[1:-1]
    A = numpy.zeros((N,N))
    F = numpy.zeros((N,))
    y = numpy.zeros((N+2,))
    for i in range(N):
        A[i,i] = dx**2 * q(x_interior[i]) - 2
        if i>0:
            A[i,i-1] = 1 - dx/2 * p(x_interior[i])
        if i<N-1:
            A[i,i+1] = 1 + dx/2 * p(x_interior[i])
        F[i] = dx**2 * f(x_interior[i])
    F[0] = F[0] - bcs[0] * (1 - dx/2 * p(x_interior[0]))
    F[-1] = F[-1] - bcs[-1] * (1 + dx/2 * p(x_interior[-1]))
    y_interior = numpy.linalg.solve(A, F)
    y[0] = bcs[0]
    y[1:-1] = y_interior
    y[-1] = bcs[-1]
    
    return x, y
    
def relax_blackbox(f, bcs, N):
    x, dx = numpy.linspace(0, 1, N+2, retstep=True)
    def residual(y):
        y[0] = bcs[0]
        y[-1] = bcs[-1]
        dy = (y[2:] - y[:-2]) / (2*dx)
        res = numpy.zeros_like(y)
        res[1:-1] = y[:-2] + y[2:] - 2*y[1:-1] - dx**2 * f(x[1:-1], y[1:-1], dy)
        return res
    y_initial = numpy.zeros_like(x)
    y = fsolve(residual, y_initial)
    return x, y
    
def relax_newton(f, dfdy, dfddy, bcs, N):
    x, dx = numpy.linspace(0, 1, N+2, retstep=True)
    y = numpy.zeros_like(x)
    y_old = numpy.ones_like(x)
    step = 0
    while numpy.linalg.norm(y-y_old) > 1e-10 and step < 100:
        y_old = y.copy()
        step = step + 1
        y[0] = bcs[0]
        y[-1] = bcs[-1]
        x_interior = x[1:-1]
        y_interior = y[1:-1]
        dy = (y[2:] - y[:-2]) / (2*dx)
        residual = y[:-2] + y[2:] - 2*y[1:-1] - dx**2 * f(x[1:-1], y[1:-1], dy)
        J = numpy.zeros((N,N))
        for i in range(N):
            J[i,i] = -2 - dx**2*dfdy(x_interior[i], y_interior[i], dy[i])
            if i>0:
                J[i,i-1] = 1 + dx/2*dfddy(x_interior[i], y_interior[i], dy[i])
            if i<N-1:
                J[i,i+1] = 1 - dx/2*dfddy(x_interior[i], y_interior[i], dy[i])
        y_new_interior = y_interior + numpy.linalg.solve(J, -residual)
        y[1:-1] = y_new_interior
    
    return x, y
    

if __name__=="__main__":
    def p(x):
        return numpy.ones_like(x)
    def q(x):
        return numpy.zeros_like(x)
    def f(x):
        return -numpy.ones_like(x)

    x_exact = numpy.linspace(0, 1, 1000)
    x, y = relax_dirichlet(p, q, f, [0, 1], [0, 1], 5)
    pyplot.plot(x, y, 'kx', mew=2)
    pyplot.plot(x_exact, 2*numpy.exp(1)/(numpy.exp(1)-1)*(1-numpy.exp(-x_exact))-x_exact)
    pyplot.xlabel(r"$x$")
    pyplot.show()
    pyplot.plot(x, y-(2*numpy.exp(1)/(numpy.exp(1)-1)*(1-numpy.exp(-x))-x))
    pyplot.xlabel(r"$x$")
    pyplot.show()
    
    def f_nonlinear(x, y, dy):
        return -1/(1+y**2)
    def dfdy_nonlinear(x, y, dy):
        return 2*y/(1+y**2)**2
    def dfddy_nonlinear(x, y, dy):
        return numpy.zeros_like(x)
        
    x, y = relax_blackbox(f_nonlinear, [0, 0], 50)
    pyplot.plot(x, y, 'k--')
    pyplot.show()
    
    x, y = relax_newton(f_nonlinear, dfdy_nonlinear, dfddy_nonlinear, 
                        [0, 0], 50)
    pyplot.plot(x, y, 'k--')
    pyplot.show()
    