import pygame

pygame.init()

SCREEN_WIDTH=800
SCREEN_HIGHT=640
SCREEN_SIDE=300
SCREEN_LOWER=100
#game window
screen=pygame.display.set_mode((SCREEN_WIDTH+SCREEN_SIDE,SCREEN_HIGHT+SCREEN_LOWER))
pygame.display.set_caption(' Editor')
#define clock
clock=pygame.time.Clock()
FPS=60
scroll_right=False
scroll_left=False
scroll=0
scroll_speed=1
#grid game variable
ROW=20
MAX_COLUMN=150
TILE_SIZE=SCREEN_HIGHT//ROW

#define color
GREEN=(144,201,120)
WHITE=(255,255,255)
RED=(200,25,25)

pine1_image=pygame.image.load('img/background/pine1.png').convert_alpha()
pine2_image=pygame.image.load('img/background/pine2.png').convert_alpha()
mountain_image=pygame.image.load('img/background/mountain.png').convert_alpha()
sky_image=pygame.image.load('img/background/sky_cloud.png').convert_alpha()

def draw_Bkgd():
    screen.fill(GREEN)
    width=sky_image.get_width()
    for x in range(4):
        screen.blit(sky_image, ((x*width)-scroll*0.5, 0))
        screen.blit(mountain_image, ((x*width)-scroll*0.6,SCREEN_HIGHT-mountain_image.get_height()-300))
        screen.blit(pine1_image,((x*width)-scroll*0.7, SCREEN_HIGHT-pine1_image.get_height()-150))
        screen.blit(pine2_image, ((x*width)-scroll*0.8, SCREEN_HIGHT-pine2_image.get_height()))

def draw_grid():
    for c in range(MAX_COLUMN+1):
        pygame.draw.line(screen,WHITE,(c*TILE_SIZE,0),(c*TILE_SIZE,SCREEN_HIGHT))
    for c in range(ROW+1):
      pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


run=True
while run:
    clock.tick(FPS)
    draw_Bkgd()
    draw_grid()
    if scroll_right==True:
        scroll+=5*scroll_speed
    if scroll_left==True:
        scroll-=5*scroll_speed
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                scroll_right=True
            if event.key==pygame.K_LEFT:
                scroll_left=True
            if event.key==pygame.K_RSHIFT:
                scroll_speed=5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                scroll_right=False
            if event.key==pygame.K_LEFT:
                scroll_left=False
            if event.key==pygame.K_RSHIFT:
                scroll_speed=1
    pygame.display.update()

pygame.quit()

