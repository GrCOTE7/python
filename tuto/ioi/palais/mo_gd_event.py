import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent.parent / "tools"))
from tools import cls, exit

def haut():
    print("↑", end=" ")


def bas():
    print("↓", end=" ")


def gauche():
    print("←", end=" ")


def droite():
    print("→", end=" ")


cls()

l=4 # Réduis la taille du problème, et quand ça marchera là, tu mettras 10 ici !

for colonne in range(l):

    # Colonne paire : monter
    if colonne % 2 == 0:
        for _ in range(l-1):
            haut()

    # Colonne impaire : descendre
    else:
        for _ in range(l-1):
            bas()

    # Aller à la colonne suivante (sauf après la dernière)
    if colonne < l-1:
        droite()

    # Retour au point de départ (en haut à droite → aller à gauche)
    for _ in range(l-1):
        gauche()

exit()
