from stat import SF_IMMUTABLE
import os, sys, inspect, locale, shutil
from matplotlib import lines
from pyparsing import line
from tabulate import tabulate
from time import sleep, time

locale.setlocale(locale.LC_ALL, "fr_FR")

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

cliWR = cliW = shutil.get_terminal_size().columns  # Réelle CLI Width
idealCliWs = range(55, 60)  # W = Width
alertMsg = infoMsg = simucliW = cliWMsg = None

simucliW = 55  # @i Si on veut Pour simuler une cliW sinon: Commenter
sleepDuration = 0  # @i Tempo des affichages en secondes des parties

cliW = simucliW if simucliW else cliWR
lg = "\n" + "-" * cliWR
sb = "\033[1m"  # Début gras (Start Bold)
eb = "\033[0m"  # Fin gras (End Bold)
cs = " "  # Césure (Prend parfois la valeur '\n')

french = "french"
(black, red, green, yellow, blue, magenta, cyan, white) = range(8)


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
    return f"(\033[1;3{color}m{n}{eb} cols)"


if simucliW:

    # Affichage du référenciel cliW si SIMU
    cliWMsg = f"Ref1. \033[1;37mSIMU{eb}: CLI with {nbCliCols(cliW)[1:-1]}"

    if simucliW == cliWR:
        cliWMsgDetails = f"\033[0;37m(As Real)"

    elif simucliW < cliWR:
        cliWMsgDetails = f" \033[1;3m(" + str(cliWR) + f" \033[0;3mreally" + f"){eb}"

    else:
        cliWMsgDetails = f"⚠️ : Your {sb}CLI has a simulated width of {eb} {nbCliCols(simucliW)} \033[1;31mBIGGER{eb} as it{sb}real width!{eb} {nbCliCols(cliWR)}:\n"
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


def get_caller_function() -> str | None:
    """Return caller function if exists"""
    stack = inspect.stack()
    if len(stack) > 2:  # Vérifie qu'il y a une fonction appelante
        caller_frame = stack[2]
        caller_function = caller_frame.function  # Récupère le nom de la fonction
        return caller_function
    return None


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


def wordWrap(msg: tuple, w: int = cliW, align="<"):

    msg = "𐍈".join(str(item) for item in msg)
    lengthes = rawStrLength(msg)
    # pf("lengthes")

    # pf("len(msg), rawStrLength(msg)[0] > w, w")
    if lengthes[0] <= w:
        # print("DÉBUT TITRE: 1 ligne")
        # msg = msg.replace("𐍈", hyphen)
        hyphen = " "
    else:
        # print("DÉBUT TITRE: Des lignes")
        msgParts = msg.split("𐍈")
        pf("msgParts")
        # print(msgParts)
        msg = "".join(
            list(map(lambda l: f"{l: {align}{w+rawStrLength(l)[1]}}", msgParts))
        )

    return (msg, lengthes)
    # msg = f"{msg[0]} {msg[1]}"
    # msg = tuple(msg)


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

        elif style == "cliWInfo":
            print(msg)

        else:
            print(msg)


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


def pf(var: str, style: int = 0):
    """Show (str) 'var', type and value as prinf(f'{var}=') if int=1 (color cyan)
    else show same data in a table
    """

    def format_value(value):
        if isinstance(value, dict):
            # Format each key-value pair for dictionaries
            return (
                "<dict> {"
                + ", ".join(
                    f"<{type(k).__name__}> {k}: <{type(v).__name__}> {v}"
                    for k, v in value.items()
                )
                + "}"
            )
        elif isinstance(value, tuple):
            # Format each element for tuples, using parentheses
            return (
                f"<tuple> ("
                + ", ".join(f"<{type(item).__name__}> {item}" for item in value)
                + ")"
            )
        elif isinstance(value, list):
            # Format each element for lists, using brackets
            return (
                f"<list> ["
                + ", ".join(f"<{type(item).__name__}> {item}" for item in value)
                + "]"
            )
        elif hasattr(value, "__dict__"):  # Safely handle objects with attributes
            try:
                return (
                    "<object> {"
                    + ", ".join(
                        f"<{type(v).__name__}> {k}: {v}"
                        for k, v in value.__dict__.items()
                    )
                    + "}"
                )
            except Exception as e:
                return f"<object> Error extracting attributes: {e}"
        else:
            # Default formatting for scalar values
            return f"<{type(value).__name__}> {value}"

    # Retrieve caller information
    lineNumber = caller_info()[2]
    frame = inspect.currentframe().f_back

    # Handle multiple variables passed in `var`
    vars = [v.strip() for v in var.split(",")]
    formatted_values = []
    try:
        for single_var in vars:
            # Evaluate and format each variable independently
            value = eval(single_var, frame.f_globals, frame.f_locals)
            formatted_values.append((single_var, format_value(value)))
    except NameError as e:
        print(f"Error: {e}")
        return

    # Print the formatted values for non-table styles
    if style:
        for var_name, formatted_value in formatted_values:
            print(f"\n\033[1;36;40m{var_name} = {formatted_value}\033[0m")
    else:
        # Display the main en-tête
        print(f"\033[0;36;40m{f' pf({var})':-^{cliWR}}\033[0;37;40m")
        print()

        # Display separate tables for each variable without separation
        for var_name, formatted_value in formatted_values:
            # Create a separate table for each variable
            data = [[formatted_value]]
            headers = [f"\033[1;36m{var_name}\033[0;37;40m"]

            # print("DATA for tbl:", data)
            # print("HEADERS for tbl:", headers)
            tbl(data, headers)  # No text between tables

    # Display the final line (only once)
    print(
        f"\033[0;36;40m{' '+'Lg. '+str(nf(lineNumber, 0))+' ':-^{cliWR}}\033[0;37;40m"
    )


