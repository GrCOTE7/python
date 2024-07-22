import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

image = pygame.image.load("ball.png").convert()

clock = pygame.time.Clock()

x = 0
y = 0

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        x -= 1
    if pressed[pygame.K_RIGHT]:
        x += 1
    if pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_DOWN]:
        y += 1

    screen.fill((0,0,0))
    screen.blit(image, (x, y))
    pygame.display.flip()
    clock.tick(60)    

pygame.quit()
