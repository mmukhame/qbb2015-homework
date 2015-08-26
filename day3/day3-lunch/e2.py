#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2=df[df["FPKM"] > 0]["FPKM"]

df3=np.log(df2)
print df3

df4=df3.values

plt.figure()
plt.hist(df4)
plt.title("Histogram of FPKM values in SRR072893")
plt.xlabel("log(FPKM values)")
plt.savefig("histogram.png")

