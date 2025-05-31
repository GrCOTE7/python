from re import I, L
import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import *
# from tools import cls
from pathlib import Path

from cycler import V
from flask.cli import F

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls

# Réf.: https://concours.castor-informatique.fr
# X (Garder) Code Prépa Concours 2025 ORANGE uftm3fkb et v37y3j6i
# X (Garder) Code Prépa Concours 2025 VERTE1 vmv6ypbt
#                                     VERTE2 mc65hnr9


def haut():
    print("↑", end=" ")


def bas():
    print("↓", end=" ")


def gauche():
    print("←", end=" ")


def droite():
    print("→", end=" ")


def avance():
    print("↑", end=" ")


def recule():
    print("↓", end=" ")


def tourneDroite():
    droite()


def tourneGauche():
    gauche()


def ramasser():
    print("T", end=" ")


def deposer():
    print("P", end=" ")


if __name__ == "__main__":

    cls(" old.algorea.org")
    # from robot import *

    def uuu():

        # fs = [0]*6
        # for i in range(6):
        #     print(i, fs.count(i), sep=": ")

        # n = max(fs, key=lambda x: fs.count(x))

        def cnt(x):
            return fs.count(x)

        cars = ["○", "●", "□", "■", "△", "▲"]
        fs = [1, 2, 4, 1, 0, 0, 2, 4, 0, 2, 0, 3, 4, 2, 0]
        fsf = [cars[int(fs[i])] for i in range(len(fs))]

        ts = [[], [], [], [], [], []]

        # for i in range(15):
        #     ts[fs[i]].append(i)
        [ts[fs[i]].append(i) for i in range(15)]
        # print("ts1", ts, sep=" = ")
        ts.sort(key=len, reverse=True)
        print("ts2", ts, sep=" = ", end="\r")

        # for c in range(15, 3, -1):
        #     print(ts[c] + str(c), end=", ")

        ls()

        ts = [item + 1 for sublist in ts for item in sublist]
        print("ts3", ts, sep=" = ")

        tbl([*[cars]], *[range(6)])
        tbl([*[range(1, 17)], *[fsf], *[fs]])

    # n = int(input("Enter a number: "))

    uuu()

    exit()
# soluce 1
