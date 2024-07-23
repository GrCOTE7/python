from modules.IterativeSorts import IterativeSort

l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]
print("Ori    :", l)

s = l.copy()

s.sort()
print("sort() :", s)

sgc7 = l.copy()
sgc7 = sorted(sgc7, key=lambda x: x)
print("sgc7() :", sgc7, end="\n\n")

IterativeSort(l)


