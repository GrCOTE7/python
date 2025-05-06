from stat import SF_IMMUTABLE
import os, sys, inspect, locale, shutil
from matplotlib import lines
from pyparsing import line
from time import sleep, time

from globals import *


def cls(title=None, fileName=""):
    """Réinitialise la console
    Affiche title sauf si title=0
    """
    os.system("cls" if os.name == "nt" else "clear")

    if title != 0:
        setTitle(title, fileName)

    alertMsg = "Mon simple message" * 5 + "\n"
    showMsg(alertMsg)
    alertMsg = "Mon cli message" * 5
    showMsg(alertMsg, target="cliWInfo")


def nf(f, dec=2):
    "Number Format 123456789 → 123 456,79"
    format_str = "%." + str(dec) + "f"
    return locale.format_string(format_str, f, grouping=True)


def caller_info(justFileName: bool = False) -> tuple | str:
    """
    Without argument: (tuple) Path of caller file, caller function name, index of line where is the instruction.\nIf argument is True (or 1): (str) Just theCcller file name
    """
    # Obtenir le cadre deux niveaux au-dessus dans la pile
    frame = inspect.currentframe().f_back.f_back
    # Obtenir le chemin complet du fichier appelant
    callerFilePath = os.path.relpath(inspect.getfile(frame))  # Chemin relatif
    # Obtenir le numéro de ligne
    callerLineNumber = frame.f_lineno
    # Nom de la fonction appelante
    function_name = frame.f_code.co_name
    context = "main" if function_name == "<module>" else f"{function_name}()"

    if justFileName:
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


if simuCliW:

    # Showl cliW if SIMU
    cliWMsg = f"Ref1. \033[1;37mSIMU{eb}: CLI with {nbCliCols(cliW)[1:-1]}"

    if simuCliW == cliWR:
        cliWMsgDetails = f"\033[0;37m(As Real)"

    elif simuCliW < cliWR:
        cliWMsgDetails = f" \033[1;3m(" + str(cliWR) + f" \033[0;3mreally" + f"){eb}"

    else:
        cliWMsgDetails = f"⚠️ : Your {sb}CLI has a simulated width of {eb} {nbCliCols(simuCliW)} \033[1;31mBIGGER{eb} as it{sb}real width!{eb} {nbCliCols(cliWR)}:\n"
        cliWMsgDetails = "\033[1;34m→ Faux \033[0;37mproblèmes d'apparence \033[1;31mpossibles...\033[0;37m"

        alertMsg = f"{cliWMsg+cliWMsgDetails: ^{cliWR+rawStrLength(cliWMsgDetails)[1]}}"
    completeCliWMsg = cliWMsg + cliWMsgDetails
    completeCliWMsgL = rawStrLength(completeCliWMsg)[1]

    cliWMsg += cliWMsgDetails + "."
# 0 : noir - 1 : rouge - 2 : vert - 3 : jaune - 4 : bleu - 5 : magenta - 6 : cyan - 7 : blanc
# 3x pour encre, 4x pour fond
# \033[3mItalique\033[23m)
# \033[4mSouligné\033[24m)
# \033[3;4mSouligné & Italique\033[23;24m)


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


def setTitle(title=None, fileName=""):

    showMsg(alertMsg)

    # # 2fix \n si trop ling titre & filename

    title = title or "Script Python"
    title = "\033[1;33m" + title[0].upper() + title[1:] + "\033[0;30m"

    filename = caller_info(1)
    filename = "abcdef777abcdefghijklmnopqrstuvwcyz1234567"  # 2ar
    filename = "abcdef777"  # 2ar
    filename = f"(\033[4m{filename})\033[23;24;37m"

    completeTitle = f"{title} {filename}"
    # compleeTitleLengths = rawStrLength(completeTitle)

    # 2fix \n si trop ling titre & filename

    t = (title, 123, filename)
    showMsg(t, target="title", w=cliWR)
    # showMsg((title, filename), style="title")
    # showMsg((title, filename, "oki"), style="title")


