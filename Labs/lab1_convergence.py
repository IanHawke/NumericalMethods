# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:44:38 2016

@author: ih3
"""

import numpy
from matplotlib import pyplot
from lab1_integral_7 import integral

def f_2(x):
    return numpy.sqrt(1.0-x**2)
    
I_2_exact = numpy.pi/4

Nstrips_all = 2**numpy.arange(10, 20)
widths = 1.0 / Nstrips_all
errors = numpy.zeros_like(widths)
for i, Nstrips in enumerate(Nstrips_all):
    I_2_approx = integral(f_2, Nstrips)
    errors[i] = abs(I_2_exact - I_2_approx)

pyplot.loglog(widths, errors, marker='x', label = r"$I_2$")
pyplot.ylabel("Error")
pyplot.xlabel("Strip width")
pyplot.legend(loc="upper left")
pyplot.show()