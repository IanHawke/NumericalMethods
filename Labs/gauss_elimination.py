import numpy

def gauss_elimination(A, b):
    """
    Solve A x = b
    """
    n = len(b)
    aug = numpy.hstack((A, numpy.reshape(b, (n, 1))))
    # Elimination
    for col in range(n):
        for row in range(col+1,n):
            pivot = aug[row,col] / aug[col,col]
            aug[row,:] -= pivot * aug[col,:]
    # Back substitution
    x = numpy.zeros_like(b)
    for row in range(n-1,-1,-1):
        x[row] = aug[row, -1] / aug[row, row]
        for col in range(row+1,n):
            x[row] -=  aug[row, col] * x[col] / aug[row, row]
    return x

def test_diagonal():
    A = numpy.identity(2)
    b = numpy.ones((2,))
    assert(numpy.all(b == gauss_elimination(A, b)))
    
def test_full():
    A = numpy.array([[1.0, 2.0], [3.0, 4.0]])
    b = numpy.array([5.0, 6.0])
    x_exact = [-4.0, 4.5]
    assert(numpy.all(x_exact == gauss_elimination(A, b)))
    
def test_pivoting():
    A = numpy.array([[1.0e-20, 1.0], [1.0, 1.0]])
    b = numpy.array([1.0, 2.0])
    x_exact = [1.0, 1.0]
    assert(numpy.all(x_exact == gauss_elimination(A, b)))