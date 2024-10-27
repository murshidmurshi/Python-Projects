import pygame

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
velocity_x=10
velocity_y=10

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
                snake_x=snake_x+10

            if event.key==pygame.K_LEFT:
                snake_x=snake_x-10
            if event.key==pygame.K_UP:
                snake_y=snake_y-10
            if event.key==pygame.K_DOWN:
                snake_y=snake_y+10
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y




    gamewindow.fill('white')
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

