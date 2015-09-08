#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/SRR.sam"

f=open(filename)

line_count = 0
line_count1 = 0
line_count2 = 0
line_count3 = 0
line_count4 = 0
line_count5 = 0

#Iterate the file line by line searching to chromosome 2L
for line, data in enumerate(f):
    fields=data.split()
    gene=fields[2] #grabbing all the chromosomes
    if gene == "2L": 
        line_count+=1
    if gene == "2R":
        line_count1+=1
    if gene == "3L":
        line_count2 += 1
    if gene == "3R":
        line_count3+=1
    if gene == "4":
        line_count4 +=1
    if gene == "X":
        line_count5+=1
#print line_count
#print line_count1
#print line_count2
#print line_count3
#print line_count4
#print line_count5
print "2L has %d, 2R has %d, 3L has %d, 3R has %d, 4 has %s, X has %d" % (line_count, line_count1, line_count2, line_count3, line_count4, line_count5)
