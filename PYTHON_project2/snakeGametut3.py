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
fps=10

init_velocity=20

velocity_x=0
velocity_y=0
food_x=random.randint(20,width/2)
food_y=random.randint(20,height/2)
score=0

gamewindow=pygame.display.set_mode((width,height))
caption=pygame.display.set_caption('SNAKE-game')
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])






running=True
while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=+init_velocity
                velocity_y=0
            if event.key==pygame.K_LEFT:
                velocity_x=-init_velocity
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_y=-init_velocity
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=+init_velocity
                velocity_x=0
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    if abs(snake_x-food_x)<10and  abs(snake_y-food_y)<10:
        score+=1

        food_x = random.randint(0, width)
        food_y = random.randint(0, height)

    gamewindow.fill('white')
    text_screen("Score:"+str(score*10),red,5,5)
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

