import time

import pygame
import random

pygame.init()
hight=700
width=700
#color
white=(255,255,255)
black=(0,0,0)
red=(0,0,255)

#snake sizes
snake_x=10
snake_y=10
snake_size=20
fps=20
velocity_x=0
velocity_y=0
food_x=random.randint(2,hight/2)
food_y=random.randint(2,width/2)
food_size=20
score=0

screen=pygame.display.set_mode((hight,width))
pygame.display.set_caption('FIRST_PYGAME')
pygame.display.update()
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_font=font.render(text,True,color)
    screen.blit(screen_font,[x,y])




running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=+10
                velocity_y=0
            if event.key == pygame.K_LEFT:
                velocity_x=-10
                velocity_y=0
            if event.key == pygame.K_UP:
                velocity_y=-10
                velocity_x=0
            if event.key == pygame.K_DOWN:
                velocity_y=+10
                velocity_x=0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=1
        food_x = random.randint(2, hight / 2)
        food_y = random.randint(2, width / 2)
        food_size = 20

    pygame.display.update()
    screen.fill('white')
    text_screen('Score:'+str(score*10),black,12,12)
    pygame.draw.rect(screen,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(screen,red,[food_x,food_y,food_size,food_size])
    clock.tick(fps)


pygame.quit()
