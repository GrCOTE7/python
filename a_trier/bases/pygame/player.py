import pygame
from pathlib import Path


class Player:
    def __init__(self, x, y):
        assets_dir = Path(__file__).resolve().parent
        self.image = pygame.image.load(str(assets_dir / "player.png"))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
