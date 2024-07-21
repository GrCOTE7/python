# https://www.youtube.com/watch?v=vcx2xam9gUg&list=PLo53cbpzes8ZDG62Pn4U4plWpP8_EBFal&index=6
# https://i.imgur.com/HxbBUK7.png

from collections import deque

# Liste des déplacement Possible
depl_possible = [(-1,0),(0,-1),(1, 0),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]

# Retrouver la distance minimum entre le point (i, j) et la destination (x, y)
def parcours_largeur(carte, deb_x, deb_y, fin_x, fin_y):

    dejaVisite = [[False for x in range(len(carte[0]))] for y in range(len(carte))]
    aVisiter = deque()
    dejaVisite[deb_x][deb_y] = True
    aVisiter.append((deb_x, deb_y, 0))
    min_dist = float('inf')

    pred = {}

    while aVisiter:

        (cur_x, cur_y, dist) = aVisiter.popleft()
        if cur_x == fin_x and cur_y == fin_y:
            min_dist = dist
            break

        for (depl_x, depl_y) in depl_possible:
            voisin_x = cur_x + depl_x
            voisin_y = cur_y + depl_y

            # Si le voisin est bien sur la carte
            if (0 <= voisin_x < len(carte)) and (0 <= voisin_y < len(carte[0])):

                # Si le voisin est accessible
                if (carte[voisin_x][voisin_y] == 1):

                    # Si le voisin n'a pas encore été visité
                    if not dejaVisite[voisin_x][voisin_y]:
                        dejaVisite[voisin_x][voisin_y] = True
                        aVisiter.append((voisin_x, voisin_y, dist + 1))

                        pred[(voisin_x, voisin_y)] = (cur_x, cur_y)

    return min_dist, pred


# Algorithme de Lee
if __name__ == '__main__':

    # Définition du labyrinthe 0 case noire, 1 blanche
    carte = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]

    depart=(0,0)
    arrivee=(9,9)

    # Trouver le chemin le plus court entre le point (0, 0) et la destination (7, 5)
    dist, pred = parcours_largeur(carte, depart[0], depart[1], arrivee[0], arrivee[1])

    if dist != float('inf'):
        print("Le chemin le plus court jusqu'à la destination a une longueur de", dist)
        print("Voici le chemin à parcourir :")
        print(arrivee)
        while (arrivee != depart):
            arrivee = pred[arrivee]
            print(arrivee)
    else:
        print("La destination ne peut pas être atteinte")
