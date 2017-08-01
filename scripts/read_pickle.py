import pickle

with open('tdms_dir.p', 'rb') as f:
    data = pickle.load(f)

print(data)