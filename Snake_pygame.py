
import pygame

pygame.init()

breedte = 600
hoogte = 400

scherm = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption("Mijn Snake Game")

while True:
    for gebeurtenis in pygame.event.get():
        if gebeurtenis.type == pygame.QUIT:
            pygame.quit()
            quit()

    scherm.fill((30, 30, 30))
    pygame.display.update()
