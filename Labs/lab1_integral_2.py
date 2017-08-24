# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:26:42 2016

@author: ih3
"""

import lab1_integral1


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
    
    return integral_4(Nstrips) + lab1_integral1.integral_1(Nstrips)

print("Total using one hundred strips:", integral_total(100))
