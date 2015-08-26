#!/usr/bin/env python

#filename = "/Users/cmdb//qbb2015/stringtie/SRR072893/t_data.ctab"

import sys

#print sys.argv
#filename=sys.argv[1]
#f=open (filename)


# to loop over make
#for filename in sys.argv[1:6]
#for filename in sys.argv[1:] skip the first one, but consider all others as files



#for line in f:
 #   fields=line.split()
 #   if "tRNA" in fields[9]:
  #      print line,

#line_count=0
#Iterate the file line by line 
#for data in f:
 #   if line_count <=10:
 #       pass
 #   elif line_count <= 15:  #pass lines less than 10, print lines more than 15
 #       print data,
 #   else:
 #       break
 #   line_count+=1


f=sys.stdin #file handle objects. open readable file handle 
    
name_counts = {}
    
for line_count, data in enumerate(f):
    fields=data.split()
    gene_name=fields[9]
    if gene_name not in name_counts:
        name_counts[gene_name]=1
    else:
        name_counts[gene_name] += 1

#Iterate key, value pairs from the name counts dictionary
for key, value in name_counts.iteritems():
   #Print gene name and count
    print key, value
        


