import pygame
import random

pygame.init()

#measures
hight=600
width=600
setup=pygame.display.set_mode((hight,width))


pygame.display.set_caption('Snake_Game')
clock=pygame.time.Clock()

#color
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

#snake
snake_x=20
snake_y=20
snake_size=23
velocity_x=0
velocity_y=0
fps=19

#food
food_x=random.randint(2,hight)
food_y=random.randint(2,width)
food_size=23


#score
score=0

font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    setup.blit(screen_text,[x,y])




#loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x=+10
                velocity_y=0

            if event.key == pygame.K_LEFT:
                velocity_x=-10
                velocity_y=0

            if event.key==pygame.K_DOWN:
                velocity_y=+10
                velocity_x=0

            if event.key == pygame.K_UP:
                velocity_y=-10
                velocity_x=0


    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=1


        food_x = random.randint(2, hight)
        food_y = random.randint(2, width)
        food_size = 23



    setup.fill('white')
    text_screen("Score:"+str(score*10),red,10,6)

    pygame.draw.rect(setup,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(setup,red,[food_x,food_y,food_size,food_size])
    clock.tick(fps)
    pygame.display.update()
