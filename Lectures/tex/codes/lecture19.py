import numpy
import matplotlib
from matplotlib import pyplot
from scipy.integrate import odeint
from scipy.optimize import newton

matplotlib.rcParams.update({'font.size':18, 'figure.figsize':(10,6)})

def f(q, x):
    dqdx = numpy.zeros_like(q)
    dqdx[0] = q[1]
    dqdx[1] = -1 - q[1]
    return dqdx
    
def compute_soln(z, x):
    return odeint(f, [0, z], x)
    
def shooting_ivp(z):
    soln = compute_soln(z, [0, 1])
    y_boundary = soln[-1, 0]
    return y_boundary - 1
    
def shooting():
    z_guess = 1.0
    z_proper = newton(shooting_ivp, z_guess)
    x = numpy.linspace(0, 1)
    soln = compute_soln(z_proper, x)
    return x, soln[:, 0]

if __name__=="__main__":

    x, y = shooting()
    pyplot.plot(x, y)
    pyplot.plot(x, 2*numpy.exp(1)/(numpy.exp(1)-1)*(1-numpy.exp(-x))-x)
    pyplot.xlabel(r"$x$")
    pyplot.show()
    pyplot.plot(x, y-(2*numpy.exp(1)/(numpy.exp(1)-1)*(1-numpy.exp(-x))-x))
    pyplot.xlabel(r"$x$")
    pyplot.show()