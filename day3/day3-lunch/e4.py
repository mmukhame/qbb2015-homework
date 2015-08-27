#!/usr/bin/env python

#working with dictionaries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data set1
df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2=df["FPKM"] > 0


#data set2
df4=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df5=df4["FPKM"] >0

b1=df2 & df5 #when they are both zero, a row will be true. Will be false when one of them or both are false. Ensures the same shape

df3=df[b1]["FPKM"] 
df6=df4[b1]["FPKM"]

l1=np.log2(df3) #rows that are true in both 
l2=np.log2(df6)


M=l1-l2 #ratio of intensity (log based)
A=(df5+df6)*0.5

print M
print A

plt.figure()
plt.scatter(M, A)
plt.title("MA Plot")
plt.ylabel("ratio")
plt.xlabel("average")
plt.savefig("MAplot.png")

