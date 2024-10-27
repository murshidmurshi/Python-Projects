import pygame

pygame.init()
SCREEN_WIDTH=800
SCREEN_HIGHT=600
Background=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
pygame.display.set_caption('GAME')
white=(255,255,255)
black=(0,0,0)
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    Background.fill('white')
    pygame.display.update()

pygame.quit()


