import os 

sourceDir = os.path.dirname(__file__)

f = open(os.path.join(sourceDir,"Popular_Baby_Names.csv"))
f.readline()
names = set()

for line in f:
    data = line.strip().split(",")
    names.add(data[3])
print(sorted(names))