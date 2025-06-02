from sympy import *

x, y = symbols('x y')

# derivative for first function
# need to underscore y to prevent variable clash
_y = x**2 + 1
dy_dx = diff(_y)

# derivative for second function
z = y**3 - 2
dz_dy = diff(z)

# Calculate derivative with and without
# chain rule, substitute y function
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))

# Prove chain rule by showing both are equal
print(dz_dx_chain) # 6*x*(x**2 + 1)**2
print(dz_dx_no_chain) # 6*x*(x**2 + 1)**2


'''

```python
from sympy import *
```

* **Imports** everything from SymPy.
* Required for symbolic computation (e.g., `symbols`, `diff`, `subs`).

---

```python
x, y = symbols('x y')
```

* Declares `x` and `y` as **symbolic variables**.
* `x` is the independent variable.
* `y` is used to construct a function of `x` for testing the chain rule.

---

```python
# derivative for first function
# need to underscore y to prevent variable clash
_y = x**2 + 1
dy_dx = diff(_y)
```

* Defines y = x^2 + 1 and names it `_y` to avoid name conflict with the `y` symbol.
* `diff(_y)` computes \frac{dy}{dx} = \frac{d}{dx}(x^2 + 1) = 2x

---

```python
# derivative for second function
z = y**3 - 2
dz_dy = diff(z)
```

* Defines $z = y^3 - 2$
* Computes the derivative of $z$ **with respect to** $y$:

  \frac{dz}{dy} = 3y^2


---

```python
# Calculate derivative with and without
# chain rule, substitute y function
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
```

* Applies the **chain rule**:

  $$
  \frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx}
  $$
* Substitutes $y = x^2 + 1$ after multiplying.
* $\frac{dz}{dx} = 3y^2 \cdot 2x \rightarrow 6x(x^2 + 1)^2$

---

```python
dz_dx_no_chain = diff(z.subs(y, _y))
```

* **Directly differentiates** $z = (x^2 + 1)^3 - 2$ with respect to $x$.
* This bypasses the chain rule, and SymPy does all the work:

  $$
  \frac{d}{dx}((x^2 + 1)^3 - 2) = 6x(x^2 + 1)^2
  $$

---

```python
# Prove chain rule by showing both are equal
print(dz_dx_chain)       # 6*x*(x**2 + 1)**2
print(dz_dx_no_chain)    # 6*x*(x**2 + 1)**2
```

* Prints both results to show they are **identical**.
* ✅ Confirms that the **chain rule works** symbolically.

---

### ✅ Output:

```plaintext
6*x*(x**2 + 1)**2
6*x*(x**2 + 1)**2
```

---

### Summary:

| Step                                                            | Meaning                      |
| --------------------------------------------------------------- | ---------------------------- |
| `dy_dx = d/dx(x² + 1)`                                          | Inner function derivative    |
| `dz_dy = d/dy(y³ − 2)`                                          | Outer function derivative    |
| Chain rule: $\frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx}$ | Multiplied and substituted   |
| Direct differentiation                                          | Bypasses symbolic chain rule |
| Comparison                                                      | Confirms they’re equal ✅     |

Let me know if you’d like to extend this to multivariable functions or implicit differentiation!

'''