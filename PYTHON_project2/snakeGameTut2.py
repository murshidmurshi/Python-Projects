import pygame
import random

#initialize
pygame.init()

#color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)


width=900
height=600
#snake rectangle
snake_x=30
snake_y=40
snake_size=20
snake_size=10
fps=10


velocity_x=0
velocity_y=0
food_x=random.randint(0,width)
food_y=random.randint(0,height)
score=0

gamewindow=pygame.display.set_mode((width,height))
caption=pygame.display.set_caption('SNAKE-game')
clock=pygame.time.Clock()

running=True
while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=+10
                velocity_y=0
            if event.key==pygame.K_LEFT:
                velocity_x=-10
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_y=-10
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=+10
                velocity_x=0
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    if abs(snake_x-food_x)<6 and  abs(snake_y-food_y)<6:
        score+=1
        print(score)


    gamewindow.fill('white')
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

