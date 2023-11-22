import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN= pygame.display.set_mode((300,300))
CLOCK = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)

sysfont = pygame.font.SysFont(None,36)

txt = sysfont.render("0",True,BLACK)

n = 0

while True:
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            
            if event.key == K_UP :
                n += 10
                txt = sysfont.render("%d" % n, True,BLACK)
                
            if event.key == K_DOWN :
                n -= 10
                txt = sysfont.render("%d" % n, True,BLACK)

            if event.key == K_LEFT:
                n *= 10
                txt = sysfont.render("%d" % n, True,BLACK)

            if event.key == K_RIGHT :
                n /= 10
                txt = sysfont.render("%d" % n, True,BLACK)

    txt = sysfont.render('%d' % n, True,(0,0,0))        
    SCREEN.blit(txt,(100,120))
    pygame.display.update()
    CLOCK.tick(60)
