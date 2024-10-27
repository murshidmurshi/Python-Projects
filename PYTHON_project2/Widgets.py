import pygame
import sys
import time
#init
pygame.init()

screen1=pygame.display.set_mode((700,700))
pygame.display.set_caption(('reaction time'))



running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()



