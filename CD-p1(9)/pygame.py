import sys
import pygame
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((400,300))

pygame.pygame.display.set_caption("Tick Tock Timer")

CLOCK = pygame.time.Clock()

sysfont = pygame.font.SysFont(None,36)

timer = 0
while True:
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        
    timer += 1
    
    screen.fill((255,255,255))

    cnt_txt = sysfont.reder("Timer : %d" % timer,True,(0,0,0))

    screen.blit(cnt_txt, (140,140))

    pygame.display.update()

    CLOCK.tick(1)
