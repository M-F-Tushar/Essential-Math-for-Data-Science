'''
This program calculates the variance, which is a measure of how spread out the numbers in a dataset are. A higher variance means the values are more spread out from the mean.
'''
# Number of pets each person owns
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / len(values)
    return _variance

print(variance(data)) # prints 21.387755102040813

'''
For each value v in values, it:

Subtracts the mean (v - mean)

Squares the result ((v - mean) ** 2)

Then it sums all those squared differences and divides by the number of values.

So, it’s computing the average of the squared distances from the mean.
'''asdf