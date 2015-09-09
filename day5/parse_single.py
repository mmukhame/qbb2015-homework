#!/usr/bin/env python

"""
Parse a singe FASTA record from stdin and print it.
"""
import sys
from fasta import FASTAReader

         
reader=FASTAReader(sys.stdin)

#while 1:
#    print reader.next()

for ident, seq in reader: 
    print ident, seq
