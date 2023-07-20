# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import sys
import mcb185

file = sys.argv[1]
ksize = int(sys.argv[2]) #how long the kmer is (nucleotide sequence length)

def kmercount(seq):
    kmers = {} #creates a dictionary
    for i in range(len(seq) -ksize +1): 
    #+1 so that last value is included, -ksize so when i reaches the end of seq, it still has sequence after itself to use
        kmer = seq[i:i+ksize] #slices/reads a section of sequence (certain # of nucleotides) and/or where new nucleo. pairs are created
        if kmer not in kmers: kmers[kmer] = 1 
        #if a combination/pair of nucleotides (kmer) isn't in the kmers dictionary, add that new combo/kmer into the kmers dictionary as the key
        #and have 1 be the starting value for that (key:value so kmer:number)
        else: kmers[kmer] += 1
        #if the combo/kmer that just scanned is already a key in the kmers dictionary, +1 to the values side of the pair
    return kmers #we want the output to be the dictionary with the kmer pairs:number of times those pairs appeared

for name, sequence in mcb185.read_fasta(file): #mcb185 opens the E.coli file as a fasta file and opens E.coli so that the program can read/use it
    #name is words at the start of each line and the sequence is the combinations of nucleotides after the words (in file); unpacking a fasta file
    kmerct = kmercount(sequence) #putting the sequence from the E.coli file into the function to get the kmers dictionary
    for kmer, count in kmerct.items(): 
    #.items separates dictionary key:value pair into individual tuples in the (key, value) format;doing kmer, count unpacks each tuple so no commas/parentheses
        print(kmer, count)

"""
python3 61kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2 | sort
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
