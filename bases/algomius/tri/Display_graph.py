import pygame
from pygame.locals import *
import time

"""
    Cette classe nous permet d'afficher les tris de manière graphique.
    Elle est appelée dans les programmes sort_
    Il faut installer la librairie pygame pour que cela fonctionne.
"""

class Display_graph:

    color_red = (255, 0, 0)
    color_blue = (0, 255, 0)
    color_green = (0, 0, 255)
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)

    # Initialisation de la fenetre qui affiche l'histogramme
    def __init__(self, title, width, height, pause_t, swap_t):
        self.resetInd()
        pygame.init()
        window_resolution = (width, height)
        self.width = width
        self.height = height
        self.pause_time = pause_t
        self.swap_time = swap_t

        pygame.display.set_caption(title)
        self.window_surface = pygame.display.set_mode(window_resolution)

    # Affichage de l'histogramme
    def drawGraph(self, l, forSwap=False):        
        n = len(l)
        recWidth = self.width / n
        ratioHeigt = self.height / max(l)
        self.window_surface.fill(Display_graph.color_white)
        
        indx = 0
        for i in range(n):
            rect = Rect(indx, self.height - l[i] * ratioHeigt, recWidth, l[i] * ratioHeigt)
            if i in self.swapInd:
                pygame.draw.rect(self.window_surface, Display_graph.color_blue, rect)
            else:
                pygame.draw.rect(self.window_surface, Display_graph.color_green, rect)

            indx += recWidth
        
        pygame.display.flip()
        if forSwap:
            time.sleep(self.swap_time)
        else:
            time.sleep(self.pause_time)

    # Gestion des deux valeurs a échanger pendant le tri  
    def displaySwap(self, l, ind1, ind2):
        if ind1 != ind2:
            self.setSwapInd([ind1,ind2])
            self.drawGraph(l, True)
            l[ind1], l[ind2] = l[ind2], l[ind1]
            self.drawGraph(l, True)
        self.resetInd()
        self.drawGraph(l)

    # réinitialisation des indices à échanger
    def resetInd(self):
        self.swapInd = []

    # Définition des indices à échanger
    def setSwapInd(self, indS):
        self.swapInd = indS

    # Gestion de la fermeture de la fenêtre
    def waitQuit(self):
        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
