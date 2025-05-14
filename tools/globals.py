import locale, shutil
from flask import cli

alertMsg = infoMsg = cliWMsg = SIMU_CLIW = None
locale.setlocale(locale.LC_ALL, "fr_FR")

# @nb Liste de constantes même si ce concept n'existe pas vraiment en Py...

#################################################################
# SIMU_CliW = 40  # @i Si on veut Pour simuler une cliW sinon: Commenter
SLEEP_DURATION = 0.7  # @i Tempo des affichages en secondes des parties
IDEAL_CLIWS = range(50, 61)  # Utiliser 55 col. est conseillé
#################################################################

# cli: Console Line Interface - W: width - R: Réel
CLIWR = shutil.get_terminal_size().columns  # Réelle CLI Width

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
