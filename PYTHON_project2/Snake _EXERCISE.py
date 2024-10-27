import pygame
import random


pygame.init()

width=600
hight=600

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

velocity_x=0
velocity_y=0
fps=27

#snake measurement
snake_x=10
snake_y=10
snake_size=19

#food measurement
food_x=random.randint(2,width/2)
food_y=random.randint(2,hight/2)
food_size=20
score=0


screen=pygame.display.set_mode((width,hight))
pygame.display.set_caption('SNAKE __GAME')
pygame.display.update()
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y ):
    screen_text=font.render(text,True,color)
    screen.blit(screen_text,[x,y])


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


    if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
        score+=1
        food_x = random.randint(0, width/2)
        food_y = random.randint(0, hight/2)
        print("SCORE:"+str(score*10))
    screen.fill('red')
    text_screen("Score:"+str(score*10),white,6,11)
    pygame.draw.rect(screen,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(screen,white,[food_x,food_y,food_size,food_size])
    clock.tick(fps)
    pygame.display.update()
pygame.quit()




