import pygame
import button
pygame.init()
SCREEN_WIDTH=800
SCREEN_HIGHT=640

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
pygame.display.set_caption('button --')
#load images
start_image=pygame.image.load('img/start_btn.png').convert_alpha()
exit_image=pygame.image.load('img/exit_btn.png').convert_alpha()

start_button=button.Button(100,200,start_image,1)
exit_button=button.Button(450,200,exit_image,1)

run=True
while run:
    screen.fill((144,241,201))
    if start_button.draw(screen):
        print('START')
    if exit_button.draw(screen):
        print('EXIT')

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()