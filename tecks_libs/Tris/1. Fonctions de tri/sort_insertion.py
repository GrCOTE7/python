import random
import Display_graph

"""
    Implémentation du tri par insertion
"""


# Tri par insertion sans affichage
def sort_insertion(l):
    for i in range(len(l)):
        j = i
        while j > 0 and l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
            j -= 1


# Tri par insertion avec affichage
def sort_insertion_display(l):
    graph = Display_graph.Display_graph("Insertion sort", 1500, 600, 0.002, 0.0001)

    for i in range(len(l)):
        j = i
        while j > 0 and l[j - 1] > l[j]:
            graph.displaySwap(l, j, j - 1)
            j -= 1

    graph.waitQuit()


if __name__ == "__main__":
    # l = random.sample(range(0, 1000), 50)
    # print(l)
    # sort_insertion(l)
    # print(l)
    l = random.sample(range(0, 1000), 75)
    print(l)
    sort_insertion_display(l)
    print(l)
