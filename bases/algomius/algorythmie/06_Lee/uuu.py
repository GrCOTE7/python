from collections import deque
from pprint import pprint

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
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
]
depl_possible = [(-1, 0), (0, -1), (1, 0), (0, 1)]
depart = (0, 1)
arrivee = (9, 9)

deb_x, deb_y = depart

dejaVisite = [[False for x in range(len(carte[0]))] for y in range(len(carte))]
dejaVisite[0][0] = True

aVisiter = deque()
aVisiter.append((deb_x, deb_y, 0))

(cur_x, cur_y, dist) = aVisiter.popleft()

pprint(dejaVisite)

for depl_x, depl_y in depl_possible:
    voisin_x = cur_x + depl_x
    voisin_y = cur_y + depl_y

    if (0 <= voisin_x < len(carte)) and (0 <= voisin_y < len(carte[0])):

        # Si le voisin est accessible
        if carte[voisin_x][voisin_y] == 1:

            print("\n %d_%d est accessible" % (voisin_x, voisin_y))
