#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd


#plot.style.use('ggplot')

data=pd.read_table( sys.stdin, names=["Scores"])
data["Scores"].hist()
plt.savefig( sys.argv[1] )