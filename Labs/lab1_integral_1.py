# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:09:52 2016

@author: ih3
"""

(0**2 + (1/4)**2 + (2/4)**2 + (3/4)**2) * 1/4

Nstrips = 4
width = 1/Nstrips
integral_4 = 0
for point in range(Nstrips):
    print("At point", point)
    height = (point / Nstrips)**2
    integral_4 = integral_4 + width * height
print("Final result is", integral_4)

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

print("One hundred strips:", integral_1(100))
