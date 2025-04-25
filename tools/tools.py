# 2do https://www.youtube.com/results?search_query=tuto+python+en+fran%C3%A7ais
import os, sys, inspect

lg = "\n" + "↔" * 55
dg = "\033[1m"  # Début gras
fg = "\033[0m"  # Fin gras


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


def lineNumber():
    """Renvoie la ligne courante (De l'appel)"""

    try:
        return inspect.currentframe().f_back.f_back.f_lineno
    except:
        return inspect.currentframe().f_back.f_lineno


def pf(var: str):
    """Affiche la (str) 'var' et sa valeur"""
    frame = inspect.currentframe().f_back
    value = eval(var, frame.f_globals, frame.f_locals)
    # print(lg)
    print(f"{var}={value}", end="\n")
    print(f"{' '+'Lg. '+str(lineNumber())+' ':-^55}\n")


def exit():
    print(
        "\n"
        + f'{
            "> exit() - Ligne "
            + str(inspect.currentframe().f_back.f_lineno)
            + ".\b\n"
        :=>55}',
    )
    sys.exit()
