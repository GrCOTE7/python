import random
from pprint import pprint


def IterativeSort(l):
    def showLine(i, l, un, deux):
        print(str(i).rjust(2), l, "→", str(un).rjust(2), "↔", str(deux).rjust(2))

    for i in range(len(l) - 1):
        minInd = i

        for j in range(i + 1, len(l)):
            if l[j] < l[minInd]:
                minInd = j

        if i != minInd:
            showLine(i, l, l[i], l[minInd])
            l[i], l[minInd] = l[minInd], l[i]

    showLine(i + 1, l, "ni", "Fi")


def IterativeSortArr(l):
    res = []

    def showLine(i, l, un, deux):
        print(str(i).rjust(2), l, "→", str(un).rjust(2), "↔", str(deux).rjust(2))
        # print(str(i).rjust(2), end=' ')

    # showLine(0, l, l[0], min(l[1:]))

    for i in range(len(l) - 1):
        minInd = i

        for j in range(i + 1, len(l)):
            if l[j] < l[minInd]:
                minInd = j

        if i != minInd:
            showLine(i, l, l[i], l[minInd])
            res.append(l[:])  # Copie de l, et pas valeur finale
            l[i], l[minInd] = l[minInd], l[i]

    showLine(i + 1, l, "ni", "Fi")
    res.append(l)  # Valeur finale de l

    return res
