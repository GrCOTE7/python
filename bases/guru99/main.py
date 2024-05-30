import csv

file = open("data_app/Emissions.csv", encoding="utf-8")

data=[]
csv_reader = csv.DictReader(file)
for line in csv_reader:
    line = {key.strip(): value.strip() for key, value in line.items()}
    data.append(line)

file.close()
print (file.closed)

print(data)

