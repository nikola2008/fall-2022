import os 

sourceDir = os.path.dirname(__file__)

f = open(os.path.join(sourceDir,"the-input.txt"))
count = 0
lines = f.readlines()
for line in lines:
    words = line.split(" ")
    count += len(words)
print(count)
f.close()