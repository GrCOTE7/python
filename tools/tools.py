from ast import If
from calendar import c
import os, sys, inspect, locale
from time import time, sleep

locale.setlocale(locale.LC_ALL, "fr_FR")

# Pour importer ce tools.py de n'importe quel endroit, autre que même parent:
# Adapter le nomber de .parent selon la profondeur du script

# from pathlib import Path

# tools_path = Path(__file__).parent.parent.parent.parent.parent / "tools"
# sys.path.append(str(tools_path))
# from tools import dg, fg, lg, cls, exit, pf

# cls("APPRENDRE LE PYTHON")

# if __name__ == "__main__":
#     pass
#     Code du script ici
#     exit()

sb = "\033[1m"  # Début gras (Start Bold)
eb = "\033[0m"  # Fin gras (End Bold)
# 0 : noir - 1 : rouge - 2 : vert - 3 : jaune - 4 : bleu - 5 : magenta - 6 : cyan - 7 : blanc
# 3x pour encre, 4x pour fond
# \033[3mItalique\033[23m)
# \033[4mSouligné\033[24m)
# \033[3;4mSouligné & Italique\033[23;24m)


def get_caller_function():
    stack = inspect.stack()
    if len(stack) > 2:  # Vérifie qu'il y a une fonction appelante
        caller_frame = stack[2]
        caller_function = caller_frame.function  # Récupère le nom de la fonction
        return caller_function
    return None


def caller_info(justeFielmName=None):
    # Obtenir le cadre deux niveaux au-dessus dans la pile
    frame = inspect.currentframe().f_back.f_back
    # Obtenir le chemin complet du fichier appelant
    callerFilePath = os.path.relpath(inspect.getfile(frame))  # Chemin relatif
    # Obtenir le numéro de ligne
    callerLineNumber = frame.f_lineno
    # Nom de la fonction appelante
    function_name = frame.f_code.co_name
    context = "main" if function_name == "<module>" else f"{function_name}()"

    if justeFielmName:
        return callerFilePath
    return callerFilePath, context, callerLineNumber


def cls(title=None, fileName=""):
    "Réinitialise la console"

    width = 57
    caller = get_caller_function()
    hightlighted = "\033[0;33;40m"  # Mise En Avant (0: Gras + couleurs jaune)
    normalInk = "\033[0;37;40m"

    os.system("cls" if os.name == "nt" else "clear")  # 2ar

    # title = title or "Script Python"
    if title is None:
        title = "Script Python"
        fileName = caller_info(1)

    title = title[0].upper() + title[1:]

    if fileName:
        width = 71
        fileName = f" (\033[3;4m{fileName}\033[23;24m)"

    print(
        f"{hightlighted}"
        + "-" * 55
        + "\n{0: ^{width}}\n".format(title + fileName, width=width)
        + "-" * 55
        + f"{normalInk}"
    )


def pf(var: str):
    """Affiche la (str) 'var' et sa valeur = prinf(f'{var}=') en cyan"""

    lineNumber = caller_info()[2]

    frame = inspect.currentframe().f_back
    value = eval(var, frame.f_globals, frame.f_locals)

    print(f"\033[1;36;40m{var}={value}", end="\n")
    print(f"\033[0;36;40m{' '+'Lg. '+str(nf(lineNumber,0))+' ':-^55}\033[0;37;40m")


def exit():
    print(
        "\n"
        + f'{
            "> exit() - Ligne "
            + str(inspect.currentframe().f_back.f_lineno)
            + ".\n"
        :=>56}',
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


def ls():
    (callerFile, context, lineNumber) = caller_info()
    s = f" L.: \033[1m{nf(lineNumber, 0)}\033[0m - {context} - F.: {callerFile}"
    print(f"{s:→>63}")  # (lineNumber cal, callerFunction,lerFile)


# 2fix tb(data, headers) (using tabulate)

if __name__ == "__main__":

    # sleep(1) # 2ar

    # print()
    cls()
    # cls("Module Outils", "tools")  # Reset l'affichage de la console
    sleep(1)

    n = 123456.789
    print("\nDans le code:", "n =", n)
    sleep(1)

    print('\npf("n")', end=" → (En cyan) :\n\n")
    pf("n")  # Affiche 'n=' et sa valeur en cyan
    sleep(1)

    print(
        f"\nnf(n) → {sb}{nf(n): >10}{eb}\n( Nombre formatté 'à la française' ;-) )\n"
    )  # nf: Number format
    sleep(1)

    ls()  # Affiche un ligne de séparation avec son numéro dans le script
    print("(Une ligne séparatrice avec juste l'instruction 'ls()')")
    sleep(1)

    print("\nReady.\n\n" + "-" * 55)

    sleep(1)

    print("\nUn arrêt du script avec juste l'instruction 'exit()' :", end="\r")
    exit()  # Arrête le script et affiche le n° de ligne de l'instruction
