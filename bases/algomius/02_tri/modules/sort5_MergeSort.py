# https://www.youtube.com/watch?v=d_4B9tLaqIY&list=PLo53cbpzes8YitYTmH9Z2wxLt73sL_CJj&index=9
# //2do voir aussi: https://www.youtube.com/watch?v=OEmlVnH3aUg&ab_channel=C%C3%A9dricGERLAND

import sys
import os
from pprint import pprint

# Tri par fusion

script_dir = os.path.dirname(__file__)
modules_dir = os.path.join(script_dir, "modules")
sys.path.append(modules_dir)

from graphData import graphData

 
def showLine(i, l, un, deux):
    print(str(i).rjust(2), l, "→", str(un).rjust(2), "↔", str(deux).rjust(2))


def mergeSort(l):
    n = len(l)

    if n > 1:
        mid = n // 2
        left_half = l[:mid]
        right_half = l[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        ind_left = ind_right = ind_list = 0

        while ind_left < len(left_half) and ind_right < len(right_half):
            if left_half[ind_left] < right_half[ind_right]:
                l[ind_list] = left_half[ind_left]
                ind_left += 1
            else:
                l[ind_list] = right_half[ind_right]
                ind_right += 1
            ind_list += 1

        while ind_left < len(left_half):
            l[ind_list] = left_half[ind_left]
            ind_left += 1
            ind_list += 1

        while ind_right < len(right_half):
            l[ind_list] = right_half[ind_right]
            ind_right += 1
            ind_list += 1
        print(l)


res = []


def SortArr(l, start=0, end=None):
    if end == None:
        end = len(l)

    if end - 1 > start:

        mid = (end + start) // 2
        SortArr(l, start, mid)
        SortArr(l, mid, end)

        tab_left = l[start:mid]
        tab_right = l[mid:end]
        i = j = 0
        k = start

        while i < len(tab_left) and j < len(tab_right):
            if tab_left[i] < tab_right[j]:
                l[k] = tab_left[i]
                i += 1
            else:
                l[k] = tab_right[j]
                j += 1
            k += 1

        while i < len(tab_left):
            l[k] = tab_left[i]
            i += 1
            k += 1

        while j < len(tab_right):
            l[k] = tab_right[j]
            j += 1
            k += 1

        # print(l)
        showLine(len(res), l, mid, k - 1)
        res.append(l[::])
        return res


if __name__ == "__main__":

    # l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]
    # print(len(l))

    # génère 10 nombres uniques entre 1 et 100
    # l = random.sample(range(1, 101), 10)
    # l = [3, 5, 1, 4, 2]

    # # print(l)
    # # mergeSort(l)
    # SortArr(l)
    # print()
    # pprint(res, width=50)
    # print("-" * 68)
    # res = SortArr(l)
    # print("-" * 68)
    # pprint(res)

    data = {
        "max_value": 200,  # Dans les données,  valeur maximum des items - Max: 1e18 (Soit 1 suivi de 18 zéros))
        "numbers_number": 100,  # Mini 1e0 + 1 (Soit 2)
        "min_value": 1,  # Dans les données,  valeur minimale des items (Max: 1e18)
        "twice_authorized": 1,  # 0 : Pas de double 1 si OK
    }

    types = {
        1: "itératif",
        2: "récursif",
        3: "à bulles",
        4: "par insertion",
        5: "par fusion",
        6: "rapide",
        7: "tas",
        8: "par comptage",
        9: "dichotomique",
        10: "complexité",
    }

    graph_params = {
        "op_name": "Tri " + types[5],  # "Tri itératif" ou "Tri récursif",
        "speed": 0.1,  # Délai entre 2 changements (En secondes)
        "screen_number": 2,  # Pour faire que le graphique sorte sur le 2ème écran et ne pas perdre la main sur l'éditeur (et le code)
    }

    graphData(data, graph_params)
