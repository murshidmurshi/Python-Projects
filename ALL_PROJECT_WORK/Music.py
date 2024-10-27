##Music example


import pygame

pygame.init()

screen_width=800
screen_hight=screen_width*0.8

screen=pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption('Music')

pygame.mixer.music.load('music2.mp3')
pygame.mixer.music.play(-1)
run=True
while run:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
