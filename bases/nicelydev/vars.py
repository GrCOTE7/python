def msg():
    print()

    a = {1, 3, 3, 4, 8}
    b = {2, 7, 3, 4, 5}
    
    unionAB = a.union(b)

    print("a: ", a, "- b:", b)
    print("union: ", unionAB)
    print("intersection: ", a.intersection(b))

    print("a diff(b):", a.difference(b))
    print("b diff(a):", b.difference(a))
    print("a symmetric_diff(b):", a.symmetric_difference(b))

    print()


if __name__ == "__main__":
    msg()
