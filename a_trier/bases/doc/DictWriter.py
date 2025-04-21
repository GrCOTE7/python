import csv

en_tete = ["Nom", "Âge"]
data = [
    {"Nom": "Alice", "Âge": "25"},
    {"Nom": "Bob", "Âge": "30"},
    {"Nom": "Charlie", "Âge": "35"},
]

filename = "data.csv"

with open(filename, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=en_tete, delimiter=",")
    writer.writeheader()  # Écrit les en-têtes dans le fichier CSV
    for row in data:
        writer.writerow(row)

print(f"Le fichier CSV '{filename}' a été créé avec succès.")
