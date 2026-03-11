# Parcourir les 10 colonnes
def haut():
    print("↑", end=" ")


def bas():
    print("↓", end=" ")


def gauche():
    print("←", end=" ")


def droite():
    print("→", end=" ")


l=4

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
