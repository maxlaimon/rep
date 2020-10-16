import csv


with open('table.csv', 'r') as table:
    reader = list(csv.reader(table))
    reader1 = reader[len(reader)//2:]
    reader = reader[:len(reader)//2]
    reader.append(['-200;-200;-200;-200'])
with open('table.csv', 'w') as table:
    writer = csv.writer(table)
    writer.writerows(reader+reader1)
