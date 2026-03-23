def CombienDeLaches(nb_oeufs, nb_etages):
    """
    Fonction qui donne le nombre minimum d'essais pour déterminer à quel
    étage casse un oeuf en fonction du nombre d'oeuf disponible et du
    nombre d'étage
    """

    # 0 étage ou 1 étage
    if nb_etages == 1 or nb_etages == 0:
        return nb_etages

    # Si un seul oeuf, il faut tester chaque étage
    if nb_oeufs == 1:
        return nb_etages

    minLaches = float("inf")

    for x in range(1, nb_etages + 1):

        res = 1 + max(
            CombienDeLaches(nb_oeufs - 1, x - 1),
            CombienDeLaches(nb_oeufs, nb_etages - x),
        )
        minLaches = min(res, minLaches)
        # print(x, end=' ')

    return minLaches


if __name__ == "__main__":

    nb_oeufs = 7

    nb_etages = 20  # 20

    print("\nTest pour max ", nb_oeufs, "oeufs et", nb_etages, "etages :\n")

    for oeufs in range(1, nb_oeufs + 1):
        print(
            f"Nombre minimum de laches dans le pire cas: {oeufs:>2} oeufs et {nb_etages} étages: {CombienDeLaches(oeufs, nb_etages):>2}"
        )

    print("-" * 68, "\nFini !\n")
