import csv

with open("example00.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)