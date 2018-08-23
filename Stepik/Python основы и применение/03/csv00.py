import csv

with open("example00.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)