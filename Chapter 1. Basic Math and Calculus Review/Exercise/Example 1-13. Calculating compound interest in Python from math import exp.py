'''
Let’s say you loan $100 to somebody with 20% interest annually. Typically, interest will be
compounded monthly, so the interest each month would be .20/12 =. 01666. How much will the 
loan balance be after two years? To keep it simple, let’s assume the loan does not require payments (and no
payments are made) until the end of those two years.

we can come up with a formula to calculate
interest. It consists of a balance A for a starting investment P, interest rate r,
time span t (number of years), and periods n (number of months in each
year).
 Here is the formula:
 A = P * (1 + (r / n)) ** (n * t)

'''


from math import exp

p = 100
r = 0.20
t = 2.0
n = 12

a = p * (1 + (r / n)) ** (n * t)

print(a)