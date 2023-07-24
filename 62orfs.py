# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

import mcb185
import sys
import argparse

file = sys.argv[1]
minsize = 300 #300 nucleotides in the open reading frame at minimum

def findorf(seq, rf): #input is the nucleotide sequence of the E.coli file, output is the coordinates 
#find M's and *'s (start and stop codons)
#bc the translate function converts nucleotides to amino acids, you need to x3 and +1 to get the nucleotide length and coordinates
    coor = {}
    first = False #using Booleans
    for i in range(len(seq)):
        if seq[i] == 'M' and first == False: #want this M to be the first M found/don't want 2 M's in a row which is why first = False
            firstcoor = i * 3 +rf +1
            #x3 to "convert" the amino acids to nucleotides quantity, +1 to convert computer (0,1,2) to human lang (1,2,3)
            #+rf to take into acc the nt before start codon bc rf is still significant in determining coordinates
            coor[firstcoor] = 0 #firstcoor:0 just to insert it in
            first = True #making first = True to indicate that first only = True after the first M is found
        if seq[i] == '*' and first == True: #making sure that an M was found before a * is counted (don't want a random *)
            lastcoor = i * 3 + 3 + rf #x3 and +rf same as firstcoor, +3 since there's 2 nt after the 1st stop nt and +1 to convert to human lang
            if lastcoor - firstcoor > minsize:
                coor[firstcoor] += lastcoor #changing the dictionary to be firstcoor:lastcoor
            else: del coor[firstcoor]
            first = False #changing first back to False to make sure the next M found is smth like M ... *, not MM ... * or *..MM
    return coor

#need to find opposite strand of DNA, then reverse that strand
def oppodna(seq):
    basepairs = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    odna = [] #opposite strand of DNA
    rdna = [] #reverse strand of opposite DNA
    for nt in seq:
        odna.append(basepairs[nt]) #finding the opposite base pair for each nt in the sequence and adding them to the odna list
    odna2 = "".join(odna) #adding up all of the individual nts to get a cohesive sequence
    rdna = odna2[::-1] #reversing the odna sequence to get rdna
    return rdna

#the + strand
for name, ntseq in mcb185.read_fasta(file):
    name2 = name.split()
    for i in range(3): #there are 3 total reading frames, i represnts the reading frame for the nucleotides at first
        aaseq = mcb185.translate(ntseq[i:]) #translating each reading frame so the 3 nucleotide sequences are converted to 3 amino acid sequences
        coordinates = findorf(aaseq, i)
        for first, last in coordinates.items():
            firstaa = int((first - i -1) / 3)
            #undoing what the findorf function did, converting the nt quantity to aa quantity to get the position of the amino acid at first coor
            ftenaa = aaseq[firstaa:firstaa+10]
            print(name2[0], first, last, '+', ftenaa) #i represents the reading frame for the amino acids now

#the - strand
for name, ntseq in mcb185.read_fasta(file):
    name2 = name.split()
    oppositentseq = oppodna(ntseq)
    for i in range(3):
        oppositeaaseq = mcb185.translate(oppositentseq[i:])
        coordinates = findorf(oppositeaaseq, i)
        for first, last in coordinates.items():
            firstaa = int((first - i -1) / 3)
            ftenaa = oppositeaaseq[firstaa:firstaa+10]
            print(name2[0], len(ntseq) - last +1, len(ntseq) - first +1, '-', ftenaa) #the coordinates are flipped around because the dna strand was reversed


#dictionary = {}
#list = []
#tuple = ()
#string = ''

"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz | sort -nk 2
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
