
## Worksheet 1

import numpy as np
import numpy.linalg as la

# The first worksheet covers basic topics in linear algebra. There is also a basic question on nonlinear root-finding.

#### Answer Coding Question 3

def MatrixConditionCheck(A, MaxConditionNumber = 10.0):
    """Check the condition number of a matrix.
    Only write output to screen if the condition number is too high.
    Should return something, really."""

    ConditionNumber = la.cond(A)
    if ConditionNumber > MaxConditionNumber:
        print("The condition number of the matrix\n{0}\n"\
              "is too large (i.e., it is {1:.4} which is larger"\
              " than {2:.4}).\n".\
              format(A, ConditionNumber, MaxConditionNumber))
        
    
#### Answer Coding Question 4

def bisection(f, interval, tolerance = 1.e-10):
    """General bisection method for a function f of one variable.     
    There must be at least one root within the interval.     
    Default tolerance (width of the interval) is 1e-10."""
    
    assert len(interval) == 2
    
    # Get the endpoints of the interval
    [x_min, x_max] = interval
    
    # Values at the ends of the domain
    f_min = f(x_min)
    f_max = f(x_max)
    
    # Check that at least one root lies within the interval
    assert(f_min * f_max < 0.0)
    
    # The loop
    x_c = (x_min + x_max) / 2.0
    f_c = f(x_c)
    iteration = 0
    while ((x_max - x_min > tolerance) and \
               (np.abs(f_c) > tolerance) and \
               (iteration < 100)):
        iteration = iteration+1    
        if f_min * f_c < 0.0:
            x_max = x_c
            f_max = f_c
        else:
            x_min = x_c
            f_min = f_c
        x_c = (x_min + x_max) / 2.0
        f_c = f(x_c)

    print("The root is approximately {0} where "\
          "f is {1:.4} (tolerance {2:.4})".format(x_c, f_c, tolerance))
    return x_c

# Now define the function whose root is to be found
def fn_worksheet1_q4(x):
    """Simple function defined in question, f(x) = tan(x) - exp(-x)."""
    
    return np.tan(x) - np.exp(-x)
