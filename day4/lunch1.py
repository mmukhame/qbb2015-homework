#!/usr/bin/env python


"""
Count intersection of two BED files
"""

from __future__ import division
import sys
import numpy 


#initialize arrays
def arrays_from_len_file(fname):  
    arrays={}
    for line in open( fname):
        fields=line.split()
        name=fields[0]
        size=int(fields[1])
        arrays[name] = numpy.zeros(size, dtype=bool)
    return arrays

def set_bits_from_file(arrays, fname):
    for line in open (fname):
        fields=line.split()
        ##Parse fields
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        arrays[ chrom ][start:end] = 1 
    
#arr=arrays_from_len_file(sys.argv[1])
#set_bits_from_file(arr,sys.argv[2])


all_sums = {}
for f_name in sys.argv[2:]:
    arr=arrays_from_len_file(sys.argv[1])
    set_bits_from_file(arr,f_name)
    total = 0
    for key, value in arr.iteritems():
        total += numpy.sum(value)
    all_sums[f_name] = total

for key,value in all_sums.iteritems():
    print key, value
#print "Total: %d" % (numpy.sum(value))
    
"""
Regions bound to DM3_Kc_BEAF.bed: 5438204

Regions bound to DM3_Kc_CTCF.bed: 3204379

Regions bound to DM3_Kc_SuHW.bed 5970273

"""