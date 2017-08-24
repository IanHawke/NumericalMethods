# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:09:07 2016

@author: ih3
"""

import numpy

def integral_2(Nstrips):
    """
    The second integral: integrate sqrt(1-x**2) between 0 and 1.
    """
    
    width = 1/Nstrips
    integral = 0
    for point in range(Nstrips):
        height = numpy.sqrt(1.0-(point / Nstrips)**2)
        integral = integral + width * height
    
    return integral
    
if __name__ == "__main__":
    print("Correct value is pi/4:", numpy.pi/4)
    print("One hundred strips:", integral_2(100))
