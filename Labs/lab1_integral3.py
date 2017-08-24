def integral_1(Nstrips):
    """
    The first integral: integrate x**2 between 0 and 1.
    """
    
    width = 1/Nstrips
    integral = 0
    for point in range(Nstrips):
        location = point / Nstrips
        height = location**2
        integral = integral + width * height
    
    return integral

