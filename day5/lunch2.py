#!/usr/bin/env python

"""
Parse a singe FASTA record from stdin and print it.
"""
#Create a histogram of the alignment scores and e-values and a scatterplot relating the two


import sys
import matplotlib.pyplot as plt

scores=[]
values=[]

for lines in open(sys.argv[1]): #do not open every single line, but find a way to only open wanted lines
    line1=lines.split()
    score1=float(line1[10])
    value1=float(line[11])
#print score1
#print value1
    scores.append(score1)
    values.append(value1)
    print scores
    print values
    #if line.startswith(" Score"):
    #    print line    #print ratio