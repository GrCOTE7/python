import sys
import os
from pprint import pprint

script_dir = os.path.dirname(__file__)
modules_dir = os.path.join(script_dir, "modules")
sys.path.append(modules_dir)

from graphData import graphData


def showLine(i, l, un, deux):
    print(str(i).rjust(2), l, "→", str(un).rjust(2), "↔", str(deux).rjust(2))


def dichotomySort(l):
    i = 0
    for indice in range(len(l)):
        j = indice
        while j > 0 and l[j - 1] > l[j]:
            showLine(i, l, l[j - 1], l[j])
            i += 1
            l[j - 1], l[j] = l[j], l[j - 1]
            j -= 1
    showLine(i, l, "ni", "Fi → Fini !")
    return l


def SortArr(l):
    res = []
    i = 0
    for indice in range(len(l)):
        j = indice
        while j > 0 and l[j - 1] > l[j]:
            showLine(i, l, l[j - 1], l[j])
            i += 1
            res.append(l[::])
            l[j - 1], l[j] = l[j], l[j - 1]
            j -= 1
    showLine(i, l, "ni", "Fi → Fini !")
    res.append(l)
    return res


if __name__ == "__main__":

    # l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]

    # génère 10 nombres uniques entre 1 et 100
    # l = random.sample(range(1, 101), 10)
    l = [3, 5, 1, 4, 2]

    dichotomySort(l[::]) 
    # print("-" * 68)
    # res = SortArr(l)
    # print("-" * 68)
    # pprint(res)

    data = {
        "max_value": 20,  # Dans les données,  valeur maximum des items - Max: 1e18 (Soit 1 suivi de 18 zéros))
        "numbers_number": 12,  # Mini 1e0 + 1 (Soit 2)
        "min_value": 1,  # Dans les données,  valeur minimale des items (Max: 1e18)
        "twice_authorized": 1,  # 0 : Pas de double 1 si OK
    }

    types = {1: "itératif", 2: "récursif", 3: "à bulles"}

    graph_params = {
        "op_name": "Tri " + types[3],  # "Tri itératif" ou "Tri récursif",
        "speed": 1,  # Délai entre 2 changements (En secondes)
        "screen_number": 2,  # Pour faire que le graphique sorte sur le 2ème écran et ne pas perdre la main sur l'éditeur (et le code)
    }

    # graphData(data, graph_params)
