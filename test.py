import pygame
import pygame.camera
from pygame.locals import *

#init program
pygame.init()
pygame.camera.init()
camlist = pygame.camera.list_cameras()
if camlist:
        cam
window_res = (1440, 900)

pygame.display.set_caption("Test RoboTech")
window_surface = pygame.display.set_mode(window_res)

fine_image = pygame.image.load("smiley_content.jpg")
not_fine_image = pygame.image.load("emoji_pas_content.png")
fine_image.convert() #sans transparence
not_fine_image.convert()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             launched = False

#body program
    window_surface.blit(fine_image, [0, 0])
    window_surface.blit(not_fine_image, [720, 0])
    pygame.display.flip()    
