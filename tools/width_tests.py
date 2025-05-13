from tabulate import tabulate

# from globals import *
# from main_tools import *


def auto_partition(data: list, L: int, decalU: int = 0, decalP: int = 0) -> list:
    """Retourne le nombre d'élément pour chaque sous-groupe en fonction de L.
    decalU: Décallage Unitaire
    decalP: Décallage Partie
    """

    parts = []
    part = 0
    part_cumul = decalP
    for v in data:
        if part_cumul + v + decalU > L:
            if part:
                parts.append(
                    part
                )  # Ajoute l'index du dernier élément du segment valide
            part_cumul = v + decalU  # Redémarre le cumul avec l'élément actuel
            part = 1
        else:
            part += 1
            part_cumul += v + decalU
    parts.append(part)
    return parts


def calculW():

    import random

    arr = [random.randint(1, 7) for _ in range(10)]
    print(arr)
    print(auto_partition(arr, 20))

    data = [6, 7, 4, 2, 5, 6, 4, 3, 1, 2]
    L = 1

    print(str(data) + "\n")
    for L in range(2, 17, 3):
        l = auto_partition(data, L, 3, 1)
        if L == 14:
            print(f"LIMITE={L}")
            print("─" * len(str(l)) + "\n" + str(l) + "\n" + "─" * len(str(l)))

    print("Reconstitution:")
    i = 0
    for n in l:
        print(data[i : i + n])
        i += n

if __name__ == "__main__":

    # cls("Width Tests")
    import os

    os.system("cls" if os.name == "nt" else "clear")
    calculW()

    # exit()
