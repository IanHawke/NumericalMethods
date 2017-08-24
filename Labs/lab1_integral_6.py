# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:17:58 2016

@author: ih3
"""


import numpy

def integral(f, Nstrips):
    """
    The general integral: integrate f between 0 and 1.
    """
    
    width = 1/Nstrips
    integral = 0
    for point in range(Nstrips):
        height = f(point / Nstrips)
        integral = integral + width * height
    
    return integral
    
if __name__ == "__main__":
    
    def f_1(x):
        return x**2
    def f_2(x):
        return numpy.sqrt(1.0-x**2)
    
    print("I_1, one hundred strips:", integral(f_1, 100))
    print("I_2, one hundred strips:", integral(f_2, 100))
