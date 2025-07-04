def case01():
    return [6, 1, 6, 4, 4, 4, 6, 6]  # [6, 1, 6, 4, 4, 4, 6, 6] → 4: 3x


def case02():
    l1 = [4, 3, 5, 0]
    l2 = [3, 4]
    l3 = [3, 0, 1]
    return l1 + l2 + l3  # [4, 3, 5, 0, 3, 4, 3, 0, 1] → 4: 1x


def case03():
    l = [0, 1, 2, 3, 4] * 500 # → 0: 1x
    return l

if __name__ == "__main__":
    pass
