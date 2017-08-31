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
    
if __name__=="__main__":
    def F(x):
        return 1/2*x**2 - 1/52*x**4 - 72/52*x
    def dF(x, dx):
        return (F(x+dx) - F(x)) / dx
        
    f_1em6 = lambda x : dF(x, 1e-6)
    x_df_6 = functional_iteration(f_1em6, 1)
    print("Root: ", x_df_6[-1], "iterations", len(x_df_6))
    f_1em1 = lambda x : dF(x, 1e-1)
    x_df_1 = functional_iteration(f_1em1, 1)
    print("Root: ", x_df_1[-1], "iterations", len(x_df_1))
    f_5em1 = lambda x : dF(x, 5e-1)
    x_df_5 = functional_iteration(f_5em1, 1)
    print("Root: ", x_df_5[-1], "iterations", len(x_df_5))