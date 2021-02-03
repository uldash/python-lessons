import json

with open("students.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"]))