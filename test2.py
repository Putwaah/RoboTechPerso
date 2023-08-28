import pygame, sys, os 
import pygame.camera 
 
 
pygame.init() 
pygame.camera.init() 
 
 
ECRAN = pygame.display.set_mode((400, 400)) 
 
 
cam = pygame.camera.Camera("/dev/video0", (400, 400)) 
cam.start() 
 
 
NUM = 0 
CAPTURE = False 
 
 
while not CAPTURE: 
 NUM = NUM + 1 
 image = cam.get_image() 
 screen.blit(image, (0,0)) 
 pygame.display.update() 
 
 NOM_FICHIER = "PHOTOS/%04d.png" % NUM 
 pygame.image.save(image, NOM_FICHIER) 
 
 for event in pygame.event.get(): 
   if event.type == pygame.QUIT: 
     CAPTURE = True 
      
os.system("avconv -r 8 -f image2 -i PHOTOS/%04d.png -y -qscale 0 -s 640x480 - aspect 4:3 output.avi")