"""
    Tri rapide nécessaire à la recherche dichotomique
"""


def partitionner(l, debut, fin):
    valeur_pivot = l[fin]
    indice_pivot = debut

    for i in range(debut, fin):
        if l[i] <= valeur_pivot:
            l[i], l[indice_pivot] = l[indice_pivot], l[i]
            indice_pivot += 1

    l[indice_pivot], l[fin] = l[fin], l[indice_pivot]
    return indice_pivot


def tri_rapide(l, debut=0, fin=None):
    if fin == None:
        fin = len(l) - 1

    if fin > debut:
        pivot = partitionner(l, debut, fin)
        tri_rapide(l, debut, pivot - 1)
        tri_rapide(l, pivot + 1, fin)


"""
    Recherche dichotomique itérative
"""


def recherche_dichotomique_iterative(l, val):
    indice_gauche = 0
    indice_droit = len(l) - 1

    while indice_gauche <= indice_droit:
        indice_milieu = (indice_gauche + indice_droit) // 2

        if val == l[indice_milieu]:
            return indice_milieu
        elif val < l[indice_milieu]:
            indice_droit = indice_milieu - 1
        else:
            indice_gauche = indice_milieu + 1

    return -1


"""
    Recherche dichotomique récursive
"""


def recherche_dichotomique_recursive(l, val, indice_gauche=0, indice_droit=None):
    if indice_droit == None:
        indice_droit = len(l) - 1

    if indice_gauche > indice_droit:
        return -1

    indice_milieu = (indice_gauche + indice_droit) // 2

    if val == l[indice_milieu]:
        return indice_milieu
    elif val < l[indice_milieu]:
        return recherche_dichotomique_recursive(
            l, val, indice_gauche, indice_milieu - 1
        )
    else:
        return recherche_dichotomique_recursive(l, val, indice_milieu + 1, indice_droit)


if __name__ == "__main__":

    l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]
    tri_rapide(l)
    print(l)

    val_recherche = 63

    print("Recherche dichotomique iterative :")
    indice = recherche_dichotomique_iterative(l, val_recherche)

    if indice != -1:
        print("Element", val_recherche, "trouvé à l'indice", indice)
    else:
        print("Element non présent dans la liste")

    print("Recherche dichotomique recursive :")
    indice = recherche_dichotomique_recursive(l, val_recherche)

    if indice != -1:
        print("Element", val_recherche, "trouvé à l'indice", indice)
    else:
        print("Element non présent dans la liste")
