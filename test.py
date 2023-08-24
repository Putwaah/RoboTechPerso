import pygame

window_res = (1024, 600)
blue_color = (89, 152, 255)

pygame.init()
pygame.display.set_caption("Test RoboTech")
window_surface = pygame.display.set_mode(window_res)
window_surface.fill(blue_color)

pygame.display.flip()

launched = True


while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             launched = False
        elif event.type == pygame.KEYDOWN and event.type == K_ESCAPE:
            launched = False
