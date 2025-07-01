import grands_plateaux_cases as gpc


def case():
    # nb = int(input())

    l = gpc.case01()  # [4, 3, 5, 0, 3, 4, 3, 0, 1]
    nb = len(l)

    d = {}
    min_dist = dist = len(l) - 1

    for i in range(1, nb):
        if l[i] not in d:
            min_dist = min(min_dist, i - d[l[i]])
            d[l[i]] = i
            pass

        d[l[i]] = i

        # for j in range(i + 1, min_dist - 3):
        #     if l[j] == l[i]:
        #         dist = j - i
        #         if dist < min_dist:
        #             min_dist = dist
        #             min_cpt = l[i]
        pass
    print(min_cpt)
    # print(l)


if __name__ == "__main__":
    case()
    pass
