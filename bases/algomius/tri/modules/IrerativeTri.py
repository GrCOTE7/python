def selection_sort(l):
    for i in range(len(l) - 1):
        minInd = i
        for j in range(i + 1, len(l)):
            if l[j] < l[minInd]:
                minInd = j
        if i != minInd:
            l[i], l[minInd] = l[minInd], l[i]
        print(
            str(i).rjust(2),
            "(//" + str(l[minInd]).rjust(2) + "→" + str(l[i]).rjust(2) + ") →",
            l,
        )
    return l
