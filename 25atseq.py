# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random

seq = ''
s = 0
length = 30
for i in range(length):
    a = random.random()
    if a >= 0.4: seq += random.choice('AT')
    else:   seq += random.choice('GC')
    p = seq[i]
    if p == 'A' or p == 'T': s += 1
per = s / length
print('30', per, seq)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
