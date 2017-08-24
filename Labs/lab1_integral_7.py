# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:37:24 2016

@author: ih3
"""

import numpy

def integral(f, Nstrips):
    """
    The general integral: integrate f between 0 and 1.
    """
    
    locations = numpy.linspace(0.0, 1.0, Nstrips, endpoint=False)
    integral = numpy.sum(f(locations)/Nstrips)
    
    return integral
    
if __name__ == "__main__":
    
    def f_1(x):
        return x**2
    def f_2(x):
        return numpy.sqrt(1.0-x**2)
    
    print("I_1, one hundred strips:", integral(f_1, 100))
    print("I_2, one hundred strips:", integral(f_2, 100))
