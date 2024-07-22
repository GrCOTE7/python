def recursiveSort(l, StartInd=0):
    if len(l) - 1 > StartInd:
        minValInd = StartInd
        for j in range(StartInd + 1, len(l)):
            if l[j] < l[minValInd]:
                minValInd = j
                
        l[StartInd], l[minValInd] = l[minValInd], l[StartInd]
        # print (str(StartInd).rjust(3), l)
        print (l,end=',')
        recursiveSort(l, StartInd + 1)
    return l


l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]
print(' # ', l)
recursiveSort(l)
# print(recursiveSort(l))
