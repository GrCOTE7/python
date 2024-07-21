# https://www.youtube.com/watch?v=KMjaEtSjsjM&list=PLo53cbpzes8ZDG62Pn4U4plWpP8_EBFal&index=4

def kadane(l):
    """ La fonction kadane prend en argument une liste d'entiers
    Cette fonction retourne:
        - la somme maximum d'une sous-liste de l
        - la sous-liste qui donne la plus grande somme
        - l'index de début de la sous-liste
    """

    # Meilleur solution, en attendant mieux
    maximum_meilleur = 0
    liste_meilleur = []
    indice_meilleur = -1

    # Solution en cours d'évaluation
    maximum_eval = 0
    liste_eval = []
    indice_eval = -1

    for i in range(len(l)):
        maximum_eval = maximum_eval + l[i]
        liste_eval.append(l[i])
        if maximum_eval <= 0:
            maximum_eval = 0
            liste_eval = []

        if len(liste_eval) == 1:
            indice_eval = i

        if maximum_eval > maximum_meilleur:
            maximum_meilleur = maximum_eval
            liste_meilleur = liste_eval.copy()
            indice_meilleur = indice_eval

    return maximum_meilleur, liste_meilleur, indice_meilleur

if __name__ == '__main__':

    liste = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print("Liste de départ", liste)
    somme, ssliste, indice =  kadane(liste)
    if indice == -1:
        print("Il n'y a pas de nombre positif dans la liste")
    else :
        print("La sous-liste", ssliste, "maximise la somme qui est de",somme)
        print("Nous commençons la sous liste à l'indice", indice)
