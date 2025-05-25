import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import cls
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from pf_tools import pf, tbl

# Réf.: https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/

iss = ["i"]
jss = ["j"]
kss = ["k"]
mss = ["m"]
nss = ["n"]
oss = ["o"]
gss = ["gris"]
rss = ["rose"]
tss = ["t"]


def bb():
    global s
    s += "\033[1;34mB \033[0m"


def rr():
    global s
    s += "\033[1;31mR \033[0m"


def gg():
    global s
    s += "\033[1;30mG \033[0m"


if __name__ == "__main__":

    cls(" zestedesavoir.com")

    # exit()
    def uuu0():
        sequence = []
        N = 6  # Nombre total d'éléments dans la séquence
        for i in range(N):
            if i < N // 2:
                # Pour les trois premiers éléments, on diminue de 2 à chaque itération
                sequence.append(N - 2 * i)
            else:
                # Pour les trois derniers éléments, on augmente de 2 à chaque itération
                sequence.append(2 * (i - N // 2) + 2)

        print(sequence)

    def uuu01():
        N = 6  # Nombre total d'éléments dans la séquence
        for i in range(N):
            value = (N - 2 * i) * ((N // 2 - i) // (N // 2) + 1) + (
                2 * (i - N // 2) + 2
            ) * (i // (N // 2))
            print(value, end=" ")

    def uuu02():
        N = 6  # Nombre total d'éléments dans la séquence
        for i in range(N // 2):
            value = N - 2 * i
            print(value, end=" ")

        # Seconde moitié de la séquence
        for i in range(N // 2, N):
            value = 2 * (i - N // 2) + 2
            print(value, end=" ")

    # uuu02()
    # ls()
    # uuu()
    # exit()
    # N = 10
    # M = N // 2
    # for r in range(M):
    #     if i < M:
    #         r = N - 2 * i
    #     else:
    #         r = 2 * (i - M) + 2
    # g = (N - r) // 2

    s = ""
    i = -1
    for _ in range(10):
        i += 1

        for r in range(5):
            if i < 5:
                r = 10 - 2 * i
            else:
                r = 2 * (i - 5) + 2
        g = (10 - r) // 2

        # Calcul de r en utilisant la symétrie de la séquence
        r = (10 - 2 * i) * ((5 - i) // 5) + (2 * (i - 5) + 2) * (i // 5)
        r = (10 - 2 * i) * ((5 - i) // 5)

        # Calcul de g basé sur r
        g = (10 - r) // 2

        for _ in range(g):
            gg()

        # bb()

        for _ in range(r):
            rr()

        # bb()

        for _ in range(g):
            gg()

        variables = ["m", "n", "o", "i", "j", "k", "g", "r", "t"]
        lists = [mss, nss, oss, iss, jss, kss, gss, rss, tss]

        for var, lst in zip(variables, lists):
            try:
                lst.append(eval(var))
            except NameError:
                pass
                # print(f"Erreur : {var} n'est pas défini")

    # tbl([[i for i in range(-1, 6)], iss, jss, kss, gss, rss, tss])
    but = ["But", 0, 1, 2, 2, 1, 0]
    tbl([iss, jss, kss, mss, nss, oss, gss, rss, tss, but])

    length = 10 * 13
    print(*[(s[i : i + length]) for i in range(0, len(s), length)], sep="\n")

    # exit()
    # 5 4 3 2 1 0 0 1 2 3 4 5
