from sympy import symbols, diff

x = symbols('x')

f = x**2           # symbolic expression
dx_f = diff(f, x)  # derivative: 2*x

print(dx_f.subs(x, 2))  # ✅ Output: 4
'''
✅ Code
from sympy import symbols, diff
🔹 What it does:
symbols: used to declare a variable (like declaring x as a symbol in math).

diff: used to compute the derivative of a symbolic expression.

x = symbols('x')
🔹 What it does:
Declares x as a symbolic variable, so you can write math like 
𝑥2 , sin(𝑥), etc.
Think of x here like a placeholder in an algebra equation.

f = x**2
🔹 What it does:
Defines 
𝑓(𝑥)=𝑥2 as a symbolic expression (not a Python function).

f now represents the math expression 𝑥2, and it can be manipulated algebraically.

dx_f = diff(f, x)
🔹 What it does:
Takes the derivative of 
𝑓 with respect to 𝑥, so:

𝑑𝑥(𝑥2)=2𝑥

dx_f now holds the symbolic expression 2*x.

print(dx_f.subs(x, 2))
🔹 What it does:
subs(x, 2) substitutes x with 2 in the symbolic derivative.

So it evaluates 
2𝑥 at 𝑥=2, which gives 2⋅2=4
The result printed is: 4


'''