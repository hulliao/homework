# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

# to calculate the percent:
# its the number of G and C letters divided by the total letters in the dna sequence

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
s = 0
for i in range(len(dna)):
    p = dna[i] 
    if p == 'G' or p == 'C':
        s += 1
l = len(dna) 
ans = s / l
print(f'{ans:.2f}') 

"""
python3 24gc.py
0.42
"""
