import numpy
from matplotlib import pyplot

def jacobi(A, b, tol=1e-10):
    n = len(A)
    P = numpy.identity(n) - A
    x = numpy.zeros_like(b)
    Nsteps = 100
    errors = numpy.zeros(Nsteps)
    exact_x = numpy.linalg.solve(A, b)
    errors[0] = numpy.linalg.norm(x - exact_x)
    x_norm_change = 1
    step = 0
    while abs(x_norm_change) > tol and step < Nsteps:
        step = step+1
        x_old = x.copy()
        x = numpy.dot(P, x) + b
        x_norm_change = numpy.linalg.norm(x - x_old)
        errors[step] = numpy.linalg.norm(x - exact_x)
    return x, errors[:step+1]
    
def gauss_seidel(A, b, tol=1e-10):
    n = len(A)
    P = numpy.identity(n) - A
    AL = numpy.tril(P)
    AU = numpy.triu(P)
    x = numpy.zeros_like(b)
    Nsteps = 100
    errors = numpy.zeros(Nsteps)
    exact_x = numpy.linalg.solve(A, b)
    errors[0] = numpy.linalg.norm(x - exact_x)
    x_norm_change = 1
    step = 0
    while abs(x_norm_change) > tol and step < Nsteps:
        step = step+1
        x_old = x.copy()
        for row in range(n):
            x[row] = b[row] + numpy.dot(AL[row,:], x) + \
                     numpy.dot(AU[row,:], x_old)
        x_norm_change = numpy.linalg.norm(x - x_old)
        errors[step] = numpy.linalg.norm(x - exact_x)
    return x, errors[:step+1]
    
if __name__=="__main__":
    A = numpy.array([[1.0, 1.0/3.0],
                     [1.0/3.0, 1.0]])
    b = numpy.array([[5.0/3.0], [7.0/3.0]])
    x, errors = jacobi(A, b)
    print(x)
    print(errors[-1])
    pyplot.semilogy(errors, 'kx')
    pyplot.xlabel("Steps")
    pyplot.ylabel("Error")
    pyplot.show()
    
    x, errors = gauss_seidel(A, b)
    print(x)
    print(errors[-1])
    pyplot.semilogy(errors, 'kx')
    pyplot.xlabel("Steps")
    pyplot.ylabel("Error")
    pyplot.show()