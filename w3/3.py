import zipfile
import os
from pathlib import Path

def write_array(arr, file):
	arr = map(lambda x : x+'\n', arr)
	file.writelines(arr)

with zipfile.ZipFile("main.zip", "r") as zip1:
	zip1.extractall("main")

p = Path("main")
files = list(p.glob('**/*.py'))
X = set()

for path in files:
	X.add(path.parts[-2])

Xlist = sorted(list(X))

with open("3.txt", "w") as F:
	write_array(Xlist, F)
with open("3.txt", "r") as F:
	for line in F:
		print(line.strip())
