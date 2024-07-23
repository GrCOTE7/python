import random
import Display_graph

"""
    Ce programme propose plusieurs implémentations du tri à bulle ou bubble sort
"""

# Tri a bulle sans affichage
def sort_bubble(l):
    hasChanged = True
    while hasChanged:
        hasChanged = False

        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                hasChanged = True


# Tri a bulle avec affichage
def sort_bubble_display(l):
    graph = Display_graph.Display_graph('Bubble sort', 1500, 600,  .2, .5)

    hasChanged = True
    while hasChanged:
        hasChanged = False

        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                graph.displaySwap(l, i, i+1)
                # l[i], l[i+1] = l[i+1], l[i]
                print(l)
                hasChanged = True
    # graph.waitQuit()

if __name__ == "__main__":
    #l = random.sample(range(1, 1000), 50)
    #print(l)
    #sort_bubble(l)
    #print(l)
    l = random.sample(range(0, 101), 10)
    print(l)
    sort_bubble_display(l)
    print(l)

