# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import gzip
import sys
import re

file = sys.argv[1]
startcoor = []
endcoor = []
nts = ''
cod = {}

def oppodna(seq):
    basepairs = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    odna = [] #opposite strand of DNA
    rdna = [] #reverse strand of opposite DNA
    for nt in seq:
        odna.append(basepairs[nt]) #finding the opposite base pair for each nt in the sequence and adding them to the odna list
    odna2 = "".join(odna) #adding up all of the individual nts to get a cohesive sequence
    rdna = odna2[::-1] #reversing the odna sequence to get rdna
    return rdna

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp.readlines():
        pattern1 = '(CDS)\s+(\d+)\.\.\d+'
        pattern2 = '(CDS)\s+\w+\(\d+\.\.(\d+)'
        match1 = re.search(pattern1, line)
        match2 = re.search(pattern2, line)
        if match1: startcoor.append(match1.group(2))
        #want the last coordinate instead of first bc the complement DNA strand is the opposite base pairs and then reversed/back to front
        genpat1 = '\s+\d+\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)'
        match3 = re.search(genpat1, line)
        if match3:
            for i in range(1, 7):
                nts += match3.group(i) #now nts is a string of nt/a genome
        if match2: endcoor.append(len(nts) - int(match2.group(2)) +1)

nt = nts.upper()
negnt = oppodna(nt)

#+ strand
for j in startcoor: #remember its not range of startcoor so it starts from the first list item
    codon = nt[int(j)-1:int(j)+2] #-1 bc for example 190 in computer language is 191 actually so -1 to convert comp to actual
    if codon not in cod: cod[codon] = 0
    cod[codon] += 1

#- strand
for j in endcoor:
    codon = negnt[int(j)-1:int(j)+2]
    if codon not in cod: cod[codon] = 0
    cod[codon] += 1

for k, l in cod.items():
    print(k, l)

fp.close()

#create a pattern to identify the genes, create groups for each set of 10 genes
#add all groups to a string
#read through the string, go to each coordinate, go from where you left off (0-190, 190-300)
#find codon at coordinate

"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""