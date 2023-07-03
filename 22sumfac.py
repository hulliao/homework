# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

n = 5 # use this value for your computation
s = 0
t = 1
for i in range(1,n+1):
    s +=i
    t = t * i
print(n,s,t)

# factorial would be 1 * 2 * 3 * 4 * 5
# use multiple variables

"""
python3 22sumfac.py
5 15 120
"""