def approximate_integral(a, b, n, f):
    # Width of each subinterval
    delta_x = (b - a) / n

    # Initialize sum of function values at midpoints
    total_sum = 0

    # Loop through each subinterval
    for i in range(1, n + 1):
        # Calculate the midpoint of the i-th subinterval
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        
        # Add the function value at this midpoint
        total_sum += f(midpoint)

    # Return the approximation of the integral
    return total_sum * delta_x

# Define the function to integrate: f(x) = x^2 + 1
def my_function(x):
    return x**2 + 1

# Call the integration function with 1,000,000 subintervals
area = approximate_integral(a=0, b=1, n=1_000_000, f=my_function)

# Print the result
print(area)  # Expected output: very close to 4/3 = 1.333333...
