# how we can declare a mathematical function and iterate it in Python
# Take this simple linear function: y = 2x + 1

def f(x):
    return 2 * x + 1

x_values = [0, 1, 2, 3]

for x in x_values:
    y = f(x)
    print(y)

'''
A function takes input variables (also called
domain variables or independent variables), plugs them into an expression,
and then results in an output variable (also called dependent variable).

'''
