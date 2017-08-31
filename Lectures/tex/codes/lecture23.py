import numpy
import matplotlib
from matplotlib import pyplot

matplotlib.rcParams.update({'font.size':18, 'figure.figsize':(10,6)})

def heat_ftcs_step(y, s, bcs):
    ynew = numpy.zeros_like(y)
    ynew[1:-1] = (1 - 2*s) * y[1:-1] + s * (y[2:] + y[:-2])
    ynew[0] = bcs[0]
    ynew[-1] = bcs[-1]
    return ynew
    
if __name__=="__main__":
    
    N = 11
    x, dx = numpy.linspace(0, 1, N+2, retstep=True)
    y = numpy.zeros_like(x)
    for i in range(len(x)):
        if x[i] < 0.25:
            y[i] = 0
        elif x[i] < 0.5:
            y[i] = 4*(x[i] - 0.25)
        elif x[i] < 0.75:
            y[i] = 4*(0.75 - x[i])
        else:
            y[i] = 0
    s = 1/3
    dt = s * dx**2
    t = 0
    t_end = 0.2
    step = 0
    pyplot.figure()
    pyplot.plot(x, y)
    while t < t_end:
        step += 1
        t += dt
        y = heat_ftcs_step(y, s, [0, 0])
        if step % int(t_end/dt/4) == 0:
            pyplot.plot(x, y)
    pyplot.xlabel(r"$x$")
    pyplot.ylabel(r"$y$")
    pyplot.show()