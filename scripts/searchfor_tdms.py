import os
import pickle

path = os.getcwd()
tdms_files = []

for subdir, dirs, files in os.walk(path):
    for file in files:
        if '.tdms' in file:
            tdms_files.append(os.path.join(subdir, file))

# print(tdms_files)

# Save list of tdms file dir

with open('tdms_dir.p', 'wb') as output:
    pickle.dump(tdms_files, output)
    # for line in tdms_files:
    #     output.write(line + "\n")
