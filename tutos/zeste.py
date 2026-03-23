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
    def uuu00():
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

    def uuu02():
        global s, i, g, r, N
        N = 12
        s = ""
        i = 11

        for _ in range(N):
            i -= 1

            # g = i + i // 6 * -2 * i + 11
            # g = i * (1 - 2 * (i // 6)) + 11

            r = (N - 2) - g * 2

            variables = ["m", "n", "o", "i", "j", "k", "g", "r", "t"]
            lists = [mss, nss, oss, iss, jss, kss, gss, rss, tss]

            for var, lst in zip(variables, lists):
                try:
                    lst.append(eval(var))
                except NameError:
                    pass

            for _ in range(g):
                gg()

            bb()

            for _ in range(r):
                rr()

            bb()

            for _ in range(g):
                gg()

        but = ["But", 0, 1, 2, 2, 1, 0]
        tbl([iss, jss, kss, mss, nss, oss, gss, rss, tss, but])

        length = N * 13
        print(*[(s[l : l + length]) for l in range(0, len(s), length)], sep="\n")

    def uuu01():
        N = 6  # Nombre total d'éléments dans la séquence
        for i in range(N // 2):
            value = N - 2 * i
            print(value, end=" ")

        # Seconde moitié de la séquence
        for i in range(N // 2, N):
            value = 2 * (i - N // 2) + 2
            print(value, end=" ")

    def uuu03():
        global s, i, j, g, r, N
        s = ""
        N = 12
        i = -1
        j = 0
        for _ in range(N):

            # r =

            i += 1
            j += 72

            k = j // 75

            g = (i + (i // 4)) // 6
            # k = (i // 13) * (22 - i)

            g = 2
            r = 777
            variables = ["m", "n", "o", "i", "j", "k", "g", "r", "t"]
            lists = [mss, nss, oss, iss, jss, kss, gss, rss, tss]

            for var, lst in zip(variables, lists):
                try:
                    lst.append(eval(var))
                except NameError:
                    pass

            for _ in range(g):
                gg()

            bb()

            for _ in range(r):
                rr()

            bb()

            for _ in range(g):
                gg()

        but = ["But", 0, 1, 2, 2, 1, 0]
        tbl(
            [
                [i for i in range(12)],
                iss,
                jss,
                kss,
                # mss,
                # nss,
                # oss,
                gss,
                rss,
                tss,
                but,
            ]
        )

        length = N * 13
        # print(*[(s[l : l + length]) for l in range(0, len(s), length)], sep="\n")

    def uuu04():
        global s, i, j, g, r, N
        N = 12
        but = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0]

        # i = -1
        j = 152

        divisor = 0.01
        while True:
            gs = []
            j = 12
            for i in range(N):
                j -= 1
                try:
                    k = int(i * j // divisor)
                    gs.append(k)
                except ZeroDivisionError:
                    break

            # gs = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0]

            if round(divisor * 100 % 10) == 0:
                print("divisor = ", divisor)

            if gs == but or divisor >= 999:
                tbl([but, gs])
                break

            divisor = round(divisor * 100 + 1) / 100

        print("Avec divisor ", divisor if gs == but else "Pas trouvé")
        print()

    def uuu05():

        limite = 4
        nb = brk = 0

        for divisor in range(-3, 4):
            if divisor == 0:
                continue

            print("divisor = ", divisor)
            # for i1 in range(-limite, limite):
            #     while True:

            #         for i in range(3):
            #             gs = []
            #             for j in range(3):
            #                 try:
            #                     k = int(i * j // divisor)
            #                     gs.append(k)
            #                 except ZeroDivisionError:
            #                     break

            #                 if nb >= 999:
            #                     brk = 1
            #                     break

            #                 nb += 1

            #         if brk:
            #             print("Avec divisor ", divisor, nb)
            #             break
            #         divisor = round(divisor * 100 + 1) / 100
            #         nb = 0

        # resIJ.append(iis)
        # tbl(resIJ)
        print(nf(nb, 0))

    def uuu06():

        resIJ = []
        iis = []
        limite = 12
        but = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0]
        nb = 0

        for divisor in range(1, 13):
            # if divisor == 0:
            #     continue
            print("divisor = ", divisor)
            for i1 in range(-limite, limite + 1):
                for i2 in range(i1 + 1, limite + 2):
                    # print("i1, i2 = ", i1, i2)
                    # for i1step in range(-limite // divisor, limite // divisor):
                    for i1step in range(1, 2):
                        for j1 in range(-limite, limite + 1):
                            for j2 in range(j1 + 1, limite + 1):
                                # print("j1, j2 = ", j1, j2)
                                for _ in range(1, 2):
                                    # -limite // divisor, limite // divisor):
                                    j2step = 1 if j2 > j1 else -1

                                    for i in range(i1, i2, i1step):
                                        gs = []
                                        for j in range(j1, j2, j2step):
                                            try:
                                                k = i + i // 6 * j
                                                gs.append(k)
                                            except ZeroDivisionError:
                                                break

                                            if gs == but:
                                                # tbl([but, gs])
                                                print(
                                                    (
                                                        "Avec divisor ",
                                                        (
                                                            divisor
                                                            if gs == but
                                                            else "Pas trouvé"
                                                        ),
                                                    ),
                                                    print(
                                                        "i1,i2,j1,j2,i1step,j2step,divisor\n",
                                                        i1,
                                                        i2,
                                                        j1,
                                                        j2,
                                                        i1step,
                                                        j2step,
                                                        divisor,
                                                    ),
                                                    exit(),
                                                )
                                                # break

                                            nb += 1
                                            print(nf(nb, 0), end="\r")

                                # n += 1
        # resIJ.append(iis)
        # tbl(resIJ)
        print(nf(nb, 0))

    def generate_sequence():
        seq = []
        N = 72  # Total number of segments in the sequence

        for i in range(N):
            seq.append(str(i // 12))
            # if i % 12 == 0:
            #     sequence.append("b")
            # elif i % 12 < 11:
            #     sequence.append("r")
            # else:
            #     sequence.append("b")

            # if i % 12 == 1 or i % 12 == 11:
            #     sequence.append("g")

        return " ".join(seq)

    print(generate_sequence())

    # exit()
    # 5 4 3 2 1 0 0 1 2 3 4 5
