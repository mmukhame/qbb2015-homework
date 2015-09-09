#!/usr/bin/env python

import sys
"""
Count kmers in fast file
"""

from fasta import FASTAReader

reader=FASTAReader(sys.stdin)
counts={}

k=11
#look at each sequence in the file; each kamer in the sequence with another for loop

#dictionary contains all the kamers
for ident, sequence in reader:
    for i in range(0, len(sequence)-k ):
        kmer=sequence[i:i+k] #will go from whatever you are in position and go to the next position 
        if kmer not in counts:
            counts[kmer]=1
        else:
            counts[kmer] +=1
            
#print kamers through a for loop. from least frequent to most frequent through a sorted 
for key in sorted(counts, key=counts.get):
    print key, counts[key]
        
        
        
        