def exit():

    s = "> exit() - Line " + sb + str(inspect.currentframe().f_back.f_lineno) + eb
    print(f"\n\033[0;32m{s:=>{cliWR+rawStrLength(s)[1]}}\033[0;37m")

    msg = (
        f"⚠️ : Votre {sb}CLI a une largeur simulée{eb} {nbCliCols(simucliW)} \033[1;31mSUPÉRIEURE{eb} à sa {sb}largeur réelle{eb} {nbCliCols(cliWR)}:\n"
        + f"{'→ \033[1;31mFaux problèmes d\'apparence possibles\033[0;37m...'.center(cliWR)}"
    )

    w = nbCliCols(cliWR)

    s2 = (
        ""
        if cliWR in idealCliWs
        else f" (\033[3;31mIDEAL: {sb}{idealCliWs.start} → {idealCliWs.stop-1}{eb})"
    )

    s3 = f" - SIMU: {sb}{simucliW}{eb} cols." if simucliW else ""

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

    sys.exit()


def chrono(function):
    """Décorateur: Calcule le temps en secondes que met une fonction à s'executer.\n
    Placer @ chrono dans la ligne précédent le def de la fonction."""

    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # (Le temps "epoch").
        start = time()

        result = function(*args, **kwargs)

        end = time()
        # Différence entre 2 temps "epochs", celui qui est gardé dans "start", et celui qui sera gardé dans "end". ;)
        time_spent = end - start

        print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")
        print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")

        return result

    wrapper.__doc__ = function.__doc__
    return wrapper


def nf(f, dec=2):
    "Number Format 123456789 → 123 456,79"
    format_str = "%." + str(dec) + "f"
    return locale.format_string(format_str, f, grouping=True)


def ls():
    """Draw a line with the line number, function and the caller file."""
    (callerFile, context, lineNumber) = caller_info()
    s = f" \033[1;31;47m L.: {nf(lineNumber, 0)} \033[0;37;40m - {context} - F.: {callerFile}"
    textLength = rawStrLength(s)
    # pf("cliW, textLength")
    trait = sl(w=cliWR - textLength[0], toPrint=False)

    print(trait + s)
    # print("-" * cliW, "Réf.")


# @chrono
def tbl(data, headers=[], indexes=False):
    print(
        tabulate(
            data,
            headers,
            tablefmt="rounded_outline",
            showindex=indexes,
        )
    )


if __name__ == "__main__":

    sleep(sleepDuration)

    cls()  # 2ar tester dans cas simulatedW
    # cls("un très long titre")
    # cls(0)

    # t1 = (1, 2, 3)
    # t2 = (4, 5, 6)
    # pf("t1, t2")
    # pf("list(zip(t1, t2))")  # pf("*(list(zip(t1, t2)))")
    # print(*list(zip(t1, t2)))  # pf("*(list(zip(t1, t2)))")

    sleep(sleepDuration)

    print("Début script...")
    sleep(sleepDuration)

    # print(franceLine(50))
    # sl()
    # sl(blue)
    # sl(green, 70)
    # sl(cyan)
    # sl(french)
    # print("uuuuuuuuuuu")
    # sl(french, 20)
    # sl("french", 30)

    import lorem, textwrap

    def justify(text, width):
        # Divise le texte en mots
        lines = textwrap.wrap(text, width)
        justified_lines = []

        for line in lines[:-1]:  # Ne pas justifier la dernière ligne
            words = line.split()
            if len(words) == 1:  # Si une seule mot, aucune justification
                justified_lines.append(line)
                continue
            # Calcule les espaces nécessaires pour justifier
            total_spaces = width - sum(len(word) for word in words)
            spaces_between_words = len(words) - 1
            spaces = [total_spaces // spaces_between_words] * spaces_between_words
            for i in range(total_spaces % spaces_between_words):
                spaces[i] += 1
            # Assemble la ligne justifiée
            justified_line = "".join(
                word + " " * space for word, space in zip(words, spaces + [0])
            )
            justified_lines.append(justified_line)

        justified_lines.append(lines[-1])  # Ajouter la dernière ligne non justifiée
        return "\n".join(justified_lines)

    def justifyCenter(text, width):
        # Divise le texte en mots et calcule les lignes justifiées
        lines = textwrap.wrap(text, width)
        justified_lines = []

        for line in lines[:-1]:  # Ne pas justifier la dernière ligne
            words = line.split()
            if len(words) == 1:  # Si une seule mot, aucune justification
                justified_lines.append(line.center(width))
                continue
            total_spaces = width - sum(len(word) for word in words)
            spaces_between_words = len(words) - 1
            spaces = [total_spaces // spaces_between_words] * spaces_between_words
            for i in range(total_spaces % spaces_between_words):
                spaces[i] += 1
            justified_line = "".join(
                word + " " * space for word, space in zip(words, spaces + [0])
            )
            justified_lines.append(
                justified_line.center(width)
            )  # Centrer la ligne justifiée

        justified_lines.append(
            lines[-1].center(width)
        )  # Centrer la dernière ligne non justifiée
        return "\n".join(justified_lines)

    # txt = txtO = lorem.paragraph()
    # pf("len(txt)")
    # print(txt + "\n")

    txt = txtO = "Mon très très très long Titre /root/chemin/sousdossier/exemples/la"
    txt = textwrap.fill(txt, width=55)
    print(txt + "\n")

    exit()  # 2ar
    # print(*(range(1, 8)))  # print(*[range(5)])

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
