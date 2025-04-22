# 2do https://www.youtube.com/results?search_query=tuto+python+en+fran%C3%A7ais
import os, sys


def cls(title="module CLS"):

    # Réinitialiser la console
    os.system("cls" if os.name == "nt" else "clear")
    # print()

    mea = "\033[0;33;40m"  # Mise En Avant (0: Gras + couleurs)
    normal = "\033[0;37;40m"
    # 0 : noir - 1 : rouge - 2 : vert - 3 : jaune - 4 : bleu - 5 : magenta - 6 : cyan - 7 : blanc
    # 3x pour encre, 4x pour fond

    print(f"{mea}" + "-" * 55)
    print("{0: ^55}".format(title[0].upper() + title[1:]))
    print("-" * 55 + f"{normal}")
    print()
    # print()
    # print("-" * 55)


# from modules.fibo import fib, fib2

if __name__ == "__main__":

    cls()
    print("Ready.\n\n" + "-" * 55)
