# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:46:22 2016

@author: ih3
"""

from lab1_integral_3 import integral_1


def integral_4(Nstrips):
    """
    The first integral: integrate x between 0 and 1.
    """
    
    width = 1/Nstrips
    integral = 0
    for point in range(Nstrips):
        height = (point / Nstrips)
        integral = integral + width * height
    
    return integral
    
def integral_total(Nstrips):
    """
    The total integral.
    """
    
    return integral_4(Nstrips) + integral_1(Nstrips)

if __name__ == "__main__":
    print("Total using one hundred strips:", integral_total(100))