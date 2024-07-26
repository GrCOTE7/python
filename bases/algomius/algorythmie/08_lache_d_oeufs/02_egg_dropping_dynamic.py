# https://www.youtube.com/watch?v=fnSIugYDNLA&list=PLo53cbpzes8ZDG62Pn4U4plWpP8_EBFal&index=8


def CombienDeLaches(nb_oeufs, nb_etages):
    """
    Fonction qui donne le nombre minimum d'essais pour déterminer à quel
    étage casse un oeuf en fonction du nombre d'oeuf disponible et du
    nombre d'étage
    """

    matrice = [
        [float("inf") for x in range(nb_etages + 1)] for x in range(nb_oeufs + 1)
    ]

    for i in range(1, nb_oeufs + 1):
        matrice[i][0] = 1
        matrice[i][1] = 1

    for i in range(1, nb_etages + 1):
        matrice[1][i] = i

    for i in range(2, nb_oeufs + 1):
        for j in range(2, nb_etages + 1):
            for x in range(1, j + 1):

                res = 1 + max(matrice[i - 1][x - 1], matrice[i][j - x])
                matrice[i][j] = min(res, matrice[i][j])

    return matrice[nb_oeufs][nb_etages]


if __name__ == "__main__":

    nb_oeufs = 12
    # nb_etages = (1585+1586) //2  # 20
    nb_etages = (int)(1.584e3)  # 20
 
    nb_diff = 0
    while nb_diff < 7:

        print("\nTest pour max ", nb_oeufs, "oeufs et", nb_etages, "étages :\n")
        nb_diff = 0
        prec = 0
        for oeufs in range(1, nb_oeufs + 1):
            nb = CombienDeLaches(oeufs, nb_etages)
            if prec != nb:
                prec = nb
                nb_diff += 1
                print(
                    f"Nombre minimum de laches dans le pire cas: {oeufs:>2} oeufs et {nb_etages} étages: {nb:>4}"
                )
                if (nb_diff>6):
                    break
        nb_etages += 1

        print("\nFini :", nb_diff, "changements du nombre de lâchés\n", "-" * 68)
