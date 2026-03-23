arr = [
    [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46],
    [2, 39, 9, 11, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46],
    [2, 5, 9, 11, 8, 87, 92, 63, 74, 6, 39, 69, 63, 33, 46],
    [2, 5, 6, 11, 8, 87, 92, 63, 74, 9, 39, 69, 63, 33, 46],
    [2, 5, 6, 8, 11, 87, 92, 63, 74, 9, 39, 69, 63, 33, 46],
    [2, 5, 6, 8, 9, 87, 92, 63, 74, 11, 39, 69, 63, 33, 46],
    [2, 5, 6, 8, 9, 11, 92, 63, 74, 87, 39, 69, 63, 33, 46],
    [2, 5, 6, 8, 9, 11, 33, 63, 74, 87, 39, 69, 63, 92, 46],
    [2, 5, 6, 8, 9, 11, 33, 39, 74, 87, 63, 69, 63, 92, 46],
    [2, 5, 6, 8, 9, 11, 33, 39, 46, 87, 63, 69, 63, 92, 74],
    [2, 5, 6, 8, 9, 11, 33, 39, 46, 63, 87, 69, 63, 92, 74],
    [2, 5, 6, 8, 9, 11, 33, 39, 46, 63, 63, 69, 87, 92, 74],
    [2, 5, 6, 8, 9, 11, 33, 39, 46, 63, 63, 69, 87, 92, 74],
    [2, 5, 6, 8, 9, 11, 33, 39, 46, 63, 63, 69, 74, 92, 87],
    [2, 5, 6, 8, 9, 11, 33, 39, 46, 63, 63, 69, 74, 87, 92],
]

import pygame
import time

pygame.init()

# taille de l'ecran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# taille des batonnets
BAR_WIDTH = 10

# couleur des batonnets
BAR_COLOR = (255, 255, 255)

# on cree la fenetre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# on parcourt le tableau
for row in arr:
    # on parcourt les elements de la ligne
    for i, elem in enumerate(row):
        # on dessine un batonnet
        pygame.draw.rect(screen, BAR_COLOR, (i * BAR_WIDTH, SCREEN_HEIGHT - elem, BAR_WIDTH, elem))
    # on rafraichit la fenetre
    pygame.display.flip()
    # on attend une seconde
    time.sleep(1)

# on ferme la fenetre
pygame.quit()
