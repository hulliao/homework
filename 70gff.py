# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import json
import sys
import gzip
import re

file = sys.argv[1]
gene = []
beg = []
end = []
strand = []

with gzip.open(file, 'rt') as fp:
    for line in fp.readlines():
        pat1 = '\s+ID=gene-\w+;\w+=\w+:\w+-\w+,\w+:\w+.\w+:\d+;\w+=\w+;\w+=Gene;(gene)=(\w+)\W' #gets the thrL, thrA, etc
        match1 = re.search(pat1, line)
        if match1: gene.append(match1.group(2)) #the thrL and thrA are in a list now
        
        pat2 = 'NC_000913.3\s+RefSeq\s+gene\s+(\d+)\s+(\d+)\s+.\s+(\W)\s+'
        match2 = re.search(pat2, line)
        if match2: 
            beg.append(match2.group(1)) #the beg coordinates are in a list now
            end.append(match2.group(2)) #the end coordinates are in a list now
            strand.append(match2.group(3)) #the strand is in a list now

for i in range(len(gene)):
    sheet = [
        {"gene": gene[i], "beg": beg[i], "end": end[i], "strand": strand[i]}
    ]    
    print(json.dumps(sheet, indent=4))

'''
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
'''