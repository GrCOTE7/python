def division(a, b):
    reste = a
    quotient = 0
    while reste >= b:
        reste -= b
        quotient += 1

    return quotient, reste


def tupples() -> None:

    t = 1, 23, "salut", (5, 6) * 2
    t += (777,)
    print(t[2].capitalize(), t, 777 in t, division(35, 7), "Oki")
    pass


def dicts():
    d = {x: 2 * x for x in range(11)}
    print(
        "5ème élément: ",
        d[5],
        "-",
        d.keys(),
        "-",
        d.values(),
        "-",
        d.items(),
        "-",
        d.get(18, "18: Trouvé"),
        "-",
        d.get(55, "55: Pas trouvé"),
        "\n" + "-" * 120,
    )
    d2 = {"un": 1, "deux": 2, "trois": 3}
    print(f"{d2=}")
    d3 = dict(un=1, deux=2, trois=3)
    print(f"{d3=}")
    print(f"{d3.keys()=}")
    print(f"{d3.values()=}")
    print(f"{d3.items()=}")
    print(f"{d3.get('un')=}")
    print(f"{d3.get('uno', 'Pas trouvé')=}")

    d3["quatre"] = 4
    del d3["deux"]
    print(f"{d3=}")
    print(f"{d3=}", f"{d3.pop("trois")=}")
    print(f"{d3=}")
    print(f"{d3.popitem()=}")
    print(f"{d3=}")
    print(f"{d3.fromkeys('un')=}")
    print(f"{d3.fromkeys(['a','b'], 1)=}")
    print(f"{dict.fromkeys(['a','b'], 1)=}")
    d3.clear()
    print(f"{d3=}")
    d3.update({"uno": 1})
    d3.setdefault("deux", 2)
    d3.setdefault("trois", 2)
    d3["quatre"] = [1, 2, 3]
    print(f"{d3=}")


def getTable(fichier):
    f = open(fichier, "r")
    champs = f.readline().rstrip().split(";")
    tab = []
    for ligne in f:
        data = ligne.rstrip().split(";")
        data[1] = int(data[1])
        data[2] = float(data[2])
        tab.append(data)
    f.close()

    return champs, tab


def tablesv1():
    f = open("restaurants.csv", "r")
    tab = [ligne.rstrip().split(";") for ligne in f]
    f.close()
    print(tab[0])
    print(*tab[1:])
    print(*tab)


def supprimeDoublons(table, colonne):
    triee = sorted(table, key=lambda r: r[colonne])
    tmp = [triee[0]]
    for resto in triee:
        if resto[colonne] != tmp[-1][colonne]:
            tmp.append(resto)
    return tmp


def tablesV2():
    f = open("restaurants.csv", "r")
    head = f.readline().rstrip().split(";")
    tab = []
    for ligne in f:
        data = ligne.rstrip().split(";")
        tab.append(data)
    f.close()

    print("", head, "\n", *tab)
    print(*[resto for resto in tab if resto[2] > 4.7])

    triee = sorted(tab, key=lambda r: r[2], reverse=False)
    print(f"{triee=}")

    dedoublonnee = supprimeDoublons(tab, 0)
    print(f"{dedoublonnee=}")


def tables():

    champs, tab = getTable("restaurants.csv")
    champs2, tab2 = getTable("restaurants2.csv")
    print("", champs, "\n", *tab)
    print("", champs2, "\n", *tab2)
    print(tab + tab2)
    print(supprimeDoublons(tab + tab2, 0))


def variables():
    s = set((2, 2, 3))
    s.add(4)
    print(s, type(s))
    s2 = {4, 5, 5, 6}  # 5 Can't be twice
    s2.add(7)
    print(s2, type(s2))
    fake_s = frozenset(s)
    # fake_s.add(8) # ERROR
    print(fake_s, type(fake_s))

    l = [2, 9]
    l[1] = 3
    l.insert(0, "Un")
    fake_l = frozenset(l)
    # fake_l.append(4) # ERROR
    print(l, fake_l, type(fake_l))


def main():
    variables()


# tupples()
# dicts()
# tables()


if __name__ == "__main__":

    # tupples()
    main()
    print("-" * 119)
