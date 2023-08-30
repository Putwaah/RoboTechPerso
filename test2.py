import pygame
import pygame.camera
import sys

pygame.init()
pygame.camera.init()

pygame.display.set_caption("Test RoboTech")
surface = pygame.display.set_mode((1440,900))


cam = pygame.camera.Camera(0)
cam.start()

fine_image = pygame.image.load("emoji_ok.png")
not_fine_image = pygame.image.load("emoji_pas_content.png")
not_fine_image.convert()
fine_image.convert()

while True:
   img = cam.get_image()
   surface.blit(img,(0,0))
   pygame.display.update()
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_o: # a remplacer par validation du code
          surface.blit(fine_image, (820, 20))
        if event.key == pygame.K_n: # IDEM que K_o
          surface.blit(not_fine_image, (820, 20))
      if event.type == pygame.QUIT:
         cam.stop()
         pygame.quit()
         exit()
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_ESCAPE:
            cam.stop()
            pygame.quit()
            exit()

    
surface.blit(fine_image, [0, 0])
surface.blit(not_fine_image, [720, 0])
pygame.display.flip()    
 