import pygame

#initialse pygame
pygame.init()


screen=pygame.display.set_mode((600,600))

#loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255,255,255))

    pygame.draw.circle(screen,(0,0,250),(250,250),75)
    pygame.draw.circle(screen, (0, 0, 30), (100, 250), 100)


    pygame.display.flip()

