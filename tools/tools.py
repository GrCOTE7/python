from calendar import c
from stat import SF_IMMUTABLE
import os, sys, inspect, locale, shutil
from matplotlib import lines
from pyparsing import line
from time import sleep, time

from globals import *
from main_tools import *

from sub_tools import pf, tbl

# Initalisation des variables globales dans globals.py

# Pour installer les librairies nécessaires🧮
# pip install -r requirements.txt

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


if __name__ == "__main__":

    # sleep(sleepDuration)

    cls()  # 2ar tester aussi dans cas simulatedW
    # cls("un très long titre")
    # cls(0)

    a = 2
    b = 3
    c = [a + b]
    pf("a,b,c")
    ls()
    sleep(sleepDuration)

    exit()  # 2ar

    a = 1
    b = "2"
    c = [1, 5]
    d = a + int(b)
    e = (1, 2, 3, 4, "555")
    f = {4, 5, 4, 6}
    g = range(5)
    pf("a, b, c, d")

    bidon()

    exit()  # 2ar

    ls()
    exit()  # 2ar

    pf("a, b, c, d, e, f, g")
    exit()  # 2ar

    t1 = [1, 2, 3]
    t2 = (4, 5, 6)
    t3 = {4, 5, 4, 6}
    pf("t1, t2, t3")
    ls()

    exit()  # 2ar

    # pf("list(zip(t1, t2))")  # pf("*(list(zip(t1, t2)))")
    print(*list(zip(t1, t2)))  # pf("*(list(zip(t1, t2)))")

    # sleep(sleepDuration)

    print("Début script...\n")

    # sl()
    # sl(blue)
    # sl(green, 70)
    # sl(cyan)
    # sl(french)
    # print("uuuuuuuuuuu")
    # sl(french, 20)
    # sl("french", 30)

    # txt = txtO = lorem.paragraph()
    # pf("len(txt)")
    # print(txt + "\n")

    txt = txtO = (
        "Mon très très très long Titre /root/chemin/sousdossier/exemples/laOuIci"
    )
    from text_tools import textwrap

    txt = textwrap.fill(txt, width=55)
    print(txt)

    # print(*(range(1, 8)))  # print(*[range(5)])

    sleep(sleepDuration)

    exit()  # 2ar

    sleep(sleepDuration)
    data = [
        ("lg", "Simple ligne sans info"),
        ("sb", "Déclenche mise en gras"),
        ("eb", "Stoppe  mise en gras"),
        # ("get_caller_function()", "→ fct() appelante"),
        # ("caller_info()", "→ Chemin, Origine, N° ligne"),
        # ("cls()", "Reset CLI et affiche titre"),
        # ("pf()", "Nom variable et valeur"),
        # ("exit()", "Arrête le script"),
        # ("chono", "Décorateur pour chrono"),
        # ("nf()", "'Formate un nombre"),
        ("ls()", "Pose une ligne séparatrice"),
    ]
    headers = ["Variable ou Fonction".center(10), "Action".center(10)]

    tbl(
        data,
        headers,
        # indexes=True,
    )
    print(f"{'→ = Retourne': >52}{' '*3}", end="")

    n = 123456.789
    print("\nDans le code:", "n =", n)
    sleep(sleepDuration)

    print('\npf("n")', end=" → (En cyan) :\n\n")
    pf("n")  # Affiche 'n=' et sa valeur en cyan
    sleep(sleepDuration)

    print(
        f"\nnf(n) → {sb}{nf(n): >10}{eb}\n( Nombre formatté 'à la française' ;-) )\n"
    )  # nf: Number format
    sleep(sleepDuration)

    ls()  # Affiche un ligne de séparation avec son numéro dans le script
    print("(Une ligne séparatrice avec juste l'instruction 'ls()')")
    sleep(sleepDuration)

    print("\nReady.\n\n" + "-" * 55)

    sleep(sleepDuration)

    print("\nUn arrêt du script avec juste l'instruction 'exit()' :", end="\r")

    exit()  # Arrête le script et affiche le n° de ligne de l'instruction
