from re import LOCALE
from stat import SF_IMMUTABLE
import os, sys, inspect, locale, shutil
from tkinter import N
from matplotlib import lines
from pyparsing import line
from time import sleep, time

from globals import *

# 2ar pour tests ponctuels
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


def refSimu(center=False, toPrint=True):
    if not simuCliW:
        return
    else:
        centered = ".center(cliWR)" if center else ""
        traitRefChiffred = (
            "-" * (simuCliW // 2 - 2)
            + " "
            + f"{str(simuCliW): ^{2+simuCliW%2}}"
            + " "
            + "-" * (simuCliW // 2 - 2)
        )
    tRC = traitRefChiffred.center(cliWR) if center else traitRefChiffred
    if toPrint:
        print(tRC)
    else:
        return tRC


def cliWAnalysis():

    realMode = 0 if simuCliW else 1
    ideal = cliW in idealCliWs

    # print(
    #     f"{str(cliW) +' // '+str(cliWR)} - Analyse CLIW: {sb}{'SIMU' if not realMode else 'RÉEL'}{eb} and {sb}{'IDEAL' if ideal else 'NOT IDEAL'}{eb}".center(
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

    if realMode and ideal:
        return

    elif not realMode and simuCliW > cliWR:
        s = (
            frenchLine()
            + f"⚠️ : Your {sb}CLI has a simulated width of {eb} {nbCliCols(simuCliW)[1:-1]} \033[1;31mBIGGER{eb} as it {sb}real width!{eb} {nbCliCols(cliWR)}:\n\033[1;34m→ Faux \033[0;37mproblèmes d'apparence \033[1;31mpossibles...\033[0;37m\n"
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
            f"⚠️ Errorfor nf() in main_tools:\n\033[1;31mBad data type ({type(f).__name__}) -> {f} (Line {src[2]} in {src[0]}){eb}"
        )
        return str(f)

    if not isinstance(f, (int, float)):
        return nf(int(f))  # Évite l'erreur en retournant une chaîne
    return locale.format_string(f"%.{dec}f", f, grouping=True)


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


def nbCliCols(n, color=white):
    return f"(\033[1;3{color}m{n}\033[0;3;3{color}m cols{eb})"


def sl(
    color: str | None = None,
    w: int = cliW,
    trait="─",
    finTrait="",
    toPrint: bool = True,
) -> str | None:
    """Simple Line\nparm: blue, red, ... or french"""
    global lineColor

    if color == "french":
        lineCode = frenchLine()
    else:
        lineColor = color if color else green if cliWR in idealCliWs else red
        lineCode = (
            f"\033[0;3{lineColor};40m" + f"{trait}{finTrait}" * w + "\033[0;37;40m"
        )

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

    filename = filename or caller_info(1, level=3)
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


# 2do lien clicable comme erreurs
def ls(level=2, **kwargs):
    """Draw a line with the line number, function and the caller file."""
    # print("kwargs = ", kwargs)  # Pour debug
    color = kwargs.get("color", yellow)

    (callerFile, context, lineNumber) = caller_info(level=level)
    # context = "ABCDEFGHIJKL"
    # callerFile = "ahcestmontoolsunpeulong\main_tools.py"
    s = f"\033[0;3{color}m{context}𐍈𐍈𐍈F.: {callerFile}:\033[1;31;47m{lineNumber}{eb}"
    textLength = rawStrLength(s)
    traitL = cliWR - textLength[0] - 1

    multiLine = 0
    # traitL2 = cliW - textLength[0] - 1
    if traitL < 0:
        traitL = cliWR // 2
        ss = s.split("𐍈𐍈𐍈")
        ss1L = rawStrLength(ss[1])[1]
        s = s.replace("𐍈𐍈𐍈", "\n")
        multiLine = 1
    else:
        s = s.replace("𐍈𐍈𐍈", " - ")
    trait = f"\033[0;3{color}m" + "─" * traitL + " "

    # print(
    #     f"{sb}{level=} | {textLength[0]=} | {cliW=} | {simuCliW=} |{cliWR=} | {len(trait)=} avec codes & 1 space"
    # )
    print(
        trait + s
        if not multiLine
        else trait + ss[0] + "\n" + f"{'→ '+ ss[1]: >{cliWR +ss1L}}" + "\n"
    )
    # refSimu()

    # Juste une ls() rapide pour DEBUG la fonction... ls() !
    # (callerFile, context, lineNumber) = caller_info(level=1)
    # s4Debugls = (
    #     f"DEBUG \033[3;31m{context} - F.: {callerFile}:\033[1;31;47m{lineNumber}{eb}"
    # )
    # print("" + s4Debugls.center(cliWR + rawStrLength(s4Debugls)[1]))

    # print("-" * cliW, "Réf.")


def exit():

    complExitMsg = (
        ""
        if cliW not in idealCliWs or simuCliW or cliW == 55
        else f"(\033[3;35m" + nbCliCols(cliW, magenta)[1:-8] + ".\033[0;32m)" + eb
    )

    (callerFile, context, lineNumber) = caller_info(level=2)

    s1 = f"EXIT{complExitMsg}\033[0;32m:"
    s2 = f"{context} - F.: {callerFile}:\033[1;31;47m{lineNumber}{eb}"

    n = cliWR - rawStrLength(s1)[0] - rawStrLength(s2)[0] - 3
    trait = f"\033[0;3{green}m" + "=" * abs(n) + ">"
    print(
        f"{trait} {s1} {s2}"
        if n > 0
        else f"{trait} {s1}\n{s2: >{cliWR+rawStrLength(s2)[1]}}"
    )

    if cliWMsg:
        print(cliWMsg)
        # print(f"{'*' *45}".center(66))
        # ls()

    try:
        sleep(sleepDuration)
        pf("cliW, simuCliW, cliWR")  # 2ar
    except:
        pass
        print(f"\033[1;31mNo pf() !!!{eb}")

    sys.exit()


def bidon():
    s = "bidon"
    print("Bidon")
    ls()


if __name__ == "__main__":
    sleep(sleepDuration)
    cls("Main TOOLS")

    if 0:  # Simple test, Mettre 1 pour cette partie
        sleep(sleepDuration)
        print("Début script →\n")
        sleep(sleepDuration)
        ls()
        sleep(sleepDuration)
        print(f"\n{'← Fin script\n': >{cliW}}")
        exit()  # 2ar

    if 0: # 2ar Activer aprè_s pf() OK et finir tests dessous
        sleep(sleepDuration)

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
    # sleep(sleepDuration)

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
