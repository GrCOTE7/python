from re import LOCALE
from stat import SF_IMMUTABLE
import os, sys, inspect, locale, shutil
from tkinter import N
from matplotlib import lines
from pyparsing import line
from time import sleep, time
from tabulate import tabulate

from globals import *

# 2ar pour tests ponctuels
# SIMU_CLIW = 40
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


def refSimu(center=False, toPrint=True):
    if not SIMU_CLIW:
        return
    else:
        centered = ".center(CLIWR)" if center else ""
        traitRefChiffred = (
            "-" * (SIMU_CLIW // 2 - 2)
            + " "
            + f"{str(SIMU_CLIW): ^{2+SIMU_CLIW%2}}"
            + " "
            + "-" * (SIMU_CLIW // 2 - 2)
        )
    tRC = traitRefChiffred.center(CLIWR) if center else traitRefChiffred
    if toPrint:
        print(tRC)
    else:
        return tRC


def cliWAnalysis():

    realMode = 0 if SIMU_CLIW else 1
    ideal = CLIW in IDEAL_CLIWS

    # print(
    #     f"{str(CLIW) +' // '+str(CLIWR)} - Analyse CLIW: {SB}{'SIMU' if not realMode else 'RÉEL'}{EB} and {SB}{'IDEAL' if ideal else 'NOT IDEAL'}{EB}".center(
    #         CLIWR
    #     )
    #     + "\n"
    # )

    def withMsg(simuDecal: int = 0):
        realMsg = f"\033[3;36mReal CLI Width \033[0m"
        nbCols = f": {nbCliCols(CLIWR, RED)[1:-1]}"
        ideal = f"(\033[3;37mIdeal: {SB}{IDEAL_CLIWS.start} → {IDEAL_CLIWS.stop-1}{EB})"

        shortStr = realMsg + ideal + nbCols
        longStr = realMsg + nbCols + "\n" + ideal
        msgL, decal = rawStrLength(shortStr)

        # print(msgL, decal, rawStrLength(ideal))

        s = (
            shortStr.center(CLIWR + decal - 1 - simuDecal)
            if msgL <= CLIWR
            else (realMsg + nbCols).center(CLIWR + decal - 16 - simuDecal)
            + "\n"
            + " " * 6
            + ideal.center(CLIWR + 2 + simuDecal)
        )
        return s

    if realMode and ideal:
        return

    elif not realMode and SIMU_CLIW > CLIWR:
        s = (
            frenchLine()
            + f"⚠️ : Your {SB}CLI has a simulated width of {EB} {nbCliCols(SIMU_CLIW)[1:-1]} \033[1;31mBIGGER{EB} as it {SB}real width!{EB} {nbCliCols(CLIWR)}:\n\033[1;34m→ Faux \033[0;37mproblèmes d'apparence \033[1;31mpossibles...\033[0;37m\n"
            + frenchLine()
        )
    elif not realMode:
        s = "\033[1;2;3;30;45m SIMU \033[0;31m " + withMsg(6) + "\n" + refSimu(1, 0)
    else:
        s = withMsg()

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
    try:
        f = float(f)
        return locale.format_string(f"%.{dec}f", f, grouping=True)
    except ValueError:
        src = caller_info()
        # print(src)
        print(
            f"⚠️ Errorfor nf() in main_tools:\n\033[1;31mBad data type ({type(f).__name__}) -> {f} (Line {src[2]} in {src[0]}){EB}"
        )
        return str(f)


def caller_info(justfilename: bool = False, level=2) -> tuple | str:
    """
    Return (tuple) Path of caller file, caller function name, index of line where is the instruction.\nIf argument is True (or 1): (str) Just theCcller file name
    """

    frame = inspect.currentframe()

    # Vérifier la profondeur de la pile avant d'accéder à f_back plusieurs fois
    for _ in range(level):
        if frame is not None and frame.f_back is not None:
            frame = frame.f_back
        else:
            return "Frame introuvable"

    # Vérifier si frame est toujours valide avant de l'utiliser
    if frame is None:
        return "Frame introuvable"

    try:
        callerFilePath = os.path.relpath(inspect.getfile(frame))  # Chemin relatif
    except TypeError:
        return "Impossible de récupérer le fichier appelant"
    # Obtenir le numéro de ligne
    # callerLineNumber = frame.f_lineno
    callerLineNumber = int(frame.f_lineno) if frame is not None else -1

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


def nbCliCols(n, color=WHITE):
    return f"(\033[1;3{color}m{n}\033[0;3;3{color}m cols{EB})"


def sl(
    color: str | None = None,
    w: int = CLIW,
    trait="─",
    finTrait="",
    toPrint: bool = True,
) -> str | None:
    """Simple Line\nparm: BLUE, RED, ... or FRENCH"""
    global lineColor

    if color == "french":
        lineCode = frenchLine(trait=trait)
    else:
        lineColor = color if color else GREEN if CLIWR in IDEAL_CLIWS else RED
        lineCode = (
            f"\033[0;3{lineColor};40m" + f"{trait}{finTrait}" * w + "\033[0;37;40m"
        )

    if toPrint:
        print(lineCode)
        return None
    else:
        return lineCode


def frenchLine(
    w: int | None = CLIWR,
    trait="─",
) -> str:
    """w is None | w != CLIWR Print a BLUE-WHITE-RED line"""

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

    endsLine = f"{trait}" * pL[0]
    centerLine = f"{trait}" * pL[1]

    endColors = ""
    (partBlue, partWhite, partRed, endColors) = (
        "\033[1;34m" + endsLine,
        "\033[1;37m" + centerLine,
        "\033[1;31m" + endsLine,
        "\033[0;37m" + endColors,
    )
    sFinale = partBlue + partWhite + partRed + endColors

    # print(partBlue, len(partBLUE), "(partBLUE)")
    # print(partWHITE, len(partpartWhiteWHITE), "(partWHITE)")
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
    formatted_title = f"\033[0;33m{title[0].upper()}{title[1:]}\033[0;37m"

    filename = filename or caller_info(1, level=3)
    formatted_filename = f"(\033[3;4;37m{filename}\033[23;24;37m)"

    title_lengths = [
        rawStrLength(part) for part in (formatted_title, formatted_filename)
    ]
    total_pure_length = sum(length[0] for length in title_lengths)
    total_codes_length = sum(length[1] for length in title_lengths)

    statusLine = sl(w=CLIWR, toPrint=False)
    print(statusLine)
    if total_pure_length <= CLIWR:
        complete_title = f"{formatted_title} {formatted_filename}"
        print(f"{complete_title:^{CLIWR + total_codes_length+1}}", end="\b")
    else:
        print(
            f"{formatted_title:^{CLIWR + title_lengths[0][1]}}{formatted_filename:^{CLIWR + title_lengths[1][1]+1}}",
            end="\b",
        )
    print(statusLine)


def showMsg(
    msg: str | tuple, color: int | str | None = 0, type: str = "info", w: int = CLIW
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
    #         # sl(w=CLIWR)
    #         # print(str(msg[0]))
    #         print(msg[0].center(CLIWR))
    #         print(msg[1].center(CLIWR))
    #         print("x".center(CLIWR))
    #         print("-" * CLIWR)
    #         # ls()
    #         print("FIN TITRE".center(CLIWR))
    #         pass


# 2do lien clicable comme erreurs
def ls(color=YELLOW, level=2, **kwargs):
    """Draw a line with the line number, function and the caller file."""
    # print("kwargs = ", kwargs)  # Pour debug
    color = kwargs.get("color", YELLOW) if color is None else color
    toPrint = kwargs.get("toPrint", True)

    (callerFile, context, lineNumber) = caller_info(level=level)
    # context = "ABCDEFGHIJKL"
    # callerFile = "ahcestmontoolsunpeulong\main_tools.py"
    s = f"\033[0;3{color}m{context}𐍈𐍈𐍈F.: {callerFile}:\033[1;31;47m{lineNumber}{EB}"
    textLength = rawStrLength(s)
    traitL = CLIWR - textLength[0] - 1

    multiLine = 0
    # traitL2 = CLIW - textLength[0] - 1
    if traitL < 0:
        traitL = CLIWR // 2
        ss = s.split("𐍈𐍈𐍈")
        ss1L = rawStrLength(ss[1])[1]
        s = s.replace("𐍈𐍈𐍈", "\n")
        multiLine = 1
    else:
        s = s.replace("𐍈𐍈𐍈", " - ")
    trait = f"\033[0;3{color}m" + "─" * traitL + " "

    # print(
    #     f"{sb}{level=} | {textLength[0]=} | {CLIW=} | {SIMU_CLIW=} |{CLIWR=} | {len(trait)=} avec codes & 1 space"
    # )

    s = (
        "\n" + trait + s
        if not multiLine
        else trait + ss[0] + "\n" + f"{'→ '+ ss[1]: >{CLIWR +ss1L}}" + "\n"
    )
    return s if not toPrint else print(s)

    # refSimu()

    # Juste une ls() rapide pour DEBUG la fonction... ls() !
    # (callerFile, context, lineNumber) = caller_info(level=1)
    # s4Debugls = (
    #     f"DEBUG \033[3;31m{context} - F.: {callerFile}:\033[1;31;47m{lineNumber}{eb}"
    # )
    # print("" + s4Debugls.center(CLIWR + rawStrLength(s4Debugls)[1]))

    # print("-" * CLIW, "Réf.")


def tbl(
    data,
    headers=[],
    colalign=None,
    indexes=False,
    tablefmt="rounded_outline",
):
    tabulate.WIDE_CHARS_MODE = False
    tabulate.PRESERVE_WHITESPACE = True
    if colalign is None:
        colalign = ["center"] * len(headers)  # Alignement à gauche par défaut
    print(
        tabulate(
            data,
            headers,
            colalign=colalign,
            maxcolwidths=[None, 55],
            tablefmt=tablefmt,
            showindex=indexes,
        )
    )


def exit():

    complExitMsg = (
        ""
        if CLIW not in IDEAL_CLIWS or SIMU_CLIW or CLIW == 55
        else f"(\033[3;35m" + nbCliCols(CLIW, MAGENTA)[1:-8] + ".\033[0;32m)" + ES
    )

    (callerFile, context, lineNumber) = caller_info(level=2)

    s1 = f"EXIT{complExitMsg}\033[0;32m:"
    s2 = f"{context} - F.: {callerFile}:\033[1;31;47m{lineNumber}{EB}"

    n = CLIWR - rawStrLength(s1)[0] - rawStrLength(s2)[0] - 3
    trait = f"\n\033[0;3{GREEN}m" + "=" * abs(n) + ">"
    print(
        f"{trait} {s1} {s2}"
        if n > 0
        else f"{trait} {s1}\n{s2: >{CLIWR+rawStrLength(s2)[1]}}"
    )

    if cliWMsg:
        print(cliWMsg)
        # print(f"{'*' *45}".center(66))
        # ls()

    try:
        sleep(SLEEP_DURATION)
        pf("CLIW, SIMU_CLIW, CLIWR")  # 2ar
    except:
        pass
        # print(f"\033[1;31mNo pf() !!!{EB}")

    sys.exit()


def bidon():
    s = "bidon"
    print("Bidon")
    ls()


if __name__ == "__main__":

    cls("Main TOOLS")

    print("Début script →\n")

    [print(f"Code couleur {c}: ", ls(c, toPrint=0)) for c in range(8)]

    print(f"\n{'← Fin script': >{CLIWR}}")

    exit()  # 2ar

    # colors = [BLUE, WHITE, RED, CYAN, MAGENTA, YELLOW, GREEN, BLACK]
    # print([c for c in colors])
    # [ls(color=c) for c in colors]
    # s = sl(CYAN, w=CLIWR // 2, toPrint=0)
    # print(s.center(CLIWR + rawStrLength(s)[1]))

    if 0:  # 2ar Activer aprè_s pf() OK et finir tests dessous
        sleep(SLEEP_DURATION)

        cls()
        cls(0)

        t1 = [1, 2, 3]
        t2 = (4, 5, 6)
        t3 = {4, 5, 4, 6}
        pf("t1, t2, t3")
        pf("list(zip(t1, t2))")  # pf("*(list(zip(t1, t2)))")
        ls()
        print(*list(zip(t1, t2)))  # pf("*(list(zip(t1, t2)))")

        exit()  # 2ar
    # sleep(SLEEP_DURATION)

    sl()
    sl(BLUE)
    sl(GREEN, 70)
    sl(CYAN)
    sl(FRENCH)
    # print("uuuuuuuuuuu")
    # sl(FRENCH, 20)
    # sl("FRENCH", 30)
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

    sleep(SLEEP_DURATION)

    exit()  # 2ar

    # sleep(SLEEP_DURATION)
    # data = [
    #     ("LG", "Simple ligne sans info"),
    #     ("SB", "Déclenche mise en gras"),
    #     ("EB" ou "ES", "Stoppe mise en gras le style"),
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
    # sleep(SLEEP_DURATION)

    # print('\npf("n")', end=" → (En cyan) :\n\n")
    # pf("n")  # Affiche 'n=' et sa valeur en cyan
    # sleep(SLEEP_DURATION)

    # print(
    #     f"\nnf(n) → {sb}{nf(n): >10}{eb}\n( Nombre formatté 'à la française' ;-) )\n"
    # )  # nf: Number format
    # sleep(SLEEP_DURATION)

    # ls()  # Affiche un ligne de séparation avec son numéro dans le script
    # print("(Une ligne séparatrice avec juste l'instruction 'ls()')")
    # sleep(SLEEP_DURATION)

    # print("\nReady.\n\n" + "-" * 55)

    # sleep(SLEEP_DURATION)

    # print("\nUn arrêt du script avec juste l'instruction 'exit()' :", end="\r")

    exit()  # Arrête le script et affiche le n° de ligne de l'instruction
