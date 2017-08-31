import numpy
import matplotlib
from matplotlib import pyplot

matplotlib.rcParams.update({'font.size':18, 'figure.figsize':(10,6)})

def burgers_upwind_periodic(y, c, bcs):
    ynew = numpy.zeros_like(y)
    for i in range(1, len(y)-1):
        if y[i] > 0: #FTBS
            ynew[i] = y[i] - c * y[i] * (y[i] - y[i-1])
        else: #FTFS
            ynew[i] = y[i] - c * y[i] * (y[i+1] - y[i])
    ynew[0] = bcs[0]
    ynew[-1] = bcs[-1]
    return ynew
    
if __name__=="__main__":
    
    N = 11
    x, dx = numpy.linspace(0, 1, N+2, retstep=True)
    y = numpy.sin(2*numpy.pi*x)
    c = 1/2
    dt = c * dx
    t = 0
    t_end = 0.4
    step = 0
    pyplot.figure()
    pyplot.plot(x, y, 'kx', mew=2)
    pyplot.xlabel(r"$x$")
    pyplot.ylabel(r"$y$")
    while t < t_end:
        step += 1
        t += dt
        y = burgers_upwind_periodic(y, c, [0, 0])
        if step % int(t_end/dt/4) == 0:
            pyplot.figure()
            pyplot.plot(x, y, 'kx', mew=2)
            pyplot.xlabel(r"$x$")
            pyplot.ylabel(r"$y$")
    pyplot.show()