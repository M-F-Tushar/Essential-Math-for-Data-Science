# normal distribution, returns likelihood of a value
import math # We need access to math.pi (π) and math.exp() (exponential function) to implement the normal distribution formula.

def normal_pdf(x: float, mean: float, std_dev: float) -> float: # This line defines a function called normal_pdf: x: the value at which we evaluate the PDF.mean: the average (μ) of the distribution.std_dev: the standard deviation (σ), which determines the "width" of the bell curve.
    return (1.0 / ((2.0 * math.pi * std_dev ** 2) ** 0.5)) * \
           math.exp(-1.0 * ((x - mean) ** 2) / (2.0 * std_dev ** 2))
# Denominator Part: 1 / sqrt(2πσ²)
# Exponent Part: e^(-(x - μ)² / (2σ²))