'''
Extract from the json files to know about the files
'''
import glob
import json
import os

files = glob.glob('./metadata/*.json')
f = open('./gf5b_all.txt', 'w')
names = []
for file in files:
    file = open(file, 'r')
    data = json.load(file)
    name = os.path.splitext(os.path.basename(data['datatranferfileurl']))[0]
    names.extend([name])

names = sorted(names)
for name in names:
    print(name)
    f.write(name)
    f.write('\n')
