import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN= pygame.display.set_mode((300,300))
CLOCK = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)

sysfont = pygame.font.SysFont(None,36)

txt = sysfont.render("",True,BLACK)

while True:
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            
            if event.key == K_UP :
                txt = sysfont.render("UP", True,BLACK)
                
            if event.key == K_DOWN :
                txt = sysfont.render("DOWN", True,BLACK)

            if event.key == K_LEFT:
                txt = sysfont.render("LEFT", True,BLACK)

            if event.key == K_RIGHT :
                txt = sysfont.render("RIGHT", True,BLACK)

            if event.key == K_ESCAPE :
                pygame.quit()
                sys.exit()
    SCREEN.blit(txt,(100,120))
    pygame.display.update()
    CLOCK.tick(60)
        

     
            
        