def showMsg(
    msg: str | tuple,
    color: int | str | None = 0,
    target: str = "info",
    w: int = cliW,
):
    """Show msg if msg != None\n
    Selon style:
    None (info)\n
    title\n
    alert\n
    """
    from text_tools import wordWrap

    if color:
        msg = f"\033[{color}m{msg}\033[0;{color}m{cs}"

    if msg and type(msg) == tuple:
        align = "^" if target == "title" else "<"
        msg = wordWrap(msg, w=w, align=align)

        if target == "alert":
            sl(french)
            print(msg)
            sl(french)

        elif target == "title":
            pass
            # sl(w=cliWR)
            # print(str(msg[0]))
            # print("x".center(cliWR))
            # print("-" * cliWR)
            # ls()
            # print("FIN TITRE".center(cliWR))

        elif target == "cliWInfo":
            print(msg)

        else:
            print(msg)

        if target == "alert":
            sl(french)
            print(msg)
            sl(french)

        elif target == "title":
            sl(w=cliWR)
            sl(w=cliWR)
            print(msg)
            sl(w=cliWR)

        elif target == "cliWInfo":
            print(msg)

        else:
            print(msg)


def exit():

    complExitMsg = (
        ""
        if cliW not in idealCliWs
        else f" - \033[3;30m" + "CLI: " + nbCliCols(cliW, black)[1:-5] + "\033[0m"
    )

    s = (
        "> exit() - Line "
        + sb
        + str(inspect.currentframe().f_back.f_lineno)
        + eb
        + complExitMsg
    )
    print(f"\n\033[0;32m{s:=>{cliWR+rawStrLength(s)[1]}}\033[0;37m")

    msg = (
        f"⚠️ : Votre {sb}CLI a une largeur simulée{eb} {nbCliCols(simuCliW)} \033[1;31mSUPÉRIEURE{eb} à sa {sb}largeur réelle{eb} {nbCliCols(cliWR)}:\n"
        + f"{'→ \033[1;31mFaux problèmes d\'apparence possibles\033[0;37m...'.center(cliWR)}"
    )

    w = nbCliCols(cliWR)

    s2 = (
        ""
        if cliWR in idealCliWs
        else f" (\033[3;31mIDEAL: {sb}{idealCliWs.start} → {idealCliWs.stop-1}{eb})"
    )

    s3 = f" - SIMU: {sb}{simuCliW}{eb} cols." if simuCliW else ""

    s = f"\033[3;36mReal CLI width:\033[0m {w[1:-1]}{s2}{s3}"

    print(
        # "CLI width: XXX COL (Simulées / Réelles)\n".center(cliW) + f"{'-'*55}\n" + msg
        ""
        if cliWR in idealCliWs
        else f"{s: ^{cliWR+rawStrLength(s)[1]+1}}"
    )

    if cliWMsg:
        print(f"{cliWMsg: ^{cliW+rawStrLength(cliWMsg)[1]}}")
        print(str("s" * 54).center(60))
        print("r" * cliWR)
        print()

    if alertMsg:
        showMsg(alertMsg)

    # pf("cliW, simuCliW, cliWR") # 2ar

    atuple = (777, "abc")
    alist = [777, "abc"]
    adict = {"a": 777, "b": "abc"}
    # pf("atuple, alist, adict")

    sys.exit()


def ls():
    """Draw a line with the line number, function and the caller file."""
    (callerFile, context, lineNumber) = caller_info()
    s = f" \033[1;31;47m L.: {nf(lineNumber, 0)} \033[0;37;40m - {context} - F.: {callerFile}"
    textLength = rawStrLength(s)
    # pf("cliW, textLength")
    trait = sl(w=cliWR - textLength[0], toPrint=False)

    print(trait + s)
    # print("-" * cliW, "Réf.")


if __name__ == "__main__":

    # sleep(sleepDuration)

    sleep(sleepDuration)
    cls()  # 2ar titre à tester aussi dans cas simulatedW ces 3 cas
    # cls("un très long titre")
    # cls(0)
    sleep(sleepDuration)
    # cls("un très long titre")
    # cls(0)

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
