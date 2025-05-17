from re import I, L
import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import *
# from tools import cls
from pathlib import Path

from cycler import V

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls, pf

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

    # cls(" france-ioi.org")
    cls("Dial Thomas / PyPRO")
    # from robot import *

    reaction = [
        "Au début, j'comprenais pas trop...",
        "Après, j'crois qu'j'ai compris la vanne...",
        "Et maintenant, j'ai compris :",
        "Mais j'cherche encore le lien qui permet d'acheter cette tablette !!!",
        "Au final: Ha, ha, ha... Merci ! ;-)",
    ]
    soluceThomas = """print("\\n".join(f"\\033[1;33;40m{idx}\\033[0;37;40m: Ok, ok... {txt}" for idx, txt in enumerate(reaction)))"""
    soluceGrCOTE7 = """print(*map(lambda t: f"\b\033[1;33;40m{t[0]}\033[0;37;40m: Ok, ok... {t[1]}\n", enumerate(reaction),)"""
    print("Recherche de la façon la + compacte...:")
    pf("len(soluceThomas),len(soluceGrCOTE7)", 2)
    exit()

    #####################################

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
