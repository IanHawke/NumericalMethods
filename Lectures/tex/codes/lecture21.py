import numpy
from matplotlib import pyplot

from numpy.polynomial.chebyshev import chebpts2

def collocation_matrix(n, bcs):
    x = 0.5 * (1 + chebpts2(n))
    b = numpy.zeros((n,))
    A = numpy.zeros((n,n))
    # Left boundary
    b[0] = bcs[0]
    A[0,0] = 1
    # Right boundary
    b[-1] = bcs[-1]
    A[-1, :] = 1
    
    for nx in range(1,n-1):
        for j in range(n):
            A[nx, j] = A[nx, j] - x[nx]**(j)
        for j in range(2,n):
            A[nx, j] = A[nx, j] + (j)*(j-1)*x[nx]**(j-2)
    
    return numpy.linalg.solve(A, b)

def compute_solution(coeffs, x):
    y = numpy.zeros_like(x)
    for j, c in enumerate(coeffs):
        y = y + c * x**j
    return y
    
x = numpy.linspace(0, 1, 1000)
bcs = [1, numpy.exp(1)]
c3 = collocation_matrix(3, bcs)
y3 = compute_solution(c3, x)
pyplot.figure()
pyplot.plot(x, y3, 'k--', x, numpy.exp(x), 'b-')
pyplot.figure()
pyplot.plot(x, y3-numpy.exp(x))

c5 = collocation_matrix(5, bcs)
y5 = compute_solution(c5, x)
pyplot.figure()
pyplot.plot(x, y5, 'k--', x, numpy.exp(x), 'b-')
pyplot.figure()
pyplot.plot(x, y5-numpy.exp(x))

nbasis = numpy.arange(3,15)
errors = numpy.zeros((len(nbasis),))
for ie, nb in enumerate(nbasis):
    c = collocation_matrix(nb, bcs)
    y = compute_solution(c, x)
    errors[ie] = abs(numpy.linalg.norm(y - numpy.exp(x)))
pyplot.figure()
pyplot.semilogy(nbasis, errors, 'kx', mew=2)