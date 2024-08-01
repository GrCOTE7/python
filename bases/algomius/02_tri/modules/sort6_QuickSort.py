# https://www.youtube.com/watch?v=JyXNda9Frrw&list=PLo53cbpzes8YitYTmH9Z2wxLt73sL_CJj&index=6

import sys
import os
from pprint import pprint
import random

script_dir = os.path.dirname(__file__)
modules_dir = os.path.join(script_dir, "modules")
sys.path.append(modules_dir)

from graphData import graphData


def showLine(i, l, un, deux):
    print(str(i).rjust(2), l, "→", str(un).rjust(2), "↔", str(deux).rjust(2))


def partitionner(l, debut, fin):
    valeur_pivot = l[fin]
    # Fixer la valeur et l'indice du pivot
    indice_pivot = debut

    # Parcourir les éléments
    for i in range(debut, fin):
        # Si l'élément est plus petit que le pivot
        if l[i] < valeur_pivot:
            # Inverser l'élément avec l'élément à gauche du pivot
            l[i], l[indice_pivot] = l[indice_pivot], l[i]
            if i != indice_pivot:
                print(l)
            # Incrémenter l'indice du pivot
            indice_pivot += 1

    # Inverser le pivot avec l'élément à droite du pivot
    l[fin], l[indice_pivot] = l[indice_pivot], l[fin]
    if fin != indice_pivot:
        print(l)
    # Retourner l'indice du pivot
    return indice_pivot

    # Retourner l'indice de pivot
    return indice_pivot


def tri_rapide(l, debut=0, fin=None):
    if fin == None:
        fin = len(l) - 1

    if fin > debut:
        # Condition de fin
        pivot = partitionner(l, debut, fin)
        # Chercher le pivot
        # Tri sur la partie de gauche
        tri_rapide(l, debut, pivot - 1)
        # Tri sur la partie de droite
        tri_rapide(l, pivot + 1, fin)


def partition(l, start, end):
    piv = l[end]
    j = start
    for i in range(start, end):
        li = l[i]
        lj = l[j]
        if l[i] <= piv:
            l[i], l[j] = l[j], l[i]
            if i != j:
                print(l)
            j += 1

    lj = l[j]
    lend = l[end]
    l[j], l[end] = l[end], l[j]
    if end != j:
        print(l)
    return j


# Tri rapide sans affichage
def sort_quicksort(l, start=0, end=None):
    if end == None:
        end = len(l) - 1

    if end > start:
        pivot = partition(l, start, end)
        sort_quicksort(l, start, pivot - 1)
        sort_quicksort(l, pivot + 1, end)


def quickSort(l):
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

    l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]

    # génère 10 nombres uniques entre 1 et 100
    # l = random.sample(range(1, (int)(1e5 + 1)), 100000)
    # l = [3, 5, 1, 4, 2]

    print(l)
    # sort_quicksort(l)
    tri_rapide(l)
    print(l)

    # quickSort(l[::])
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
