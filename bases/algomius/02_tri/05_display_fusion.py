import random
import Display_graph

"""
    Implémentation du tri par fusion
"""


# Tri fusion sans affichage
def sort_merge(l):
    n = len(l)

    if n > 1:
        mid = n // 2
        tab_left = l[0:mid] 
        tab_right = l[mid:n]
        sort_merge(tab_left)
        sort_merge(tab_right)

        i = j = k = 0
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


# Tri fusion avec affichage
def sort_merge_display(l, start=0, end=None):
    graph.drawGraph(l)
    if end == None:
        end = len(l)

    if end - 1 > start:

        mid = (end + start) // 2
        sort_merge_display(l, start, mid)
        sort_merge_display(l, mid, end)

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
        print(l)
        graph.drawGraph(l)


if __name__ == "__main__":
    # l = random.sample(range(0, 1000), 500)
    # print(l)
    # sort_merge(l)
    # print(l)

    graph = Display_graph.Display_graph("Merge sort", 1500, 600, 1, 1)
    # l = random.sample(range(0, 100), 5)
    l = [3, 5, 1, 4, 2]
    print(l)
    sort_merge_display(l)
    graph.waitQuit()
    print(l)
