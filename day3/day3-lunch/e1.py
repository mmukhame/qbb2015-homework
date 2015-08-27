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
    roi1=df["t_name"].str.contains("FBtr0331261") 
    Sxlm.append(df1[roi1]["FPKM"].values)
#import points that you want to graph. First will be males and second is female.
metadata=pd.read_csv("~/qbb2015/rawdata/replicates.csv")
Sx1=[]
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df2=pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi2=df2["t_name"].str.contains("FBtr0331261") 
    Sx1.append(df2[roi2]["FPKM"].values)
    
print Sx1
#[14A, 0], [14B, 0], [14C, 0], [14D, 0]) Males do not have a lethal sex gene   
Sx2=[]
for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df2=pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi2=df2["t_name"].str.contains("FBtr0331261") 
    Sx2.append(df2[roi2]["FPKM"].values)
    
print Sx2

#[14A, 0], [14B, 79.103477], [14C, 182.233475], [14D, 2.409474])

    

plt.figure()
plt.title("Sxl")
plt.xlabel("developmental stage")
plt.ylabel("mRNA Abundance (RPKM)")
plt.plot(Sxl, color = 'r', label='female')
plt.plot(Sxlm, color = 'b', label = 'male')
plt.legend(['female', 'male'], loc='center left')
xticks=['10', '11', '12', '13', '14A', '14B', '14C', '14D']


plt.plot(4, 0, 'o', color='r')
plt.plot(5, 79.103477, 'o', color ='r')
plt.plot(6, 182.233475, 'o', color = 'r')
plt.plot(7, 2.409474, 'o', color = 'r')


plt.plot(4, 0, 'o', color='b')
plt.plot(5, 0, 'o', color ='b')
plt.plot(6, 0, 'o', color = 'b')
plt.plot(7, 0, 'o', color = 'b')

plt.xticks (range(8), xticks)
plt.yticks(range(0,350,50))
plt.savefig("Exercise1.png")




