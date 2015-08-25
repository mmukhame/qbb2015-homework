#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/SRR.sam"

f=open(filename)
line_count=0
for line in f:
    if line[0:3] == "SRR": 
        line_count+=1
        if line_count <=10:
            #fields=line.split()
            #print fields[2]
            print line.split()[4]
        


