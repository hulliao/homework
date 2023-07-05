# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

# How to reverse DNA sequence?
# I want the sequence to print in the reverse direction
# I also want the sequence to print the opposite base pair

dna = 'ACTGAAAAAAAAAAA'
seq = ''
for i in range(len(dna)):
    base = dna[i]
    if base == 'A': seq += 'T'
    elif base == 'T': seq += 'A'
    elif base == 'C': seq += 'G'
    else: seq += 'C'
print(seq[::-1])


a = ("abcdefgh") # testing different method
x = slice(1, 5, 2)
print(a[x])

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
