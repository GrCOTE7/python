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


def SortArr(l):
    res = []

    def recursionSort(l, StartInd=0):
        nonlocal res
        if len(l) - 1 > StartInd:
            minValInd = StartInd
            for j in range(StartInd + 1, len(l)):
                if l[j] < l[minValInd]:
                    minValInd = j

            showLine(StartInd, l, l[StartInd], l[minValInd])
            res.append(l.copy())
            l[StartInd], l[minValInd] = l[minValInd], l[StartInd]

            if len(l) - 2 == StartInd:
                # print ('xxx', len(l), StartInd)
                res.append(l.copy())
            recursionSort(l, StartInd + 1)

    recursionSort(l)
    showLine(len(l) + 1, l, "ni", "Fi → Fini !")
    return res


if __name__ == "__main__":
    from pprint import pprint

    # l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]
    l = [3, 1, 4, 2]
    # print(" # ", l)
    res = SortArr(l)
    # recursiveSort(l)
    print("-" * 55)
    pprint(res, width=50)
