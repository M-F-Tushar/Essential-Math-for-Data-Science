from sympy import *

x = symbols('x')
# declare function
z = (x**2 + 1)**3 - 2
dz_dx = diff(z, x)
print(dz_dx)
# 6*x*(x**2 + 1)**2

'''
This is the chain rule, which says that for a given function y (with input
variable x) composed into another function z (with input variable y), we can
find the derivative of z with respect to x by multiplying the two respective
derivatives together:
dz/dx = dz/dy * dy/dx
# In this case, we have:
dz/dy = 3*(y**2) 
dy/dx = 2*x
# So, dz/dx = 6*x*(x**2 + 1)**2
# This is a powerful technique in calculus that allows us to differentiate
composite functions efficiently.
# The output is the derivative of z with respect to x.

'''