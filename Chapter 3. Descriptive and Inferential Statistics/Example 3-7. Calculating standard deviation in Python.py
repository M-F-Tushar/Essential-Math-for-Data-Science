''''
The standard deviation is the square root of the variance. It gives you a measure of how spread out the values are, but in the same units as the data itself (unlike variance, which is in squared units).
'''
from math import sqrt

# Number of pets each person owns
data = [0, 1, 5, 7, 9, 10, 14]
def variance(values):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / len(values)
    return _variance

def std_dev(values):
    return sqrt(variance(values))

print(std_dev(data)) # prints 4.624689730353898