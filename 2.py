import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((300,300))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 30)
txt = "Wait..."
txt2 = "Key Down !"

while True :

    SCREEN.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

    key_event = pygame.key.get_pressed()

    if key_event[pygame.K_LEFT]:
        txt = "Left " + txt2

    if key_event[pygame.K_RIGHT]:
        txt = "Right " + txt2

    if key_event[pygame.K_UP]:
        txt = "UP " + txt2

    if key_event[pygame.K_DOWN]:
        txt = "DOWN " + txt2

    if key_event[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()


    msg = sysfont.render(txt,True,(0,0,0))
    SCREEN.blit(msg, (50,100))
    pygame.display.update()
    CLOCK.tick(60)
    

    
