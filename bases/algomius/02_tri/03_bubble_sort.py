import random
import Display_graph

"""
    Ce programme propose plusieurs implémentations du tri à bulle ou bubble sort
"""


def bubbleSort(l):
    changesExists = True
    while changesExists:
        changesExists = False
        for ind in range(len(l) - 1):
            if l[ind] > l[ind + 1]:
                l[ind], l[ind + 1] = l[ind + 1], l[ind]
                print(l)
                changesExists = True
    return l


def bubbleSortDisplay(l):
    graph = Display_graph.Display_graph("Bubble sort", 1500, 600, 0.2, 0.2)
    changesExists = True
    while changesExists:
        changesExists = False
        for ind in range(len(l) - 1):
            if l[ind] > l[ind + 1]:
                graph.displaySwap(l, ind, ind + 1)
                # l[ind], l[ind + 1] = l[ind + 1], l[ind]
                print(l)
                changesExists = True
    graph.waitQuit()


if __name__ == "__main__":

    # l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]

    # génère 10 nombres uniques entre 1 et 100
    l = random.sample(range(1, 101), 10)

    print(l)
    # bubbleSort(l)
    bubbleSortDisplay(l)
