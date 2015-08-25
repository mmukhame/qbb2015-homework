#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation, comment ='#', header = None)
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attribuates"]


#take a start position, gene one occurs at position 1, gene four occurs at position 400, and make a plot where they occur across a chromosome

roi = df["chromosome"].str.contains("2L") #pulling out a chromosome column assuming you named is chromosome at top; look whether this row contains 2L
print df[roi].shape

#genes are further apart at the top vs. genes that are more dense
#now we know thw rows interested in, we are going to use three commands to map on chromosome
#initialize the canvas 
#plt.figure()
#actual plot, retrieve start values
#plt.plot(df[roi] ["start"])
#plt.savefig("starts2l.png")
#y is the position along the chromosome 
#x is the row number 


roi=df["chromosome"].str.contains("2R")

plt.figure()
plt.plot(df[roi]["start"])
plt.xlabel("gene")
plt.savefig("starts2R.png")

for chromosome in ("2L", "2R", "Y"):
	roi = df["chromosome"].str.contains(chromosome)
	
	
	plt.figure()
	plt.plot(df[roi]["start"])
	plt.title(chromosome)
	plt.ylabel("start position")
	plt.xlabel("gene")
	plt.savefig("starts"+chromosome + "png")




