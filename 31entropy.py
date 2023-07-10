# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import math
import sys
# python3 31entropy.py 0.1 0.2 0.3 0.4

p = sys.argv[1:]
H = []
for i in range(len(p)):
    q = float(p[i])
    a = q * math.log2(q)
    H.append(a)
print(f'{-sum(H):.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
