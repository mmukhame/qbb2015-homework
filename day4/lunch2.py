#!/usr/bin/env python


"""
Count intersection of two BED files
"""

from __future__ import division
import sys
import copy
import numpy 
import matplotlib.pyplot as plt
import matplotlib_venn as venn3


#initialize arrays
def arrays_from_len_file(fname):  
    arrays={}
    for line in open( fname):
        fields=line.split()
        name=fields[0]
        size=int(fields[1])
        arrays[name] = numpy.zeros(size, dtype=bool)
    return arrays

def set_bits_from_file( arrays, fname ):
    for line in open( fname ):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        arrays[ chrom ][ start : end ] = 1


arr = arrays_from_len_file( sys.argv[1] )
set_bits_from_file( arr, sys.argv[2] )
#count number of elements that intersect

total=0 #keep track of total number of elements
any_overlap=0 #any overlap with region that is marked will be counted
all_overlap=0
half_overlap=0

for line in open(sys.argv[3]):
    fields=line.split()
    ##Parse fields
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    #Get slice
    sl=arr[chrom][start:end] 
    total +=1
    any_overlap += sl.any()
    all_overlap+= sl.all() 
    #half overlap
    half_overlap += (numpy.sum (sl)/len(sl)>0.5)
print "Total: %d , Any overlap: %d, All overlap: %d, Half overlap: %d" % (total, any_overlap, all_overlap, half_overlap)


"""
DM3_Kc_BEAF & DM3_Kc_SuHW.bed
/Users/cmdb/qbb2015-homework/day4 $ ./lunch2.py dm3.len DM3_Kc_BEAF.bed DM3_Kc_SuHW.bed
Total: 7972 , Any overlap: 1868, All overlap: 993, Half overlap: 1730



DM3_Kc_BEAF.bed & DM3_Kc_CTCF.bed
/Users/cmdb/qbb2015-homework/day4 $ ./lunch2.py dm3.len DM3_Kc_BEAF.bed DM3_Kc_CTCF.bed
Total: 5600 , Any overlap: 3192, All overlap: 2231, Half overlap: 3051



DM3_Kc_SuHW.bed & DM3_Kc_CTCF.bed
/Users/cmdb/qbb2015-homework/day4 $ ./lunch2.py dm3.len DM3_Kc_SuHW.bed DM3_Kc_CTCF.bed
Total: 5600 , Any overlap: 2354, All overlap: 1158, Half overlap: 2248

DM3_Kc_SuHW.bed & DM3_Kc_BEAF.bed
/Users/cmdb/qbb2015-homework/day4 $ ./lunch2.py dm3.len DM3_Kc_SuHW.bed DM3_Kc_BEAF.bed
Total: 6135 , Any overlap: 1782, All overlap: 246, Half overlap: 1341

DM3_Kc_CTCF.bed & DM3_Kc_BEAF.bed
/Users/cmdb/qbb2015-homework/day4 $ ./lunch2.py dm3.len DM3_Kc_CTCF.bed DM3_Kc_BEAF.bed
Total: 6135 , Any overlap: 2999, All overlap: 413, Half overlap: 2102



DM3_Kc_CTCF.bed & DM3_Kc_SuHW.bed
/Users/cmdb/qbb2015-homework/day4 $ ./lunch2.py dm3.len DM3_Kc_CTCF.bed DM3_Kc_SuHW.bed
Total: 7972 , Any overlap: 2346, All overlap: 493, Half overlap: 2095

"""


plt.figure()
venn3(subsets=(5438204,3204379,3,4,5,6,7), set_labels=('Set1', 'Set2', 'Set3','Set4', 'Set5', 'Set6', 'Set7'))
plt.title("Histogram of FPKM values in SRR072893")
plt.xlabel("log(FPKM values)")
plt.savefig("Venndiagram.png")



