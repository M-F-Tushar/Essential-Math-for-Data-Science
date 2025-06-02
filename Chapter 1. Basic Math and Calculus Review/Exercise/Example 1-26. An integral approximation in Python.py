def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0
    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)
    return total_sum * delta_x
def my_function(x):
    return x**2 + 1
area = approximate_integral(a=0, b=1, n=5, f=my_function)
print(area) # prints 1.33

'''
The arguments a
and b will specify the min and max of the x range, respectively. n will be
the number of rectangles to pack, and f will be the function we are
integrating. The function will return the approximate area under the
curve of the function f between a and b using the midpoint rule for numerical integration.
The midpoint rule is a method for approximating the integral of a function by
dividing the interval into n subintervals, calculating the midpoint of each
subinterval, evaluating the function at those midpoints, and summing the
results multiplied by the width of each subinterval.
The function my_function(x) is defined to return the value of the function
'''