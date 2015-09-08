#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation, comment ='#', header = None)

#print df 

#print df.head()


#print df.describe()
#print df.info()


#Pulling out specific rows with the use of square brackets
#print "\nthis is what happens with [0:5]\n"
#print df[1:5] #the end number is not inclusive, prints four. prints rows 1 thru 4

#print "\nthis is what happens with [0:5]\n"
#print df[0:5]


#show rows 10 through 15 (1-based, inclusive)
#print df[9:15]


#show rows 20 through 25
#print df[19:25]

#subsetting columns
#print df.info()

#we are going to name the columns with the use of list
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attribuates"]
#print df.info ()


#you can sort based on columns
#print df.sort("type", ascending=False)



#print df["chromosome"]

#extract three columns: chromosome, start, end 

#print df[["chromosome", "start", "end"]]

#subsetting by rows and columns
#print df["start"][1:7] 


#print df.shape #tells us how many rows and columns
df2 = df["start"]
#print df2.shape


#command to save
df2.to_csv("startColumn.txt", sep='\t', index=False)

#Filter based on individual value in a columnc
#do not need to split, will be using Boolean indexing and Boolean fixing...true or false

#subset: 5000 rows, and dont want this row, want this one, dont want this one. Need 5000 true and falses
#want to find features for a value less than 10 start position

#print df.shape
roi = df["start"] < 10
#print roi.shape
#print df[roi]
print df[roi].shape


