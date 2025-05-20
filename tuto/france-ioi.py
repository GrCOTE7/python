from re import I, L
import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import *
# from tools import cls
from pathlib import Path

from cycler import V

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls

# Réf.: https://www.france-ioi.org/
# Code ALGORÉA: yqp4gbnf


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
    print("D", end=" ")


def tourneGauche():
    print("G", end=" ")


if __name__ == "__main__":

    cls(" france-ioi.org")
    # from robot import *

    # nVilles = int(input())
    # nbVilles = 0
    # for _ in range(nVilles):
    #     nbVilles += 1 if int(input()) > 10000 else 0

    # print(nbVilles)

    def uuu():

        a = 1

        d, f, n = (int(input()) for _ in range(3))
        print(sum(1 for _ in range(n) if d <= int(input()) <= f))

    uuu()
    exit()
    # x = int(input(()))
    # y = int(input())

    #####################################
    #####################################
    # n = int(input())
    # px = [int(input()) for _ in range(n)]
    # print(len(px) - px[::-1].index(min(px))) Donne la dernière pos du min
    #####################################
    # arbres = {
    #     "Tinuviel": lambda h, f: h <= 5 and f >= 8,
    #     "Calaelen": lambda h, f: h >= 10 and f >= 10,
    #     "Falarion": lambda h, f: h <= 8 and f <= 5,
    #     "Dorthonoin": lambda h, f: h >= 12 and f <= 7,
    # }
    # # h = int(input())
    # # f = int(input())
    # h = 12
    # f = 12
    # print("".join([nom for nom, test in arbres.items() if test(h, f)]))
    # print((lambda h, f: h <= 5 and f >= 8)(h, f))
    # print(list(arbres.keys()))
    # print([nom for nom, test in arbres.items() if test(h, f)])
    #################################
    # js = int(input())
    # data = [int(input()) for _ in range(js)]
    # print(sum(x for x in data if x > 0), sum(-x for x in data if x < 0), sep='\'n')

    # print("Tarif", "réduit" if int(input()) < 21 else "plein")

    # fs = {name: int(input()) for name in ["Arignon", "Evaran"]}
    # print(fs)
    # if abs(fs["Arignon"] - fs["Evaran"]) > 10 :
    #     print ("La famille", max(fs, key=fs.get), "a un champ trop grand")

    # Socles pour statues
    # print(sum(list(i**2 for i in range(int(input()), int(input()) - 1, -1))))
    # print(*range(100, -1, -1), "Décollage !", sep="\n")
    # print("Partie de cache-cache", *range(1, 11), "J'arrive !", sep="\n")

    # kms parcourus en 1j, 2j et 3j pour 3 disciplines
    # print(*list((2 + 34 + 6) * i for i in range(1, 4)))

    # # Parcours une damier lxl une seule fois par case et retour pos de départ
    # l = 4
    # h, b, d, g = "haut", "bas", "droite", "gauche"
    # # Génération des commandes
    # mvs = [(h, l - 1), (d, l - 1), (b, 1)]
    # for go_down in range((l - 2) // 2):
    #     mvs.extend([(g, l - 2), (b, 1), (d, l - 2), (b, 1)])
    # mvs.append((g, l - 1))
    # # Exécution des mouvements
    # for mv in [sens for sens, n in mvs for _ in range(n)]:
    #     # eval(mv + "()")
    #     print(mv + "()")
    # print()

    # taille = 4
    # tours = taille**2 // 4
    # while tours > 0:
    #     tours -= 1
    #     print(tours)
    #     for mvt in ["haut", "droite", "bas", "gauche"]:
    #         eval(mvt + "()")
    #     print()

    # # 108 tours de 13 kms
    # for _ in range(108):
    #     for mvt in ["haut", "droite", "bas", "gauche"]:
    #         for _ in range(13):
    #             eval(mvt + "()")
    #         print()

    # for mvt in [["haut", "droite"], ["gauche", "bas"]]:
    #     for _ in range(2):
    #         eval(mvt[0] + "()")
    #         eval(mvt[1] + "()")

    # taille = 40
    # for l in range(taille):
    #     for r in range(taille // 2):
    #         print("XO" if l % 2 else "OX", end="")
    #     print()

    # for l in range(ord("a"), ord("z") + 1):
    #     for _ in range(3):
    #         print(chr(l) + "_", end="")
    #     print()
    exit()
