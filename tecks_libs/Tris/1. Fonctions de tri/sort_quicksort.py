import random
import Display_graph

"""
    Implémentation du tri rapide
"""


# Fonction de partitionnement du tableau, le pivot est le dernier élément
def partition(l, start, end):
    piv = l[end]
    j = start
    for i in range(start, end):
        if l[i] <= piv:
            l[i], l[j] = l[j], l[i]
            j += 1
    l[j], l[end] = l[end], l[j]
    return j


# Tri rapide sans affichage
def sort_quicksort(l, start=0, end=None):
    if end == None:
        end = len(l) - 1

    if end > start:
        pivot = partition(l, start, end)
        sort_quicksort(l, start, pivot - 1)
        sort_quicksort(l, pivot + 1, end)


# Partitionnement avec affichage
def partition_display(l, start, end):
    piv = l[end]
    j = start
    for i in range(start, end):
        if l[i] <= piv:
            graph.displaySwap(l, i, j)
            j += 1
    graph.displaySwap(l, end, j)
    return j


# Tir rapide avec affichage
def sort_quicksort_display(l, start=0, end=None):
    if end == None:
        end = len(l) - 1

    if end > start:
        pivot = partition_display(l, start, end)
        sort_quicksort_display(l, start, pivot - 1)
        sort_quicksort_display(l, pivot + 1, end)


if __name__ == "__main__":
    l = random.sample(range(0, 1000), 500)
    print(l)
    sort_quicksort(l)
    print(l)

    graph = Display_graph.Display_graph("Quicksort", 1500, 600, 0.002, 0.005)
    l = random.sample(range(0, 1000), 500)
    print(l)
    sort_quicksort_display(l)
    graph.waitQuit()
    print(l)
