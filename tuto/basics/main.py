import sys
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *

cls("Script tuto/")


if __name__ == "__main__":
    pass

    class Personne:
        def __init__(self, nom, age):
            self.nom = nom
            self.age = age
            print(77777)

        def se_presenter(self):
            print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.", end="")

            line()

    # exit()
    lg = "\n" + "-" * 55
    print("{0: ^55}".format("Divers"))
    print(lg)

    # //2fix classer ci-dessous

    class Personne:
        def __init__(self, nom, age):
            self.nom = nom
            self.age = age

        ls()

        def se_presenter(self):
            print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.", end="")

    # Création d'un objet
    p1 = Personne("Lionel", 61)
    p1.se_presenter()
    print(lg)

    import numpy as np

    arr = np.array([1, 2, 3, 4, 5, 6])
    print(arr.mean(), end="")  # Moyenne des éléments

    print(lg)

    import pandas as pd

    data = {"Nom": ["Alice", "Bob"], "Âge": [25, 30]}
    df = pd.DataFrame(data)
    print(df)

    print(lg)

    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]
    plt.plot(x, y)
    # plt.show()

    print(lg)

    exit()
    s = "Lionel"
    print(s[2:4])
    print()

    d = dict()
    d["M-P", "R"] = 789
    d["L", "C"] = 123

    for f, l in d:
        print(f"{f+'. ':<5} {l+'. ':<7}", ": ", d[f, l])

    print("\n" + str(d))

    n = d["L", "C"]
    print(n)
    print(": ".join(["L. C.", str(n)]))

    print(d.keys())
    print(d.values())
    print(d.items())

    print(lg)

    print("Longueur=%s" % len(d))
    print("Type=%s" % type(d))
    d.update({("A", "K"): 456})
    print(str(d) + "\n")

    # print(d.items())

    sorted_keys = sorted(d.keys())
    for key in sorted_keys:
        print(f"{str(key):<12} : ", d[key])
    print(d.pop(("A", "K")))
    print(lg)
    sorted_keys = sorted(d.keys())
    for key in sorted_keys:
        print(f"{str(key):<12} : ", d[key])

    print(lg)

    a = [1, 2, 3]
    # b = a
    b = a[::]  # <=> b = a.copy()
    b.append(4)

    print(f"{a=}\n" + f"{b=}")
    print(lg)
