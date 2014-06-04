# -*- coding: utf-8 -*-
"""
Example solutions for Worksheet 1

Ian Hawke
"""

def MatrixConditionCheck(A):
    import numpy as np

    MaxConditionNumber = 10 # This is absurdly low    
    ConditionNumber = np.linalg.cond(A)
    if ConditionNumber > MaxConditionNumber:
        print "Condition number of matrix\n", A, "\ntoo large (bigger than", MaxConditionNumber, ").\n"
    

import numpy as np

print "\nQuestion 1\n"

A1 = np.array([[1,2],[3,4]])
A1T = np.transpose(A1)
A1I = np.linalg.inv(A1)
print "The matrix\n", A1, "\nhas transpose\n", A1T, "\nand inverse\n", A1I

A2 = np.array([[-3,2],[3,6]])
A2T = np.transpose(A2)
A2I = np.linalg.inv(A2)
print "The matrix\n", A2, "\nhas transpose\n", A2T, "\nand inverse\n", A2I

print "\nQuestion 2\n"

v1 = np.array([1,3,-1])
v2 = np.array([1,-2])
v3 = np.array([1,6,-3,1])

print "The vector\n", v1, "\nhas norms", np.linalg.norm(v1,1), np.linalg.norm(v1,2), np.linalg.norm(v1,np.inf)
print "The vector\n", v2, "\nhas norms", np.linalg.norm(v2,1), np.linalg.norm(v2,2), np.linalg.norm(v2,np.inf)
print "The vector\n", v3, "\nhas norms", np.linalg.norm(v3,1), np.linalg.norm(v3,2), np.linalg.norm(v3,np.inf)

print "The matrix\n", A1, "\nhas norms", np.linalg.norm(A1,1), np.linalg.norm(A1,np.inf)
print "The matrix\n", A2, "\nhas norms", np.linalg.norm(A2,1), np.linalg.norm(A2,np.inf)

print "\nQuestion 3\n"

MatrixConditionCheck(A1)
MatrixConditionCheck(A2)

print "\nQuestion 4\n"

# Bisection algorithm

tolerance = 1e-15
# Define the function
f = lambda x: np.tan(x) - np.exp(-x)
# Define the interval
x_min = 0.0
x_max = 1.0
# Values at the ends of the domain
f_min = f(x_min)
f_max = f(x_max)
assert(f_min * f_max < 0.0)
# The loop
x_c = (x_min + x_max) / 2.0
f_c = f(x_c)
iteration = 0
while ((x_max - x_min > tolerance) and (np.abs(f_c) > tolerance) and (iteration < 100)):
    iteration = iteration+1    
    if f_min * f_c < 0.0:
        x_max = x_c
        f_max = f_c
    else:
        x_min = x_c
        f_min = f_c
    x_c = (x_min + x_max) / 2.0
    f_c = f(x_c)
#    print "Iteration ", iteration, " x ", x_c, " f ", f_c

print "The root is approximately ", x_c, " where f is ", f_c
