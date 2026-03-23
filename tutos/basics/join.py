import sys
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *
from tools import ls

cls("join()")

if __name__ == "__main__":

    # Concaténation de noms avec des virgules comme séparateur
    names = ["Alice", "Bob", "Charlie"]
    result = ", ".join(names)
    print(result)  # Output: Alice, Bob, Charlie
    ls()

    # Création d'un chemin de fichier avec un séparateur spécifique
    file_parts = ["home", "user", "documents", "file.txt"]
    file_path = "/".join(file_parts)
    print(file_path)  # Output: home/user/documents/file.txt
    ls()

    # print(",".join([x for x in [1, 2, 3]])) ERROR
    print(",".join([str(x) for x in [1, 2, 3]]))
    ls()

    nombres = [1, 2, 3, 4, 5]
    chaine_nombres = ", ".join(map(str, nombres))
    chaine_nombres = ", ".join(map(str, nombres))
    print(nombres)
    # print(",".join(nombres)) ERROR
    print(chaine_nombres)
    ls()

    email = "example@gmail.com"
    masque_email = email[0] + "***" + "".join(email[email.index("@") :])
    print(masque_email)
    ls()

    import random
    import string

    caracteres = random.choices(string.ascii_letters + string.digits, k=12)
    mot_de_passe = "".join(caracteres)
    print(mot_de_passe)
    ls()

    import numpy as np

    # Créer un tableau à partir d'une liste Python
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)

    # Créer un tableau 2D (matrice)
    matrice = np.array([[1, 2], [3, 4], [5, 6]])
    print(matrice)
    ls()

    # Tableau de zéros
    zeros = np.zeros((3, 3))

    # Tableau de uns
    uns = np.ones((2, 4))

    # Tableau de valeurs aléatoires
    random_values = np.random.rand(3, 3)

    # Tableau d'une séquence de nombres
    range_values = np.arange(0, 10, 2)  # De 0 à 10, pas de 2

    print(zeros, uns, random_values, range_values, sep="\n---\n")

    exit()
