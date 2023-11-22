import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN= pygame.display.set_mode((600,600))
CLOCK = pygame.time.Clock()

sysfont = pygame.font.SysFont(None,36)

txt = sysfont.render("",True,(0,0,0))

coord = sysfont.render("",True,(0,0,0))

x,y = 0,0

while True:
    SCREEN.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos[0],event.pos[1]
            coord = sysfont.render("(%d, %d)" %(x,y),True,(0,0,0))
            
            if event.button == 1 :
                txt = sysfont.render("1", True,(0,0,0))
                
            if event.button == 2 :
                txt = sysfont.render("2", True,(0,0,0))

            if event.button == 3 :
                txt = sysfont.render("3", True,(0,0,0))

            if event.button == 4 :
                txt = sysfont.render("4", True,(0,0,0))

            if event.button == 5 :
                txt = sysfont.render("5", True,(0,0,0))

    SCREEN.blit(txt,(285,220))
    SCREEN.blit(coord,(x,y))
    pygame.display.update()
    CLOCK.tick(60)
    
