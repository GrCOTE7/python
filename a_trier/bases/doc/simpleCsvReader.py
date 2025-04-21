import csv


def extract():
    data = []
    with open("data/persons.csv", mode="r") as file:
        print("Extract")
        csv_reader = csv.reader(file)
        for line in csv_reader:
            # line = {key.strip(): value.strip() for key, value in line}
            data.append(line)

    return data


def extractDico():
    data = []
    with open("data/persons.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            # line = {key.strip(): value.strip() for key, value in line.items()}
            data.append(line)

    return data


print(extract())
print(extractDico())
