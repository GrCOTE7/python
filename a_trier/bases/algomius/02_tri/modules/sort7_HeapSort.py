# https://www.youtube.com/watch?v=cCiyQ1Z_NBY&list=PLo53cbpzes8YitYTmH9Z2wxLt73sL_CJj&index=7

# https://www.youtube.com/watch?v=JyXNda9Frrw&list=PLo53cbpzes8YitYTmH9Z2wxLt73sL_CJj&index=6

import sys
import os
from pprint import pprint
import random

from matplotlib.pyplot import show

script_dir = os.path.dirname(__file__)
modules_dir = os.path.join(script_dir, "modules")
sys.path.append(modules_dir)

from graphData import graphData


def showLine(i, l, un, deux):
    print(str(i).rjust(2), l, " :", str(un).rjust(2), "↔", str(deux).rjust(2))


FINI = "Fi → Fini !"

res = []
i_count = 0


def heap_sort(l):
    n = len(l)
    # Il n'y a que n // 2 racines dans le tas, le reste sont des feuilles
    for i in range(n // 2 - 1, -1, -1):
        heapify(l, n, i)

    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0)


# restore heap properties (liste, dernier indice, racine à évaluer)
def heapify(l, n, i):
    maxVal = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and l[maxVal] < l[left]:
        maxVal = left

    if right < n and l[maxVal] < l[right]:
        maxVal = right

    if maxVal != i:
        l[i], l[maxVal] = l[maxVal], l[i]
        heapify(l, n, maxVal)


def heap_sort_arr(l):
    global res, i_count
    n = len(l)
    if res == []:
        # showLine(i_count, l, l[i], l[0])
        res.append(l[::])
        # showLine(i_count, l, l[0], l[1])
    # Il n'y a que n // 2 racines dans le tas, le reste sont des feuilles
    for i in range(n // 2 - 1, -1, -1):
        heapify_arr(l, n, i)

    for i in range(n - 1, 0, -1):
        showLine(i_count, l, l[i], (str)(l[0]) + " trié")
        l[i], l[0] = l[0], l[i]
        i_count += 1
        res.append(l[::])
        heapify_arr(l, i, 0)
    showLine(len(res) - 1, l, "ni", FINI)
    return res


# restore heap properties (liste, dernier indice, racine à évaluer) 
def heapify_arr(l, n, i):
    """
    Ajuste récursivement les éléments de la liste pour maintenir la propriété de max-heap.

    Parameters:
    list l : La liste des éléments à ajuster.
    n (int): La longueur de la liste.
    i (int): L'index du nœud courant dans le tas.
    """
    global i_count

    maxVal = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and l[maxVal] < l[left]:
        maxVal = left

    if right < n and l[maxVal] < l[right]:
        maxVal = right

    if maxVal != i:
        showLine(i_count, l, l[i], l[maxVal])
        l[i], l[maxVal] = l[maxVal], l[i]
        i_count += 1
        res.append(l[::])
        heapify_arr(l, n, maxVal)


def SortArr(l):
    return heap_sort_arr(l)


if __name__ == "__main__":

    # l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]

    # génère 10 nombres uniques entre 1 et 100
    # l = random.sample(range(1, (int)(1e5 + 1)), 100000)
    # l = [3, 7, 5, 1, 4, 6, 2]

    # print(l)
    # heap_sort_arr(l)
    # print(l)
    # print("-" * 68)
    # pprint(res, width=150)

    # quickSort(l[::])
    # res =
    # res = SortArr(l)

    # print("-" * 68)
    # pprint(res)

    # SortArr = quickSort()

    data = {
        "max_value": 100,  # Dans les données,  valeur maximum des items - Max: 1e18 (Soit 1 suivi de 18 zéros))
        "numbers_number": 10,  # Mini 1e0 + 1 (Soit 2)
        "min_value": 1,  # Dans les données,  valeur minimale des items (Max: 1e18)
        "twice_authorized": 0,  # 0 : Pas de double 1 si OK
    }

    # print(l)
    types = {
        1: "itératif",
        2: "récursif",
        3: "à bulles",
        4: "par insertion",
        5: "par fusion",
        6: "rapide",
        7: "par tas",
        8: "par comptage",
        9: "dichotomique",
        10: "complexité",
    }

    graph_params = {
        "op_name": "Tri " + types[3],  # "Tri itératif" ou "Tri récursif",
        "speed": 0.1,  # Délai entre 2 changements (En secondes)
        "screen_number": 2,  # Pour faire que le graphique sorte sur le 2ème écran et ne pas perdre la main sur l'éditeur (et le code)
    }

    graphData(data, graph_params)
