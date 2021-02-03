import csv

pt = dict()
with open("Crimes.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=",")
    for line in reader:
        if "2015" in line["Date"]:
            i = pt.setdefault(line["Primary Type"], 0)
            pt.update({line["Primary Type"]: i + 1})
print(max(pt, key=lambda x: pt[x]))
