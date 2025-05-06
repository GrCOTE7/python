import locale, shutil

locale.setlocale(locale.LC_ALL, "fr_FR")

# simucliW = 50  # @i Si on veut Pour simuler une cliW sinon: Commenter
sleepDuration = 0.7  # @i Tempo des affichages en secondes des parties

# cli Console - W width - R Réel
cliWR = shutil.get_terminal_size().columns  # Réelle CLI Width
idealCliWs = range(55, 60)
alertMsg = infoMsg = simuCliW = cliWMsg = None

cliW = simuCliW if simuCliW else cliWR
lg = "\n" + "-" * cliWR
sb = "\033[1m"  # Début gras (Start Bold)
eb = "\033[0m"  # Fin gras (End Bold)

french = "french"
(black, red, green, yellow, blue, magenta, cyan, white) = range(8)
