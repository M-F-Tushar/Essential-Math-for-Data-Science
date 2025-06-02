from sympy import *

# Declare variables to SymPy
x, i, n = symbols('x i n')

# Declare function and range
f = x**2 + 1
lower, upper = 0, 1

# Calculate width and each rectangle height at index "i"
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)

# Iterate all "n" rectangles and sum their areas
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()
# Calculate the area by approaching the number
# of rectangles "n" to infinity
area = limit(n_rectangles, n, oo)
print(area) # prints 4/3

'''
We want to find the area under the curve of the function x^2 + 1 between 0 and 1. This area is exactly the integral of the function over that range.

Instead of calculating the integral directly, we break the area into many thin rectangles and add up their areas. The more rectangles we use, the closer we get to the true area.

We represent these rectangles symbolically using variables:

n is the number of rectangles (we’ll imagine making this number really big).

i counts which rectangle we’re looking at.

delta_x is the width of each rectangle.

x_i is the position along the x-axis at the right edge of the i-th rectangle.

For each rectangle, we calculate its height by plugging x_i into the function x^2 + 1.

The area of each rectangle is its height times its width: delta_x times f(x_i).

We add up the areas of all rectangles from i=1 up to i=n to get an approximate total area.

Finally, we imagine making the rectangles infinitely thin by letting n (the number of rectangles) grow towards infinity.

Taking this limit gives the exact area under the curve, which your program calculates symbolically and prints as 4/3.
'''