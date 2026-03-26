import random
import Display_graph

"""
    Implémentation du tri par comptage, couting sort
"""

# uniquement possible avec des entier car utilisé comme indice
# Mauvaise gestion de la mémoire, beaucoup de cases vides
# temps linéaire


# Tri par comptage sans affichage histogramme
def sort_countsort(l):
    maxVal = max(l)
    output = [0 for i in range(maxVal + 1)]

    for i in l:
        output[i] += 1

    ind = 0
    for i in range(len(output)):
        for j in range(output[i]):
            l[ind] = i
            ind += 1


# Tri par comptage avec affichage histogramme
def sort_countsort_display(l):
    maxVal = max(l)
    output = [0 for i in range(maxVal + 1)]

    for i in l:
        output[i] += 1
        graph.drawGraph(output)

    ind = 0
    for i in range(len(output)):
        for j in range(output[i]):
            l[ind] = i
            ind += 1
            graph.drawGraph(l)


if __name__ == "__main__":
    l = random.sample(range(0, 1000), 50)
    print(l)
    generator = sort_countsort(l)
    print(l)

    graph = Display_graph.Display_graph("Countsort", 1500, 600, 0.02, 0.05)
    l = random.sample(range(0, 1000), 100)
    print(l)
    sort_countsort_display(l)
    graph.waitQuit()
    print(l)
