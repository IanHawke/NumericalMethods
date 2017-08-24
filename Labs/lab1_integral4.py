def f_x_squared(x):
    """
    Square the input
    """
    return x**2

def integral_2(f, Nstrips):
    """
    The general integral: f(x) between 0 and 1.
    """
    
    width = 1/Nstrips
    integral = 0
    for point in range(Nstrips):
        location = point / Nstrips
        height = f(location)
        integral = integral + width * height
    
    return integral


