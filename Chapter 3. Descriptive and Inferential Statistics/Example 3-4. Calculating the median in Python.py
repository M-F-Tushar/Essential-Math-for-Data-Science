# Number of pets each person owns
sample = [0, 1, 5, 7, 9, 10, 14]

def median(values):
    ordered = sorted(values)
    print(ordered)
    n = len(ordered)
    mid = int(n / 2) - 1 if n % 2 == 0 else int(n/2)
    if n % 2 == 0:
        return (ordered[mid] + ordered[mid+1]) / 2.0
    else:
        return ordered[mid]
print(median(sample)) # prints 7

'''
The median is the middlemost value in a set of ordered values. You sequentially
order the values, and the median will be the centermost value. If you have an
even number of values, you average the two centermost values. 

'''