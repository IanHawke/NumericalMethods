import numpy
from matplotlib import pyplot

def euler_pc(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    for n in range(N):
        fn = f(x[n], y[:,n])
        yp = y[:,n] + dx * fn
        y[:,n+1] = y[:,n] + dx / 2 * (fn + f(x[n+1], yp))
    return x, dx, y

def ab2(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    fn = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    fn[:,0] = f(x[0], y[:,0])
    x_epc, dx_epc, y_epc = euler_pc(f, dx, y0, 1)
    y[:,1] = y_epc[:,1]
    for n in range(1,N):
        fn[:,n] = f(x[n], y[:,n])
        y[:,n+1] = y[:,n] + dx * (3 * fn[:,n] - fn[:,n-1]) / 2
    return x, dx, y

def milne(f, x_end, y0, N):
    x, dx = numpy.linspace(0, x_end, N+1, retstep=True)
    y = numpy.zeros((len(y0),N+1))
    fn = numpy.zeros((len(y0),N+1))
    y[:,0] = y0
    fn[:,0] = f(x[0], y[:,0])
    x_epc, dx_epc, y_epc = euler_pc(f, dx, y0, 1)
    y[:,1] = y_epc[:,1]
    for n in range(1,N):
        fn[:,n] = f(x[n], y[:,n])
        yp = y[:,n] + dx * (3 * fn[:,n] - fn[:,n-1]) / 2 #AB2 predictor
        fp = f(x[n+1], yp)
        y[:,n+1] = y[:,n-1] + dx * (fp + 4 * fn[:,n] + fn[:,n-1]) / 3
    return x, dx, y

if __name__=="__main__":

    def f_exp(x, y):
        return -y
    
    x, dx, y_ab2 = ab2(f_exp, 30, [1], 3000)
    pyplot.figure(figsize=(12,6))
    pyplot.plot(x, y_ab2[0,:])
    pyplot.ylim(-1.1,1.1)
    pyplot.xlabel(r"$x$")
    pyplot.ylabel("Adams-Bashforth 2")
    pyplot.show()
    
    x, dx, y_milne = milne(f_exp, 30, [1], 3000)
    pyplot.figure(figsize=(12,6))
    pyplot.plot(x, y_milne[0,:])
    pyplot.ylim(-1.1,1.1)
    pyplot.xlabel(r"$x$")
    pyplot.ylabel("Milne")
    pyplot.show()
    