import json

student1 = {
    "firs name": "Greg",
    "last name": "Dean",
    "certificate": True,
    "scores": [70, 80, 90],
    "description": "Good job, Greg"
}
student2 = {
    "firs name": "Wirt",
    "last name": "Wood",
    "certificate": True,
    "scores": [80, 80.2, 80],
    "description": "Nicely Done"
}

data = [student1, student2]
#print(json.dumps(data, indent=4, sort_keys=True))
with open("students.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
