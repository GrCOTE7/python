import locale, os, shutil, sys
from flask import cli

alertMsg = infoMsg = cliWMsg = SIMU_CLIW = None
locale.setlocale(locale.LC_ALL, "fr_FR")

# @nb Liste de constantes même si ce concept n'existe pas vraiment en Py...

#################################################################
# SIMU_CliW = 40  # @i Si on veut Pour simuler une cliW sinon: Commenter
SLEEP_DURATION = 0.7  # @i Tempo des affichages en secondes des parties
IDEAL_CLIWS = range(50, 61)  # Utiliser 55 col. est conseillé
#################################################################

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
(BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE) = range(8)

# 0 : noir - 1 : rouge - 2 : vert - 3 : jaune - 4 : bleu - 5 : magenta - 6 : cyan - 7 : blanc
# 3x pour encre, 4x pour fond
# \033[3mItalique\033[23m)
# \033[4mSouligné\033[24m)
# \033[3;4mSouligné & Italique\033[23;24m)
