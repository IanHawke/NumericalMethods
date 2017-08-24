# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:45:35 2016

@author: ih3
"""

def integral_1(Nstrips):
    """
    The first integral: integrate x**2 between 0 and 1.
    """
    
    width = 1/Nstrips
    integral = 0
    for point in range(Nstrips):
        height = (point / Nstrips)**2
        integral = integral + width * height
    
    return integral
    
if __name__ == "__main__":
    print("One hundred strips:", integral_1(100))
