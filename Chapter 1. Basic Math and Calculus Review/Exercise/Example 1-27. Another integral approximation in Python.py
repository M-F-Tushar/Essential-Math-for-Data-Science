def approximate_integral(a, b, n, f):
    # Width of each subinterval
    delta_x = (b - a) / n
    
    # Initialize the total sum of f(midpoints)
    total_sum = 0
    
    # Loop over each subinterval
    for i in range(1, n + 1):
        # Calculate midpoint of the i-th subinterval
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        
        # Add the function value at the midpoint
        total_sum += f(midpoint)
    
    # Multiply the sum by the width to get the area approximation
    return total_sum * delta_x

# Function to integrate: f(x) = x^2 + 1
def my_function(x):
    return x**2 + 1

# Approximate the integral over [0, 1] with 1000 subintervals
area = approximate_integral(a=0, b=1, n=1000, f=my_function)

# Print the result
print(area)  # Expected ≈ 1.333333...
