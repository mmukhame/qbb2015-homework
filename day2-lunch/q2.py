#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/SRR.sam"

f=open(filename)
 

line_count=0
for line in f:
    if "NM:i:0" in line:
        line_count+=1
print line_count
 