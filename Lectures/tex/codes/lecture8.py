import numpy

def functional_iteration(f, x0, max_steps=100, tol=1e-10):
    x = numpy.zeros(max_steps+1)
    x[0] = x0
    step = 0
    g = lambda x : x - f(x)
    while abs(f(x[step])) > tol and step < max_steps:
        step = step + 1
        x[step] = g(x[step-1])
    return x[:step+1]
    
def chord(f, x0, m, max_steps=100, tol=1e-10):
    x = numpy.zeros(max_steps+1)
    x[0] = x0
    step = 0
    g = lambda x : x - m * f(x)
    while abs(f(x[step])) > tol and step < max_steps:
        step = step + 1
        x[step] = g(x[step-1])
    return x[:step+1]
    
def newton(f, df, x0, max_steps=100, tol=1e-10):
    x = numpy.zeros(max_steps+1)
    x[0] = x0
    step = 0
    g = lambda x : x - f(x) / df(x)
    while abs(f(x[step])) > tol and step < max_steps:
        step = step + 1
        x[step] = g(x[step-1])
    return x[:step+1]
    
def secant(f, x0, x1, max_steps=100, tol=1e-10):
    x = numpy.zeros(max_steps+1)
    x[0] = x0
    x[1] = x1
    step = 1
    while abs(f(x[step])) > tol and step < max_steps:
        step = step + 1
        x[step] = x[step-1] - f(x[step-1]) * (x[step-1] - x[step-2]) / \
                    (f(x[step-1]) - f(x[step-2]))
    return x[:step+1]
    
if __name__=="__main__":
    def f(x):
        return x - numpy.cos(x)
    def df(x):
        return 1 + numpy.sin(x)
    
    x_func_iteration = functional_iteration(f, 0)
    print("Functional iteration")
    print("s={}, f(s)={}, in {} steps".format(x_func_iteration[-1],
          f(x_func_iteration[-1]), len(x_func_iteration)))
    x_chord = chord(f, 0, 1.08)
    print("Chord, m=1.08")
    print("s={}, f(s)={}, in {} steps".format(x_chord[-1],
          f(x_chord[-1]), len(x_chord)))
    x_chord = chord(f, 0, 0.8)
    print("Chord, m=0.8")
    print("s={}, f(s)={}, in {} steps".format(x_chord[-1],
          f(x_chord[-1]), len(x_chord)))
    x_newton = newton(f, df, 0)
    print("Newton")
    print("s={}, f(s)={}, in {} steps".format(x_newton[-1],
          f(x_newton[-1]), len(x_newton)))
    x_secant = secant(f, 0, 1)
    print("Secant")
    print("s={}, f(s)={}, in {} steps".format(x_secant[-1],
          f(x_secant[-1]), len(x_secant)))