# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:41:16 2019

@author: PI
"""

import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

datafiles= glob.glob("data/*.csv")

dataframes = dict()

for f in datafiles:
    #parse currency pair name from the file name
    commodity_name = f.split(os.path.sep)[-1].split('.')[0]
    # Using read_csv function read file into a DataFrame 'df'.

    # reading only two columns from each file: 'date', and 'close'. 
    # 'date' will be used to index each record in data frame, and the close price will be used to  calculate correlations. 
    df = pd.read_csv(f, sep=',', header=0, index_col=["Date"], usecols=["Date", "Close"])
    # rename 'close' column the the currency pair name pair.
    df.columns = [commodity_name]
    
    # read each of files into a pandas data frame.
    dataframes[commodity_name] = df

# join all data frames create above into a single 'final_df' data frame. 
final_df = None
for k,v in dataframes.items():
    if (final_df is None):
        final_df = v
    else:
        final_df = final_df.join(v, how='left')
        
print("--------------- FINAL DATA FRAME (10 Lines) ---------------")
print(final_df.head(10))

# Correlation Calculation
corr_df = final_df.corr(method='pearson')
print("--------------- CORRELATIONS ---------------")
print(corr_df.head(len(dataframes)))

print("--------------- CREATE A HEATMAP ---------------")
# create mask to display only the lower triangle of the matrix (since it's mirrored around its 
# top-left to bottom-right diagonal).
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True

# create the heatmap using seaborn library. 
seaborn.heatmap(corr_df, cmap='RdYlGn_r', vmax=1.0, vmin=-1.0 , mask = mask, linewidths=2.5)

# plot heatmap
plt.yticks(rotation=0) 
plt.xticks(rotation=90) 
plt.show()