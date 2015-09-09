#!/usr/bin/env python

"""
Parse a singe FASTA record from stdin and print it.
"""

import sys
from fasta import FASTAReader

sequence_name={}
ratio_iden=[]

for line in open(sys.argv[1]):
    line1=line.split()
    print line1
    if line1==[]:
        pass
    elif line1[0]==">":
        print line  
    if line.startswith(" Iden"):
        print line    #print ratio
 