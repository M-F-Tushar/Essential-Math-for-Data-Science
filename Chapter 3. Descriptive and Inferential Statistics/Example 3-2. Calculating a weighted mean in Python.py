# Three exams of .20 weight each and final exam of .40 weight
sample = [90, 80, 63, 87]

weights = [.20, .20, .20, .40]

weighted_mean = sum(s * w for s,w in zip(sample, weights)) / sum(weights) 

print(weighted_mean) # prints 81.4

'''
🔍 Step-by-Step Explanation:
zip(sample, weights)
Pairs each score with its corresponding weight:

[(90, 0.20), (80, 0.20), (63, 0.20), (87, 0.40)]
s * w for s, w in zip(...)
Multiplies each score s by its weight w:

[18.0, 16.0, 12.6, 34.8]
sum(...)
Sums up the weighted scores:

18.0 + 16.0 + 12.6 + 34.8 = 81.4
sum(weights)
Adds up the weights:

0.20 + 0.20 + 0.20 + 0.40 = 1.0
Division:
Divides the weighted score total by the total weight:

81.4 / 1.0 = 81.4

'''