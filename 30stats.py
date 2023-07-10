# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys
# python3 30stats.py 3 1 4 1 5

print('Count:', len(sys.argv) -1)

p = sys.argv[1:]
print('Minimum:', float(min(p)))

p = sys.argv[1:]
print('Maximum:', float(max(p)))

a = 0
for i in range(len(p)):
    a += float(p[i])
q = a / (len(sys.argv) -1)
print('Mean:', f'{q:.3f}')

r = []
for i in range(len(p)):
    b = float(p[i]) - q
    r.append(b ** 2)
t = (sum(r) / (len(p))) ** (1 / 2)
print(f'Std. dev: {t:.3f}')

u = (int((len(p) -1) / 2))
p.sort()
v = float(p[u])
print('Median', f'{v:.3f}')


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
