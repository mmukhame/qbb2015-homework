#!/usr/bin/env python

#working with dictionaries
import pandas as pd
import matplotlib.pyplot as plt

metadata=pd.read_csv("~/qbb2015/rawdata/samples.csv")
Sxl=[]
for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df=pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi=df["t_name"].str.contains("FBtr0331261") #grab the row interested in 
    Sxl.append(df[roi]["FPKM"].values) #want number, store in the list Sxl
 #pulls out female, and sample column
Sxlm=[]
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df1=pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi1=df["t_name"].str.contains("FBtr0331261") #grab the row interested in 
    Sxlm.append(df1[roi1]["FPKM"].values)
#pass to plot with three commands

plt.figure()
plt.title("Sxl")
plt.xlabel("developmental stage")
plt.ylabel("mRNA Abundance (RPKM)")
plt.plot(Sxl, color = 'r', label='female')
plt.plot(Sxlm, color = 'b', label = 'male')
plt.legend(['female', 'male'])
xticks=['10', '11', '12', '13', '14A', '14B', '14C', '14D']
plt.xticks (range(8), xticks)
plt.yticks(range(0,350,50))
plt.savefig("Exercise1.png")


