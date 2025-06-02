from math import sqrt

# Number of pets each person owns
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values, is_sample: bool = False):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / (len(values) - (1 if is_sample else 0))
    return _variance

def std_dev(values, is_sample: bool = False):
    return sqrt(variance(values, is_sample))

print("VARIANCE = {}".format(variance(data, is_sample=True))) # 24.95238095238095
print("STD DEV = {}".format(std_dev(data, is_sample=True))) # 4.99523582550223

'''
🧠 KEY CONCEPTS
✅ Population vs. Sample
Population: You have all data points of interest (e.g., every person in the group).

Sample: You have a subset of the population and want to generalize.

Type	        Divisor in Variance Formula
Population	        n
Sample	           n - 1 (Bessel’s correction)

🔍 Your Code, Explained
1. variance() Function

def variance(values, is_sample: bool = False):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / (len(values) - (1 if is_sample else 0))
    return _variance
Takes an optional is_sample argument.

Calculates the mean of the values.

For each value:

Finds the squared difference from the mean.

Then divides by:

n for population,

n - 1 for sample (if is_sample=True).

💡 Smart use of a conditional expression in the denominator!


'''