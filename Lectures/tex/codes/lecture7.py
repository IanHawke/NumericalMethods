import numpy

if __name__=="__main__":
    def f(x):
        return x - numpy.cos(x)
        
    def g(x):
        return x - f(x)
    
    Nsteps = 100
    x = numpy.zeros(Nsteps+1)
    for step in range(Nsteps):
        x[step+1] = g(x[step])
    print(x[0])
    print(x[1])
    print(x[5])
    print(x[20])
    print(x[50])
    print(x[-1])
    print(x[100] - x[50])
    print(x[100]- x[90])
    print(f(x[100]))
    print(f(x[50]))
    print(f(x[60]))