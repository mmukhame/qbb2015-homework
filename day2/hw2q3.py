#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"

df=pd.read_table(annotation, comment ='#', header = None)
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attribuates"]


#take a start position, gene one occurs at position 1, gene four occurs at position 400, and make a plot where they occur across a chromosome

roi = df["chromosome"].str.contains("Sxl") #pulling out a chromosome column assuming you named is chromosome at top; look whether this row contains Sxl
#print df[roi].shape

#genes are further apart at the top vs. genes that are more dense
#now we know thw rows interested in, we are going to use three commands to map on chromosome
#initialize the canvas 
plt.figure()
#actual plot, retrieve start values
plt.plot(df[roi] ["start"])
plt.savefig("starts2l.png")
#y is the position along the chromosome 
#x is the row number 
plt.title(Sxl subset) 
plt.ylabel("start position")
plt.xlabel("gene")

