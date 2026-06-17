import os, sys, inspect, locale, shutil

def get_cli_width(default=80):
    """Récupère la largeur réelle de la console avec plusieurs stratégies."""

    for env_name in ("PY_CLI_WIDTH", "CLI_WIDTH", "COLUMNS"):
        env_val = os.environ.get(env_name)
        if env_val and env_val.isdigit() and int(env_val) > 0:
            return int(env_val)

    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes

            class COORD(ctypes.Structure):
                _fields_ = [("X", wintypes.SHORT), ("Y", wintypes.SHORT)]

            class SMALL_RECT(ctypes.Structure):
                _fields_ = [
                    ("Left", wintypes.SHORT),
                    ("Top", wintypes.SHORT),
                    ("Right", wintypes.SHORT),
                    ("Bottom", wintypes.SHORT),
                ]

            class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
                _fields_ = [
                    ("dwSize", COORD),
                    ("dwCursorPosition", COORD),
                    ("wAttributes", wintypes.WORD),
                    ("srWindow", SMALL_RECT),
                    ("dwMaximumWindowSize", COORD),
                ]

            get_std_handle = ctypes.windll.kernel32.GetStdHandle
            get_csbi = ctypes.windll.kernel32.GetConsoleScreenBufferInfo
            get_std_handle.argtypes = [wintypes.DWORD]
            get_std_handle.restype = wintypes.HANDLE
            get_csbi.argtypes = [
                wintypes.HANDLE,
                ctypes.POINTER(CONSOLE_SCREEN_BUFFER_INFO),
            ]
            get_csbi.restype = wintypes.BOOL

            for std_handle in (-11, -12, -10):  # stdout, stderr, stdin
                handle = get_std_handle(std_handle)
                if not handle or handle == wintypes.HANDLE(-1).value:
                    continue
                csbi = CONSOLE_SCREEN_BUFFER_INFO()
                if get_csbi(handle, ctypes.byref(csbi)):
                    cols = int(csbi.srWindow.Right - csbi.srWindow.Left + 1)
                    if cols > 0:
                        return cols
        except Exception:
            pass

    for stream in (
        getattr(sys, "__stdout__", None),
        sys.stdout,
        getattr(sys, "__stderr__", None),
        sys.stderr,
        getattr(sys, "__stdin__", None),
        sys.stdin,
    ):
        try:
            if stream is None:
                continue
            cols = os.get_terminal_size(stream.fileno()).columns
            if cols > 0:
                return cols
        except Exception:
            continue

    try:
        cols = shutil.get_terminal_size(fallback=(default, 24)).columns
        if cols > 0:
            return cols
    except Exception:
        pass

    return default


CLIWR = get_cli_width()  # Réelle CLI Width
SIMU_CLIW = 77
CLIW = SIMU_CLIW if SIMU_CLIW else CLIWR
LG = "\n" + "-" * CLIWR
SB = "\033[1m"  # Début gras (Start Bold)
EB = ES = "\033[0m"  # Fin gras (End Bold ou End Style) Car sert aussi de reset
FRENCH = "french"
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def cls(title=None, filename="", page=None):
    """Réinitialise la console (CLI) ou la page (Flet).
    Affiche title sauf si title=0.
    """

    if page is None and hasattr(title, "clean") and callable(getattr(title, "clean")):
        page = title
        title = None

    if page is not None and hasattr(page, "clean") and callable(getattr(page, "clean")):
        page.clean()

        if title not in (None, 0) and hasattr(page, "title"):
            page.title = str(title)

        if hasattr(page, "update") and callable(getattr(page, "update")):
            page.update()
        return

    def _force_home_windows():
        if os.name != "nt":
            return
        try:
            import ctypes

            class COORD(ctypes.Structure):
                _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            if handle not in (0, -1):
                ctypes.windll.kernel32.SetConsoleCursorPosition(handle, COORD(0, 0))
        except Exception:
            pass

    out = getattr(sys, "__stdout__", None)

    try:
        if out and hasattr(out, "write"):
            out.write("\033[3J\033[2J\033[H")
            out.flush()
    except Exception:
        pass

    if os.name == "nt":
        try:
            with open("CON", "w", encoding="utf-8", errors="ignore") as con:
                con.write("\033[3J\033[2J\033[H")
                con.flush()
        except Exception:
            pass

    _force_home_windows()
    os.system("cls" if os.name == "nt" else "clear")
    _force_home_windows()

    # cliWAnalysis()

    # if title != 0:
    #     setTitle(title, filename)


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
        lineCode = f"\033[0;3{lineColor}m" + f"{trait}{finTrait}" * w + EB

    if toPrint:
        print(lineCode)
        return None
    else:
        return lineCode


def refresh_cli_width():
    global CLIWR, CLIW, LG
    CLIWR = get_cli_width()
    CLIW = SIMU_CLIW if SIMU_CLIW else CLIWR
    LG = "\n" + "-" * CLIWR
    return CLIWR


# cli: Console Line Interface - W: width - R: Réel
CLIWR = get_cli_width()  # Réelle CLI Width

CLIW = SIMU_CLIW if SIMU_CLIW else CLIWR
LG = "\n" + "-" * CLIWR
SB = "\033[1m"  # Début gras (Start Bold)
EB = ES = "\033[0m"  # Fin gras (End Bold ou End Style) Car sert aussi de reset du style

FRENCH = "french"
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

# 0 : noir - 1 : rouge - 2 : vert - 3 : jaune - 4 : bleu - 5 : magenta - 6 : cyan - 7 : blanc
# 3x pour encre, 4x pour fond
# \033[3mItalique\033[23m)
# \033[4mSouligné\033[24m)
# \033[3;4mSouligné & Italique\033[23;24m)


# cli: Console Line Interface - W: width - R: Réel


def nf(x, dec=0):
    """
    Format number without using locale.
    1234567.89 → 1 234 567,89
    """
    try:
        x = float(x)
    except Exception:
        return str(x)

    # Format with dot as decimal separator
    s = f"{x:,.{dec}f}"

    # Replace US separators with French ones
    s = s.replace(",", " ").replace(".", ",")

    return s


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
    partBlue, partWhite, partRed, endColors = (
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
