import csv

students = [["Greg", "Dean", 70, 80, 90, 'Good job, Greg'],
            ["Wirt", "Wood", 80, 80.2, 80, 'Nicely done']]

with open("example00.csv", "a", newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for student in students:
        writer.writerow(student)
    writer.writerows(students)