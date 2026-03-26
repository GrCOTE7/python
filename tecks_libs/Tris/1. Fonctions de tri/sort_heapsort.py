import random
import Display_graph

"""
    Implémentation du tri par tas
"""


# Tri par tas sans affichage
def sort_heapsort(l):
    n = len(l)
    # Il n'y a que n // 2 racine dans le tas, le reste sont des feuilles
    for i in range(n // 2 - 1, -1, -1):
        restore_heap_properties(l, n, i)
    print(l)
    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        restore_heap_properties(l, i, 0)


# Fonction qui permet de reformer un tas
def restore_heap_properties(l, n, i):
    maxVal = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and l[maxVal] < l[left]:
        maxVal = left

    if right < n and l[maxVal] < l[right]:
        maxVal = right

    if maxVal != i:
        l[i], l[maxVal] = l[maxVal], l[i]
        restore_heap_properties(l, n, maxVal)


# Tris par tas avec affichage
def sort_heapsort_display(l):
    n = len(l)
    for i in range(n // 2 - 1, -1, -1):
        restore_heap_properties_display(l, n, i)
    print(l)
    for i in range(n - 1, 0, -1):
        graph.displaySwap(l, i, 0)
        restore_heap_properties_display(l, i, 0)


def restore_heap_properties_display(l, n, i):
    maxVal = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and l[maxVal] < l[left]:
        maxVal = left

    if right < n and l[maxVal] < l[right]:
        maxVal = right

    if maxVal != i:
        graph.displaySwap(l, i, maxVal)
        restore_heap_properties_display(l, n, maxVal)


if __name__ == "__main__":
    l = random.sample(range(0, 1000), 20)
    print(l)
    generator = sort_heapsort(l)
    print(l)
    graph = Display_graph.Display_graph("Heapsort", 1500, 600, 0.02, 0.05)
    l = random.sample(range(0, 1000), 100)
    print(l)
    sort_heapsort_display(l)
    graph.waitQuit()
    print(l)
