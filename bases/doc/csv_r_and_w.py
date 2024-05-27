import csv

with open("persons.csv", encoding="utf-8") as file_csv:
    reader = csv.DictReader(file_csv, delimiter=",")
    for line in reader:
        line = {key.strip(): value.strip() for key, value in line.items()}
        print(line)
