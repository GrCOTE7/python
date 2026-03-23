import pygame
import time


class Display_chess:

    color_red = (255, 0, 0)
    color_blue = (0, 0, 255)
    color_green = (0, 255, 0)
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)

    def __init__(self, title, width, height, pause_t):
        pygame.init()
        self.width = width
        self.height = height
        self.pause_time = pause_t
        pygame.display.set_caption(title)
        self.window_surface = pygame.display.set_mode((width, height))

    def drawChess(self, lstQueen):
        recHeight = int(self.height / 8)
        recWidth = int(self.width / 8)
        self.window_surface.fill(self.color_white)

        for i, j in [(i, j) for i in range(8) for j in range(8)]:
            if (i + j) % 2:
                pygame.draw.rect(
                    self.window_surface,
                    self.color_black,
                    pygame.Rect(i * recWidth, j * recHeight, recWidth, recHeight),
                )

        if len(lstQueen) == 8:
            queenColor = self.color_green
        else:
            queenColor = self.color_blue

        for i, j in lstQueen:
            pygame.draw.rect(
                self.window_surface,
                queenColor,
                pygame.Rect(j * recWidth, i * recHeight, recWidth, recHeight),
            )

        pygame.display.flip()

        if len(lstQueen) == 8:
            time.sleep(2)

        time.sleep(self.pause_time)

    def waitQuit(self):
        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False


def giveFreePositions(lstQueen):
    lstPossibility = [(len(lstQueen), i) for i in range(8)]

    lstValid = []
    for i in lstPossibility:
        valid = True
        for j in lstQueen:
            if i[1] == j[1]:
                valid = False
            elif abs((i[0] - j[0]) / (i[1] - j[1])) == 1:
                valid = False
        if valid:
            lstValid.append(i)

    return lstValid


def printQueenPositions(lstQueen=[]):

    graphChess.drawChess(lstQueen)
    for i in giveFreePositions(lstQueen):
        if len(lstQueen) == 7:
            print(lstQueen + [i])
            graphChess.drawChess(lstQueen + [i])
        else:
            printQueenPositions(lstQueen + [i])


graphChess = Display_chess("Les 8 dames", 800, 800, 0.002)
printQueenPositions()
graphChess.waitQuit()
