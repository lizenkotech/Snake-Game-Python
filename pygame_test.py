
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont(None, 60)
text = font.render("hello", True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(text, (140, 120))
    pygame.display.flip()
