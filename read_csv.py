import csv

with open('file.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

