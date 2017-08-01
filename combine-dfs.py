
# coding: utf-8

# Combine all data into a single df
# Save df as .p and .csv
# ===

import pandas as pd
import pickle

df_dir = pickle.load(open('df-dir.p', 'rb'))

# read all df.p
all_df = []
for df in df_dir:
    all_df.append(pd.read_pickle(df))

giant_df = pd.concat(all_df)

# Save the giant_df to all-df.p and csv

print('Writing to all-df.p')
giant_df.to_pickle('all-df.p')
print('Writing to all-df.csv')
giant_df.to_csv('all-df.csv')
print('pickle and csv format exported')
