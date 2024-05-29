import csv

headers = ["Name", "Age"]
data = [
    ("Alice", 50),
    ("Bob", 60),
    ("Charlie", 70),
]

filename = "data.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(headers)
    for row in data:
        writer.writerow(row)
