import csv


with open('table.csv', 'r') as table:
    reader = list(csv.reader(table))
    reader[0][0] += ';my_col'
    for i in range (1, len(reader) - 1):
        reader[i][0] += ';True'
with open('table.csv', 'w') as table:
    writer = csv.writer(table)
    writer.writerows(reader)
