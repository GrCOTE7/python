from re import LOCALE
from stat import SF_IMMUTABLE
import os, sys, inspect, locale, shutil
from tkinter import N
from matplotlib import lines
from pyparsing import line
from time import sleep, time

from globals import *

# # 2ar
# simuCliW = 40
# cliWMsgF = None


def setMsg(txt, **args):
    """<str> content,\n
    Option: <int> type (0 = info (default), 1 = centered, 2 = alert)
    """
    global cliWMsg
    if not txt:
        print("⚠️ Aucun message fourni !")
        return

    cliWMsg = txt


def cliWAnalysis():

    # print(
    #     f"{str(cliW) +' // '+str(cliWR)} - Analyse CLIW: {sb}{'SIMU' if simuCliW else 'RÉEL'}{eb}".center(
    #         cliWR
    #     )
    #     + "\n"
    # )

    def withMsg(simuDecal: int = 0):
        realMsg = f"\033[3;36mReal CLI Width \033[0m"
        nbCols = f": {nbCliCols(cliWR, red)[1:-1]}"
        ideal = f"(\033[3;37mIdeal: {sb}{idealCliWs.start} → {idealCliWs.stop-1}{eb})"

        shortStr = realMsg + ideal + nbCols
        longStr = realMsg + nbCols + "\n" + ideal
        msgL, decal = rawStrLength(shortStr)

        # print(msgL, decal, rawStrLength(ideal))

        s = (
            shortStr.center(cliWR + decal - 1 - simuDecal)
            if msgL <= cliWR
            else (realMsg + nbCols).center(cliWR + decal - 16 - simuDecal)
            + "\n"
            + " " * 6
            + ideal.center(cliWR + 2 + simuDecal)
        )
        return s

    if not simuCliW and cliWR not in idealCliWs:
        s = withMsg()

    elif simuCliW <= cliWR:

        traitRefChiffred = (
            "-" * (simuCliW // 2 - 3)
            + " "
            + f"{sb+str(simuCliW)+eb: >4}"
            + " "
            + "-" * (simuCliW // 2 - 3)
        ).center(cliWR)
        traitRef = ("-" * simuCliW).center(cliWR)
        s = "\033[1;2;3;30;45m SIMU \033[0;31m" + withMsg(6) + "\n" + traitRefChiffred
    else:
        s = (
            frenchLine()
            + f"⚠️ : Your {sb}CLI has a simulated width of {eb} {nbCliCols(simuCliW)[1:-1]} \033[1;31mBIGGER{eb} as it {sb}real width!{eb} {nbCliCols(cliWR)}:\n\033[1;34m→ Faux \033[0;37mproblèmes d'apparence \033[1;31mpossibles...\033[0;37m\n"
            + frenchLine()
        )
    setMsg(s)


def cls(title=None, filename=""):
    """Réinitialise la console
    Affiche title sauf si title=0
    """

    os.system("cls" if os.name == "nt" else "clear")

    cliWAnalysis()

    if title != 0:
        setTitle(title, filename)


def nf(f, dec=2):
    "Number Format 123456789 → 123 456,79"
    format_str = "%." + str(dec) + "f"
    return locale.format_string(format_str, f, grouping=True)


def caller_info(justfilename: bool = False) -> tuple | str:
    """
    Return (tuple) Path of caller file, caller function name, index of line where is the instruction.\nIf argument is True (or 1): (str) Just theCcller file name
    """
    # Obtenir le cadre deux niveaux au-dessus dans la pile
    
    frame = inspect.currentframe().f_back.f_back.f_back
    # Obtenir le chemin complet du fichier appelant
    callerFilePath = os.path.relpath(inspect.getfile(frame))  # Chemin relatif
    # Obtenir le numéro de ligne
    callerLineNumber = frame.f_lineno
    # Nom de la fonction appelante
    function_name = frame.f_code.co_name
    context = "main" if function_name == "<module>" else f"{function_name}()"

    if justfilename:
        # return callerFilePath # 2ar vérif si dessous ok
        return os.path.basename(callerFilePath)
    return callerFilePath, context, callerLineNumber


def get_caller_function() -> str | None:
    """Return caller function if exists"""
    stack = inspect.stack()
    if len(stack) > 2:  # Vérifie qu'il y a une fonction appelante
        caller_frame = stack[2]
        caller_function = caller_frame.function  # Récupère le nom de la fonction
        return caller_function
    return None


def rawStrLength(s: str) -> tuple:
    """Lenght without color codes ou {sb} or {eb}\n
    Return (tuple) Length without color codes, length of color codes)
    Sum of these data is complete length
    """
    import re

    s_ori = len(s)
    # Regex pour supprimer les séquences \033[...m et {sb}, {eb}
    cleanedStr = len(re.sub(r"\033\[[0-9;]*m|{sb}|{eb}", "", s))
    return (cleanedStr, s_ori - cleanedStr)


def nbCliCols(n, color=white):
    return f"(\033[1;3{color}m{n}\033[0;3;3{color}m cols{eb})"


def sl(color: str | None = None, w: int = cliW, toPrint: bool = True) -> str | None:
    """Simple Line\nparal: blue, red, ... or french"""
    global lineColor

    if color == "french":
        lineCode = frenchLine()
    else:
        lineColor = color if color else green if cliWR in idealCliWs else red
        lineCode = f"\033[0;3{lineColor};40m" + "─" * w + "\033[0;37;40m"

    if toPrint:
        print(lineCode)
        return None
    else:
        return lineCode


def frenchLine(w: int | None = cliWR) -> str:
    """w is None | w != cliWR Print a blue-white-red line"""

    def partsLength(totalLength: int) -> tuple:
        """Calculate pure length of each part (tuple) first and third (egal), central part"""
        a = totalLength // 3
        if totalLength % 3 == 0:  # Cas où n = 1, 4, 7,...
            b = a
        elif totalLength % 3 == 1:  # Cas où n = 2, 5, 8,...
            b = a + 1
        else:  # Cas où n = 3, 6, 9,...
            a += 1
            b = a - 1
        return (a, b)

    # w = 21
    pL = partsLength(w)  # (a, b) patriotPartLength
    # print("w =", w, "→", *pL, pL[0])
    # print("-" * 65 + "8888")

    colorsCodes = [4, 7, 1, 7]

    endsLine = "─" * pL[0]
    centerLine = "─" * pL[1]

    endColors = ""
    (partBlue, partWhite, partRed, endColors) = (
        "\033[1;34m" + endsLine,
        "\033[1;37m" + centerLine,
        "\033[1;31m" + endsLine,
        "\033[0;37m" + endColors,
    )
    sFinale = partBlue + partWhite + partRed + endColors

    # print(partBlue, len(partBlue), "(partBlue)")
    # print(partWhite, len(partWhite), "(partWhite)")
    # print(partRed, len(partRed), "(partRed)")
    # print(endColors, len(endColors), "(endColors)")
    # print(
    #     sFinale,
    #     len(partBlue + partWhite + partRed + endColors),
    #     "(partBlue + partWhite + partRed + endColors)",
    # )

    # print(len(sFinale), "(len(sFinale))")
    # print(rawStrLength(sFinale), "(rawStrLength(sFinale))")

    # print("\n" + "-" * 21, "21", "(Réfce.)")
    # name = " Lionel "

    # complete = sFinale + name

    # print(
    #     sFinale + name,
    #     rawStrLength(sFinale + name),
    #     "(sFinale + name)",
    # )
    return sFinale
    exit()  # 2ar


def setTitle(title=None, filename=""):

    title = title or "Script Python"
    formatted_title = f"\033[1;33m{title[0].upper()}{title[1:]}\033[0;37m"

    filename = filename or caller_info(1)
    # filename = "(main_tools.py)(main_tools.py)(main_tools.p)"
    formatted_filename = f"(\033[3;4;37m{filename}\033[23;24;37m)"

    title_lengths = [
        rawStrLength(part) for part in (formatted_title, formatted_filename)
    ]
    total_pure_length = sum(length[0] for length in title_lengths)
    total_codes_length = sum(length[1] for length in title_lengths)

    statusLine = sl(w=cliWR, toPrint=False)
    print(statusLine)
    if total_pure_length <= cliWR:
        complete_title = f"{formatted_title} {formatted_filename}"
        print(f"{complete_title:^{cliWR + total_codes_length+1}}", end="\b")
    else:
        print(
            f"{formatted_title:^{cliWR + title_lengths[0][1]}}{formatted_filename:^{cliWR + title_lengths[1][1]+1}}",
            end="\b",
        )
    print(statusLine)


def showMsg(
    msg: str | tuple, color: int | str | None = 0, type: str = "info", w: int = cliW
):
    """Show msg if msg != None\n
    Selon style:
    None (info)\n
    title\n
    alert\n
    """
    # from text_tools import wordWrap

    if color:
        msg = f"\033[{color}m{msg}\033[{color}m"

    print(msg, end="ok")

    # if msg and type(msg) is tuple:
    #     align = "^" if type == "title" else "<"
    #     # msg = wordWrap(msg, w=w, align=align)

    #     if type == "alert":
    #         sl(french)
    #         print(msg)
    #         sl(french)

    #     elif type == "title":
    #         # sl(w=cliWR)
    #         # print(str(msg[0]))
    #         print(msg[0].center(cliWR))
    #         print(msg[1].center(cliWR))
    #         print("x".center(cliWR))
    #         print("-" * cliWR)
    #         # ls()
    #         print("FIN TITRE".center(cliWR))
    #         pass


def ls():
    """Draw a line with the line number, function and the caller file."""
    (callerFile, context, lineNumber) = caller_info()
    s = f" \033[1;31;47m L.: {nf(lineNumber, 0)} \033[0;37;40m - {context} - F.: {callerFile}"
    textLength = rawStrLength(s)
    # pf("cliW, textLength")
    trait = sl(w=cliWR - textLength[0], toPrint=False)

    print(trait + s)
    # print("-" * cliW, "Réf.")


def exit():

    complExitMsg = (
        ""
        if cliW not in idealCliWs or simuCliW
        else f" - \033[3;35m" + "CLI: " + nbCliCols(cliW, magenta)[1:-5] + "\033[0m"
    )

    s = (
        "> exit() - Line "
        + sb
        + str(inspect.currentframe().f_back.f_lineno)
        + eb
        + complExitMsg
    )

    print(f"\n\033[0;32m{s:=>{cliWR+rawStrLength(s)[1]}}\033[0;37m")

    if cliWMsg:
        print(cliWMsg)

    try:
        sleep(sleepDuration)
        pf("cliW, simuCliW, cliWR")  # 2ar
    except:
        pass
        print(f"\033[1;31mNo pf() !!!{eb}")

    sys.exit()


if __name__ == "__main__":
    sleep(sleepDuration)
    # # 2ar titre à tester aussi dans cas simulatedW ces 3 cas

    # exit()
    cls("un long long Titre")

    # cls()
    # cls(0)
    sleep(sleepDuration)

    exit()  # 2ar
    # t1 = [1, 2, 3]
    # t2 = (4, 5, 6)
    # t3 = {4, 5, 4, 6}
    # pf("t1, t2, t3")
    # pf("list(zip(t1, t2))")  # pf("*(list(zip(t1, t2)))")
    # print(*list(zip(t1, t2)))  # pf("*(list(zip(t1, t2)))")

    exit()  # 2ar
    # sleep(sleepDuration)

    print("Début script...\n")

    exit()  # 2ar
    # sl()
    # sl(blue)
    # sl(green, 70)
    # sl(cyan)
    # sl(french)
    # print("uuuuuuuuuuu")
    # sl(french, 20)
    # sl("french", 30)
    exit()  # 2ar

    # txt = txtO = lorem.paragraph()
    # pf("len(txt)")
    # print(txt + "\n")
    exit()  # 2ar

    txt = txtO = (
        "Mon très très très long Titre /root/chemin/sousdossier/exemples/laOuIci"
    )
    from text_tools import textwrap

    txt = textwrap.fill(txt, width=55)
    print(txt)

    # print(*(range(1, 8)))  # print(*[range(5)])

    sleep(sleepDuration)

    exit()  # 2ar

    # sleep(sleepDuration)
    # data = [
    #     ("lg", "Simple ligne sans info"),
    #     ("sb", "Déclenche mise en gras"),
    #     ("eb", "Stoppe  mise en gras"),
    #     # ("get_caller_function()", "→ fct() appelante"),
    #     # ("caller_info()", "→ Chemin, Origine, N° ligne"),
    #     # ("cls()", "Reset CLI et affiche titre"),
    #     # ("pf()", "Nom variable et valeur"),
    #     # ("exit()", "Arrête le script"),
    #     # ("chono", "Décorateur pour chrono"),
    #     # ("nf()", "'Formate un nombre"),
    #     ("ls()", "Pose une ligne séparatrice"),
    # ]
    # headers = ["Variable ou Fonction".center(10), "Action".center(10)]

    # tbl(
    #     data,
    #     headers,
    #     # indexes=True,
    # )
    # print(f"{'→ = Retourne': >52}{' '*3}", end="")

    # n = 123456.789
    # print("\nDans le code:", "n =", n)
    # sleep(sleepDuration)

    # print('\npf("n")', end=" → (En cyan) :\n\n")
    # pf("n")  # Affiche 'n=' et sa valeur en cyan
    # sleep(sleepDuration)

    # print(
    #     f"\nnf(n) → {sb}{nf(n): >10}{eb}\n( Nombre formatté 'à la française' ;-) )\n"
    # )  # nf: Number format
    # sleep(sleepDuration)

    # ls()  # Affiche un ligne de séparation avec son numéro dans le script
    # print("(Une ligne séparatrice avec juste l'instruction 'ls()')")
    # sleep(sleepDuration)

    # print("\nReady.\n\n" + "-" * 55)

    # sleep(sleepDuration)

    # print("\nUn arrêt du script avec juste l'instruction 'exit()' :", end="\r")

    exit()  # Arrête le script et affiche le n° de ligne de l'instruction
