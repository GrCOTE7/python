import csv, os, sys

# sys.path.append("../../gc7/tools")
# sys.path.append("../../gc7/tools/file")
from file import get_data, get_caller_depth

print("Appelant:")
print(get_caller_depth())


get_data(123)


csv_path = "c:\\laragon\\www\\python\\bases\\doc\\data\\persons.csv"

# with open(csv_path, encoding="utf-8") as file_csv:
#     reader = csv.DictReader(file_csv, delimiter=",")
#     for line in reader:
#         # line = {key.strip(): value.strip() for key, value in line.items()}
#         print(line)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Remontez dans l'arborescence des répertoires jusqu'à la racine de votre projet
# (dans cet exemple, nous supposons que le script est deux niveaux en dessous de la racine du projet)
project_root = os.path.dirname(os.path.dirname(script_dir))

# print('projet_root',project_root)
