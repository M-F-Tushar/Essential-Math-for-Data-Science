x = [1, 4, 6, 2]
n = len(x)
summation = sum(10*x[i] for i in range(0,n))
print(summation)

'''
Explanation:
x = [1, 4, 6, 2]
A list x is defined with 4 integers.

n = len(x)
Calculates the length of the list x, which is 4, and stores it in n.

sum(10*x[i] for i in range(0,n))
This is a generator expression that multiplies each element in x by 10 and then sums them up.
Here's the breakdown of the multiplication:

10 * x[0] = 10 * 1 = 10

10 * x[1] = 10 * 4 = 40

10 * x[2] = 10 * 6 = 60

10 * x[3] = 10 * 2 = 20

The sum is:
10 + 40 + 60 + 20 = 130

print(summation)
Outputs the result:

130
'''