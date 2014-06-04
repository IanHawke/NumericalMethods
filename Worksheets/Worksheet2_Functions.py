
## Worksheet 2
    
import numpy as np
import scipy.linalg as la

#### Answer Coding Question 1

def LU_decomposition(A):
    """Perform LU decomposition using the Doolittle factorisation."""
    
    L = np.zeros_like(A)
    U = np.zeros_like(A)
    N = np.size(A, 0)
    
    for k in range(N):
        L[k, k] = 1
        U[k, k] = (A[k, k] - np.dot(L[k, :k], U[:k, k])) / L[k, k]
        for j in range(k+1, N):
            U[k, j] = (A[k, j] - np.dot(L[k, :k], U[:k, j])) / L[k, k]
        for i in range(k+1, N):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]
    
    return L, U

#### Answer Coding Question 2

def ThomasAlgorithm(a, b, c, f):
    """Implement the Thomas algorithm to solve A x = f. 
    The vectors a, b, c are the sub-diagonal, diagonal and super-diagonal 
    vectors of the original matrix A."""
    
    # Make copies of the input
    aa = a.copy()
    bb = b.copy()
    cc = c.copy()
    
    x = np.zeros_like(f)
    d = np.zeros_like(f)
    d[:] = f[:]
    N = len(f)
    for k in range(1, N):
        m = aa[k-1] / bb[k-1]
        bb[k] -= m * cc[k-1]
        d[k] -= m * d[k-1]
    x[-1] = d[-1] / bb[-1]
    for k in range(N-2, -1, -1):
        x[k] = (d[k] - cc[k] * x[k+1]) / bb[k]
    
    return x

#### Answer Coding Question 3

def Jacobi(A, b, tolerance = 1.e-10, MaxSteps = 100):
    """Solve the linear system A x = b using Jacobi's method, 
    starting from the trivial initial guess."""
    
    x = np.zeros_like(b)
    
    Anorm = A.copy()
    bnorm = b.copy()
    n = len(b)
    
    for i in range(n):
        bnorm[i] /= A[i, i]
        Anorm[i, :] /= A[i, i]
    
    # Compute the split
    N = np.eye(n)
    P = N - Anorm
    AL = la.tril(P)
    AU = la.triu(P)
    
    # Compute the convergence matrix and check its spectral radius
    M = np.dot(la.inv(N), P)
    eigenvalues, eigenvectors = la.eig(M)
    rho = np.amax(np.absolute(eigenvalues))
    if (rho > 1):
        print("Jacobi will not converge as the"\
            " largest eigenvalue of the convergence matrix is {}".format(rho))
    
    for j in range(MaxSteps):
        x_old = x.copy()
        x = bnorm + np.dot(AL + AU, x)
        if (la.norm(x - x_old) < tolerance):
            print "Jacobi converged in ", j, " iterations."
            break
    
    return x

#### Answer Coding Question 4

def GaussSeidel(A, b, tolerance = 1.e-10, MaxSteps = 100):
    """Solve the linear system A x = b using the Gauss-Seidel method, 
    starting from the trivial initial guess."""
    
    x = np.zeros_like(b)
    
    Anorm = A.copy()
    bnorm = b.copy()
    n = len(b)
    
    for i in range(n):
        bnorm[i] /= A[i, i]
        Anorm[i, :] /= A[i, i]
    
    # Compute the split
    D = np.eye(n)
    AL = la.tril(D - Anorm)
    AU = la.triu(D - Anorm)
    N = np.eye(n) - AL
    P = AU
    
    # Compute the convergence matrix and check its spectral radius
    M = np.dot(la.inv(N), P)
    eigenvalues, eigenvectors = la.eig(M)
    rho = np.amax(np.absolute(eigenvalues))
    if (rho > 1):
        print("Gauss-Seidel will not converge as the"\
              " largest eigenvalue of the convergence matrix is {}".format(rho))
    
    for j in range(MaxSteps):
        x_old = x.copy()
        for i in range(n):
            x[i] = bnorm[i] + np.dot(AL[i, :], x) + np.dot(AU[i, :], x_old)
        if (la.norm(x - x_old) < tolerance):
            print("Gauss-Seidel converged in {} iterations.".format(j))
            break
    
    return x

#### Answer Coding Question 5

def chord(f, m, x0, tolerance = 1e-10, MaxSteps = 100):
    """Implement the chord method to find the root of the equation f(x) = 0, 
    starting from the initial guess x^{(0)} = x0."""
    
    x = np.zeros(MaxSteps)
    x[0] = x0
    
    # Set up the map g
    g = lambda x: x - m * f(x)
    
    for i in range(1, MaxSteps):
        x[i] = g(x[i-1])
        if (np.absolute(f(x[i])) < tolerance):
            break
    return x[:i+1]

