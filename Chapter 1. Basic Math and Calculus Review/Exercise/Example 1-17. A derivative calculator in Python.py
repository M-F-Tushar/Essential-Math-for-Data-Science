def derivative_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m

def my_function(x):
    return x**2 

slope_at_2 = derivative_x(my_function, 2, 0.0001)

print(slope_at_2)

'''
Explanation:
def derivative_x(f, x, step_size):

This defines a function named derivative_x.

Inputs:

f: a function you want to differentiate (passed as a variable).

x: the point at which you want to calculate the derivative.

step_size: a small number (often called h) that approximates how close you look to estimate the slope.

This method uses the forward difference formula to approximate the derivative:

f′(x)≈ f(x+h)−f(x)/h
​
m = (f(x + step_size) - f(x)) / ((x + step_size) - x)

This is the core formula to estimate the derivative.

It calculates the average rate of change between x and x + h.

Expanded:

f(x + step_size): the function value at a point just ahead of x.

f(x): the function value at the current point.

((x + step_size) - x): equals step_size, or h.

So m approximates the slope of the tangent at x.

return m

The result m, which is the estimated derivative at x, is returned.
def my_function(x):
    return x**2
Explanation:
This defines a specific function, here: 

f(x)=x 2.
The derivative of 
x 2 is 2x, so at 𝑥=2, the exact derivative is 4.

You’ll use this function to test your derivative_x function.


slope_at_2 = derivative_x(my_function, 2, 0.0001)
Explanation:
Calls derivative_x to compute the slope of my_function at x = 2.

Uses a small step size of 0.0001 for better accuracy.

Stores the result (approximated slope) in the variable slope_at_2.

print(slope_at_2)
Explanation:
Outputs the value of slope_at_2, which should be very close to 4, like 4.0001.
'''