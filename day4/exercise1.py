#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division

import matplotlib.pyplot as plt
import sys
import numpy
import copy
from matplotlib_venn import venn3, venn3_circles


def arrays_from_len_file( fname ):
    arrays = {}
    for line in open( fname ):
        fields = line.split()
        name = fields[0]
        size = int( fields[1] )
        arrays[name] = numpy.zeros( size, dtype=bool )
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
arr2=copy.deepcopy(arr) 
arr3=copy.deepcopy(arr) 

set_bits_from_file(arr, sys.argv[2])
set_bits_from_file(arr2, sys.argv[3])
set_bits_from_file(arr3, sys.argv[4])

count_Abc=0
count_aBc=0
count_abC=0
count_ABc=0
count_aBC=0
count_AbC=0
count_ABC=0


for filename in sys.argv[2:]:
    for line in open( filename ):
        fields = line.split()
    #   Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
    #   Get slice
        sl = arr[chrom][start:end]
        sl1=arr2[chrom][start:end]
        sl2=arr3[chrom][start:end]
    #    # Aggregate
        if sl.any() and not (sl1.any() or sl2.any()):
            count_Abc +=1
        if sl1.any() and not (sl.any() or sl2.any()):
            count_aBc +=1
        if sl2.any() and not (sl.any() or sl1.any()):
            count_abC +=1
        if sl.any() and sl1.any() and not sl2.any():
            count_ABc +=1
        if sl1.any() and sl2.any() and not sl.any():
            count_aBC +=1
        if sl.any() and sl2.any() and not sl1.any():
            count_AbC +=1
        if sl.any() and sl1.any() and sl2.any():
            count_ABC +=1
                
    
print "Abc: %d, aBc: %d, abC: %d, ABc: %d, aBC: %d, AbC: %d, ABC: %d" % ( count_Abc, count_aBc, count_abC, count_ABc, count_aBC, count_AbC, count_ABC)

plt.figure()
venn3(subsets=(count_Abc, count_aBc, count_abC, count_ABc, count_aBC, count_AbC, count_ABC), set_labels=('Set1', 'Set2', 'Set3', 'Set4', 'Set5', 'Set6', 'Set7'))
plt.savefig("Venndiagram.png")






#arr2=copy.deepcopy(arr)


