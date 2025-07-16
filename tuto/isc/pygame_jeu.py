import pygame
from pygame import *


LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

# * [ ] Attendre réponse Thierry // sprite pour finir (2/4)


class Vaisseau(pygame.sprite.Sprite):
    def __init__(self):
        super(Vaisseau, self).__init__()

        # self.surf = pygame.Surface((50, 25))
        # self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load("ressources/vaisseau.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

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

        if pressed_keys[K_SPACE]:
            if len(le_missile.sprites()) < 1:
                missile = Missile(self.rect.center)
                tous_sprites.add(missile)
                le_missile.add(missile)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGEUR_ECRAN:
            self.rect.right = LARGEUR_ECRAN
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HAUTEUR_ECRAN:
            self.rect.bottom = HAUTEUR_ECRAN


class Missile(pygame.sprite.Sprite):
    def __init__(self, center_missile):
        super(Missile, self).__init__()
        self.surf = pygame.image.load("ressources/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=center_missile)

    def update(self):
        self.rect.move_ip(15, 0)
        if self.rect.left > LARGEUR_ECRAN:
            self.kill()


pygame.init()

pygame.display.set_caption("The Shoot'em up 1.0")
ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))

clock = pygame.time.Clock()

tous_sprites = pygame.sprite.Group()
le_missile = pygame.sprite.Group()

vaisseau = Vaisseau()
tous_sprites.add(vaisseau)

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    ecran.fill((0, 0, 0))

    touche_appuyee = pygame.key.get_pressed()

    vaisseau.update(touche_appuyee)
    le_missile.update()

    for a_sprite in tous_sprites:
        ecran.blit(a_sprite.surf, a_sprite.rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
