import csv
import pandas
import numpy as np


def csvrd(file):
	with open(file, "r") as F:
		reader = csv.reader(F)
		for row in reader:
			print(row)

df = pandas.read_csv('table.csv', sep = ';', header = None)
df_out = pandas.DataFrame(np.insert(df.values, int(len(df) / 2), values = [-200, -200, -200, -200], axis = 0))
df_out.to_csv('middle_row.csv', index = False, header = 0)

csvrd('table.csv')
