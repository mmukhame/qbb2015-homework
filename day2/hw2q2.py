#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation, comment ='#', header = None)
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attribuates"]


#take a start position, gene one occurs at position 1, gene four occurs at position 400, and make a plot where they occur across a chromosome

roi = df["chromosome"].str.contains("Sxl")
roi2=df["type"].str.contains("transcript")

roi3=roi &  roi2
#genes are further apart at the top vs. genes that are more dense
#now we know thw rows interested in, we are going to use three commands to map on chromosome
#initialize the canvas 
plt.figure()
#actual plot, retrieve start values
plt.plot(df[roi3] ["start"])
plt.savefig("questiontwo.png")