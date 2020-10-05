import csv

def csvrd(file):
	with open(file, "r") as F:
		reader = csv.reader(F)
		for row in reader:
			print(row)

csvrd('table.csv')
