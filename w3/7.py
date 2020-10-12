import pandas
import csv


def read_my_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

df2 = pandas.read_csv('table.csv', sep = ';', header = 0)
df2['my_col'] = [True for i in range(len(df2))]
df2.to_csv('new_col.csv', index = False)
read_my_csv("new_col.csv")
