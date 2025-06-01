# calculates continuous interest in Python using the exp() function.
from math import exp 
p = 100  # principal amount
r = 0.20 # annual interest rate
t = 2.0 # time in years

a = p *exp(r * t)

print(a)  # prints the final amount after continuous compounding interest

