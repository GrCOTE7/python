l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]
print("Ori    :", l)

s = l.copy()

s.sort()
print("sort() :", s)

sgc7 = l.copy()

sgc7 = sorted(sgc7, key=lambda x: x)
print("sgc7() :", sgc7, end="\n\n")

lori = l.copy()
print(" " * 15, lori)


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
            "(//" + str(l[minInd]).rjust(2) + "→" + str(l[i]).rjust(2) + ") → ",
            l,
        )
    return l


selection_sort(l)
