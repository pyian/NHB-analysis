
# coding: utf-8

import importTdms
import os
import pickle

path = os.getcwd()

tdms_dir = []

# loop through all files in cwd

for subdir, dirs, files in os.walk(path):
    for file in files:
        if file[-5:] == '.tdms':
            tdms_dir.append(os.path.join(subdir, file))

# save tdms_dir log as pickle

with open('tdms-dir.p', 'wb') as output:
    pickle.dump(tdms_dir, output)

print('Total number of tdms files: {}'.format(len(tdms_dir)))

file_name = []

for path in tdms_dir:
    file_name.append(importTdms.to_pd(path))

df_dir = []
for name in file_name:
    df_dir.append(os.getcwd() + '\\' + name)

# # save df_dir log as pickle

with open('df-dir.p', 'wb') as output:
    pickle.dump(df_dir, output)

print('DONE')
