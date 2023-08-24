import pygame

res = (1024, 600)

pygame.init()
pygame.display.set_caption("Test RoboTech")
window_surface = pygame.display.set_mode(res)
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
