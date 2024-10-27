import pygame

pygame.init()

screen=600,600
display_surface1=pygame.display.set_mode((screen))
display_surface=pygame.display.set_caption('hello')

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    s=pygame.draw.circle(display_surface1,(0,0,250),(50,400),29)
    pygame.draw.line(display_surface1, (255, 0, 0), (60, 100),(90,90))
    pygame.display.flip()
