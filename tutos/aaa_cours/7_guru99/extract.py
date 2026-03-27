import csv
from pathlib import Path


def extract():
    """
    Extract data from Emissions.csv and show dict
    """
    print("Extraction...")

    data = []
    pathfile = Path(__file__).resolve().parent / "data_app" / "Emissions.csv"
    print(pathfile)
    # exit()
    with open(pathfile) as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            line = {key.strip(): value.strip() for key, value in line.items()}
            data.append(line)
    return data


if __name__ == "__main__":
    dict = extract()
    print(dict)
