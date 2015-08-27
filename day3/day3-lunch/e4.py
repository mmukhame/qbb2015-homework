#!/usr/bin/env python

#working with dictionaries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data set1
df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2=df[df["FPKM"] > 0]["FPKM"]
df3=np.log(df2).values


#data set2
df4=pd.read_csv("~/qbb2015/rawdata/samples.csv")
df5=df[df["FPKM"] > 0]["FPKM"]
df6=np.log(df5).values


M=df6-df5
A=(df5+df6)/2

print M
print A

plt.figure()
plt.scatter(M, A)
plt.ylabel("ratio")
plt.xlabel("average")
plt.savefig("MAplot.png")

