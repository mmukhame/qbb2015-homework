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
            counts[kmer]=[ (ident,i )] #list contains the start location of the kamer. The first time you see it, and initialize that list with an i. I is the location where the current location is of the sequence, 
        else:
            counts[kmer].append((ident, i))
            
query=sys.argv[1]
#finding a match between kmers and dictionary
for i in range(0,len(query)-k): #looking at kamers at query sequence, rather than the target sequence
    kmer=query[i:i+k]
    if kmer in counts:
        
        matches=counts[kmer]
        for ident, pos in matches:
            print i, pos, ident
        
        
        

