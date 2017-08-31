import numpy

def functional_iteration(f, x0, max_steps=100, tol=1e-10):
    N = len(x0)
    x = numpy.zeros((max_steps+1,N))
    x[0,:] = x0
    step = 0
    g = lambda x : x - f(x)
    while numpy.linalg.norm(f(x[step])) > tol and step < max_steps:
        step = step + 1
        x[step,:] = g(x[step-1,:])
    return x[:step+1,:]
    
def newton(f, df, x0, max_steps=100, tol=1e-10):
    N = len(x0)
    x = numpy.zeros((max_steps+1,N))
    x[0,:] = x0
    step = 0
    while numpy.linalg.norm(f(x[step])) > tol and step < max_steps:
        step = step + 1
        fx = f(x[step-1, :])
        J = df(x[step-1, :])
        c = numpy.linalg.solve(J, -fx)
        x[step,:] = x[step-1, :] + c
    return x[:step+1,:]
    
if __name__=="__main__":
    def f(x):
        return numpy.array([  x[0]**2 +    x[1]**2 - 1,
                            5*x[0]**2 + 21*x[1]**2 - 9])
    def df(x):
        return numpy.array([[ 2*x[0],  2*x[1]],
                            [10*x[0], 42*x[1]]])
    
    print("Exact solution is", numpy.array([numpy.sqrt(3)/2, 1/2]))
    x = functional_iteration(f, numpy.array([1, 1]))
    print("Functional iteration", x[-1, :])
    x = newton(f, df, numpy.array([1, 1]))
    print("Newton", x[-1, :], "iterations", len(x))