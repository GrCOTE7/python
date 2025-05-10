import locale, shutil
from flask import cli

alertMsg = infoMsg = cliWMsg = simuCliW = None
locale.setlocale(locale.LC_ALL, "fr_FR")

#################################################################
# simuCliW = 40  # @i Si on veut Pour simuler une cliW sinon: Commenter
sleepDuration = 0.7  # @i Tempo des affichages en secondes des parties
idealCliWs = range(50, 61)  # Utiliser 55 col. est conseillé
#################################################################

# cli: Console Line Interface - W: width - R: Réel
cliWR = shutil.get_terminal_size().columns  # Réelle CLI Width

cliW = simuCliW if simuCliW else cliWR
lg = "\n" + "-" * cliWR
sb = "\033[1m"  # Début gras (Start Bold)
eb = "\033[0m"  # Fin gras (End Bold) - Sert aussi de reset du style

french = "french"
(black, red, green, yellow, blue, magenta, cyan, white) = range(8)

# 0 : noir - 1 : rouge - 2 : vert - 3 : jaune - 4 : bleu - 5 : magenta - 6 : cyan - 7 : blanc
# 3x pour encre, 4x pour fond
# \033[3mItalique\033[23m)
# \033[4mSouligné\033[24m)
# \033[3;4mSouligné & Italique\033[23;24m)
