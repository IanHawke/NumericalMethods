import numpy

def lu(A):
    n = len(A)
    L = numpy.zeros_like(A)
    U = numpy.zeros_like(A)
    for k in range(n):
        L[k, k] = 1.0
        U[k, k] = (A[k, k] - numpy.dot(L[k, :], U[:, k])) / L[k, k]
        for row in range(k+1, n):
            L[row, k] = (A[row,k] - numpy.dot(L[row,:],U[:,k])) / U[k, k]
        for col in range(k+1, n):
            U[k, col] = (A[k,col] - numpy.dot(L[k,:],U[:,col])) / L[k, k]
    return L, U
    
if __name__=="__main__":
    A = numpy.array([[1.0, 2.0, 3.0],
                     [4.0, 5.0, 6.0],
                     [7.0, 8.0, 0.0]])
    b = numpy.array([[1.0], [2.0], [3.0]])
    L, U = lu(A)
    print(A)
    print(L)
    print(U)
    print(numpy.dot(L, U))
    
    # Compare this against the result on the slides
    A = numpy.array([[2.0, 1.0,-1.0],
                     [4.0, 1.0, 0.0],
                     [-2.0,-3.0,8.0]])
    print(A)
    L, U = lu(A)
    print(L)
    print(U)
    print(numpy.dot(L, U))