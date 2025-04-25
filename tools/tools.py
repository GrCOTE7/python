# 2do https://www.youtube.com/results?search_query=tuto+python+en+fran%C3%A7ais
import os, sys, inspect, locale
from time import time, sleep

locale.setlocale(locale.LC_ALL, "fr_FR")

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


def chrono(function):
    """Décorateur: Calcule le temps en secondes que met une fonction à s'executer."""

    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # (Le temps "epoch").
        start = time()

        result = function(*args, **kwargs)

        end = time()
        # Différence entre 2 temps "epochs", celui qui est gardé dans "start", et celui qui sera gardé dans "end". ;)
        time_spent = end - start

        # if len(args) > 0:
        #     print(f'{args[0]}: {time_spent:.2f}"')
        # else:
        #     print(f'{time_spent:.2f}"')

        print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")

        return result

    wrapper.__doc__ = function.__doc__
    return wrapper


def nf(f, dec=2):
    "Number Format 123456789 → 123 456,79"
    format_str = "%." + str(dec) + "f"
    return locale.format_string(format_str, f, grouping=True)


if __name__ == "__main__":

    cls()
    # sleep(3)

    n = 123456.789
    print(nf(n))
    print("Ready.\n\n" + "-" * 55)
