import random
import time


def sort_selection(l):
    for i in range(len(l)-1):
        minInd = i
        for j in range(i+1, len(l)):
            if l[j] < l[minInd]:
                minInd = j
        if i!=minInd:
            l[i], l[minInd] = l[minInd], l[i]


def sort_bubble(l):
    hasChanged = True
    while hasChanged:
        hasChanged = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                hasChanged = True


def partition(l, start, end):
    piv = l[end]
    j = start
    for i in range(start, end):
        if l[i] <= piv:
            l[i], l[j] = l[j], l[i]
            j += 1
    l[j], l[end] = l[end], l[j]
    return j


def sort_quick(l, start=0, end=None):
    if end == None:
        end = len(l) - 1

    if end > start:
        pivot = partition(l, start, end)
        sort_quick(l, start, pivot - 1)
        sort_quick(l, pivot + 1, end)


l1 = random.sample(range(0, 1000000), 5000)
l2 = l1[::]
l3 = l1[::]

start = time.time()
sort_selection(l1)
end = time.time()
print("Selection:", end - start)

start = time.time()
sort_bubble(l2)
end = time.time()
print("Bubble:", end - start)

start = time.time()
sort_quick(l3)
end = time.time()
print("Quick:", end - start)
