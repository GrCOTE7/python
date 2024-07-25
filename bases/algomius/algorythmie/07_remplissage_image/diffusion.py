from collections import deque

# Liste des mouvements possibles pour l'algorithme
deplacement = [
    (-1, 0),  # gauche
    (1, 0),  # droite
    (0, -1),  # haut
    (0, 1),  # bas
    (-1, -1),  # diagonale haut/gauche
    (-1, 1),  # diagonale bas/gauche
    (1, -1),  # diagonale haut/droite
    (1, 1),  # diagonale bas/droite
]


def pointValide(image, point, ancienneCouleur):
    """
    Un point est jugé valide si :
    - Il est toujours dans les limites de notre tableau image
    - Il est de la couleur à modifier
    Les arguments de la fonction sont:
    - L'image sous forme de liste de Liste
    - Les coordonnées du point de départ de la diffusion
    - La couleur à remplacer
    """
    return (
        0 <= point[0] < len(image)
        and 0 <= point[1] < len(image[0])
        and image[point[0]][point[1]] == ancienneCouleur
    )


def remplissageDiffusionIteratif(image, pointDepart, nouvelleCouleur):
    """
    Fonction de remplissage par diffusion itérative. Cette fonction utilise la
    méthode de parcourt en largeur dans la théorie des graphes.
    Les arguments de la fonction sont:
    - L'image sous forme de liste de Liste
    - Les coordonnées du point de départ de la diffusion
    - La nouvelle couleur à utiliser
    """

    resteATraiter = deque()
    resteATraiter.append(pointDepart)

    # Récupération de la couleur au point origine
    ancienneCouleur = image[pointDepart[0]][pointDepart[1]]

    while resteATraiter:

        pointCourant = resteATraiter.popleft()
        image[pointCourant[0]][pointCourant[1]] = nouvelleCouleur

        for depl in deplacement:
            # Addition du point courant et d'un déplacement pour obtenir les coordonnées d'un point adjacent
            pointVoisin = tuple(p + q for p, q in zip(pointCourant, depl))

            # Voir base/tuple_list.py

            # pointCourant et depl :
            # pointCourant et depl sont probablement des tuples ou des listes de coordonnées. Par exemple, dans un contexte de manipulation de points dans un espace 2D ou 3D, pointCourant pourrait être (x, y) ou (x, y, z) et depl pourrait être (dx, dy) ou (dx, dy, dz).

            # zip(pointCourant, depl) :
            # La fonction zip prend deux ou plusieurs itérables (dans ce cas, pointCourant et depl) et les agrège en un seul itérable de tuples. Par exemple, si pointCourant = (1, 2) et depl = (3, 4), alors zip(pointCourant, depl) produira [(1, 3), (2, 4)].

            # Compréhension de liste :
            # La partie p + q for p, q in zip(pointCourant, depl) est une compréhension de liste qui itère sur chaque tuple produit par zip. Pour chaque tuple (p, q), elle calcule la somme p + q.
            # Par exemple, avec pointCourant = (1, 2) et depl = (3, 4), cela produira [1 + 3, 2 + 4] soit [4, 6].

            # Conversion en tuple :
            # Enfin, tuple(...) convertit la liste résultante en un tuple. Donc, [4, 6] devient (4, 6).

            if pointValide(image, pointVoisin, ancienneCouleur):
                resteATraiter.append((pointVoisin))


def remplissageDiffusionRecursif(image, pointDepart, nouvelleCouleur):
    """
    Fonction de remplissage par diffusion récursive. Cette fonction utilise la
    méthode de parcourt en profondeur dans la théorie des graphes.
    Les arguments de la fonction sont:
    - L'image sous forme de liste de Liste
    - Les coordonnées du point de départ de la diffusion
    - La nouvelle couleur à utiliser
    """

    # Récupération de la couleur au point origine
    ancienneCouleur = image[pointDepart[0]][pointDepart[1]]
    image[pointDepart[0]][pointDepart[1]] = nouvelleCouleur

    for depl in deplacement:
        # Addition du point courant et d'un déplacement pour obtenir
        # les coordonnées d'un point adjacent
        pointVoisin = tuple(p + q for p, q in zip(pointDepart, depl))
        if pointValide(image, pointVoisin, ancienneCouleur):
            remplissageDiffusionRecursif(image, pointVoisin, nouvelleCouleur)


if __name__ == "__main__":

    image = [
        ["J", "J", "J", "G", "G", "G", "G", "G", "G", "G"],
        ["J", "J", "J", "J", "J", "J", "G", "V", "V", "V"],
        ["G", "G", "G", "G", "G", "G", "G", "V", "V", "V"],
        ["B", "B", "B", "B", "B", "G", "G", "G", "G", "V"],
        ["B", "R", "R", "R", "R", "R", "G", "V", "V", "V"],
        ["B", "B", "B", "R", "R", "G", "G", "V", "V", "V"],
        ["B", "M", "B", "R", "R", "R", "R", "R", "R", "V"],
        ["B", "M", "M", "M", "M", "R", "R", "V", "V", "V"],
        ["B", "M", "M", "V", "M", "M", "M", "M", "V", "V"],
        ["B", "M", "M", "V", "V", "V", "V", "V", "V", "V"],
    ]
    
    import copy
    # image[::] ne copie pas les sous-listes
    imagePourR = copy.deepcopy(image)

    pointDepart = (3, 9)
    nouvelleCouleur = "C"

    print("-" * 50)

    for r in image:
        print(r)

    print("-" * 50)

    remplissageDiffusionIteratif(image, pointDepart, nouvelleCouleur)
    print("Itératif")
    for r in image:
        print(r)

    print("-" * 50)

    pointDepart = (3, 9)
    nouvelleCouleur = "C"
    image = imagePourR
    # for r in image:
    #   print(r)
    
    remplissageDiffusionRecursif(imagePourR, pointDepart, nouvelleCouleur)
    print("Récursif")

    for r in image:
        print(r)

    # print("-" * 50)
