'''
The mode is the most frequently occurring set of values. It primarily becomes
useful when your data is repetitive and you want to find which values occur the
most frequently.
When no value occurs more than once, there is no mode. When two values occur
with an equal amount of frequency, then the dataset is considered bimodal.

'''

# Number of pets each person owns
from collections import defaultdict

sample = [1, 3, 2, 5, 7, 0, 2, 3]

def mode(values):
    counts = defaultdict(lambda: 0)
    for s in values:
        counts[s] += 1
    max_count = max(counts.values())
    modes = [v for v in set(values) if counts[v] == max_count]
    return modes
print(mode(sample)) # [2, 3]

'''
✅ Sample Data

sample = [1, 3, 2, 5, 7, 0, 2, 3]
This is a list of the number of pets different people own.

✅ Import and Setup

from collections import defaultdict
defaultdict is like a regular Python dictionary, but with a default value.

In this case, every key will start with a value of 0.

✅ Define the mode() Function

def mode(values):
Defines a function called mode that accepts a list of numbers.

🧮 Step 1: Count the Frequency of Each Value
e
    counts = defaultdict(lambda: 0)
This sets up a dictionary called counts where each key (a number in the list) starts at 0.

    for s in values:
        counts[s] += 1
For each number s in the list values, increment its count by 1.

After this loop runs, counts will look like:

{1: 1, 3: 2, 2: 2, 5: 1, 7: 1, 0: 1}
🔍 Step 2: Find the Highest Frequency

    max_count = max(counts.values())
Finds the maximum value among all frequencies.

Here: max_count = 2 because both 2 and 3 appear twice, more than any other number.

🧩 Step 3: Collect All Values That Match the Max Count

    modes = [v for v in set(values) if counts[v] == max_count]
Creates a list of values that appear as frequently as max_count.

set(values) ensures each number is only checked once.

The result here is:

[2, 3]
Both 2 and 3 are modes.

✅ Step 4: Return the Result

    return modes
🖨️ Final Line

print(mode(sample))  # [2, 3]
'''