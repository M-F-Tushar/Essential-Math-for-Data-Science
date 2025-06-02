from sympy import *
# This script demonstrates how to use the `sympy` library to compute the
# "x" and step size "s" , Declare symbols
x, s = symbols('x s')

# declare fnction
f =  x**2

# slope between two points with gap "s"
# sustitude into rise over run formula
slope_f = (f.subs(x, x + s) - f) / ((x + s) - x)

# substitute 2 for x
slope_2 = slope_f.subs(x, 2)
# calculate slope at x = 2
# infinitely approach step size _s_ to 0
result = limit(slope_2, s, 0)
print(result) # 4

'''
breaking down what each line does and why it's there:

from sympy import *
Purpose: Imports everything from the sympy library.

sympy is a Python library for symbolic mathematics (like algebra, calculus, etc.).

You need it to define symbols, perform algebraic manipulations, and compute limits.

x, s = symbols('x s')
Purpose: Declares x and s as symbols (not variables with numerical values).

x is the input variable of the function.

s represents the step size or small change in x (used to compute the slope between two points).

f = x**2
Purpose: Defines the function f(x)=x2.

This is the function for which you're computing the slope (derivative).

slope_f = (f.subs(x, x + s) - f) / ((x + s) - x)
Purpose: Computes the difference quotient, which is the formula for the slope between two points:
f(x+s)−f(x)/s
​f.subs(x, x + s) means you're evaluating f(x+s), i.e., replacing x with x + s.

f is f(x), and (x + s) - x simplifies to s.

So this line computes:
(x+s)2 − x2/s

slope_2 = slope_f.subs(x, 2)
Purpose: Substitutes x = 2 into the difference quotient.

Now the slope is calculated specifically at 
x=2, so you're looking at:
(2+s)2−2**2/s

result = limit(slope_2, s, 0)
Purpose: Takes the limit as s→0.

This is the definition of the derivative of 
f(x) at x=2.

It simulates the slope of the tangent line by making the second point get infinitely close to the first.

print(result)  # 4
Purpose: Prints the final result.

The output is 4, which means the slope of the tangent to the curve 
f(x)=x**2 at x=2 is 4.

'''