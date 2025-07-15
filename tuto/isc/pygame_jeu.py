import pygame
from pygame import *


LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600


class Vaisseau(pygame.sprite.Sprite):
    def __init__(self):
        super(Vaisseau, self).__init__()
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGEUR_ECRAN:
            self.rect.right = LARGEUR_ECRAN
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HAUTEUR_ECRAN:
            self.rect.bottom = HAUTEUR_ECRAN


pygame.init()

pygame.display.set_caption("The Shoot'em up 1.0")
ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))

clock = pygame.time.Clock()

vaisseau = Vaisseau()

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    ecran.fill((0, 0, 0))

    touche_appuyee = pygame.key.get_pressed()

    vaisseau.update(touche_appuyee)

    ecran.blit(vaisseau.surf, vaisseau.rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
