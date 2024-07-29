def showLine(i, l, un, deux):
    print(str(i).rjust(2), l, "→", str(un).rjust(2), "↔", str(deux).rjust(2))
    # print(str(i).rjust(2), end=' ')

    # showLine(0, l, l[0], min(l[1:]))


def recursiveSort(l, StartInd=0):

    if len(l) - 1 > StartInd:
        minValInd = StartInd
        for j in range(StartInd + 1, len(l)):
            if l[j] < l[minValInd]:
                minValInd = j

        l[StartInd], l[minValInd] = l[minValInd], l[StartInd]
        print(str(StartInd).rjust(3), l)
        recursiveSort(l, StartInd + 1)

    return l


def recursiveSortArr(l):
    res = []

    def recursionSort(l, res, StartInd=0):
        if len(l) - 1 > StartInd:
            minValInd = StartInd
            for j in range(StartInd + 1, len(l)):
                if l[j] < l[minValInd]:
                    minValInd = j

            l[StartInd], l[minValInd] = l[minValInd], l[StartInd]

            print(str(StartInd).rjust(3), l)
            # res.append(l)  # Copie de l, et pas valeur finale
            # recursionSort(l, StartInd + 1)

            showLine(StartInd, l[minValInd], 111, 222)
            recursionSort(l, StartInd + 1)

    res.append(l)
    return recursionSort(l, res)

    # showLine(StartInd, l, "ni", "Fi")

    return recursionSort(l, res)


if __name__ == "__main__":
    # l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]
    l = [3, 1, 4, 2]
    print(" # ", l)
    res = recursiveSortArr(l)
    # recursiveSort(l)
    print("-" * 55)
    print(res)
