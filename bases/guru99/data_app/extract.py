import csv


def extract():
    """
    Extract data from Emissions.csv and show dict
    """
    print("Extraction...")
    
    data=[]
    with open("Emissions.csv") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            line = {key.strip(): value.strip() for key, value in line.items()}
            data.append(line)

    return data


if __name__ == "__main__":
    dict = extract()
    print(dict)

