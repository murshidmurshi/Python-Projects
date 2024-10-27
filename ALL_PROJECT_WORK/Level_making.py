
import pickle
import pygame
import button
import csv
pygame.init()

SCREEN_WIDTH=800
SCREEN_HIGHT=640
SCREEN_SIDE=300
SCREEN_LOWER=100

screen=pygame.display.set_mode((SCREEN_WIDTH+SCREEN_SIDE,SCREEN_HIGHT+SCREEN_LOWER))
pygame.display.set_caption('Level--')
#define color
GREEN=(144,201,120)
WHITE=(255,255,255)
RED=(255,0,0)
#load images
pine1_image=pygame.image.load('img/background/pine1.png')
pine2_image=pygame.image.load('img/background/pine2.png')
mountain_image=pygame.image.load('img/background/mountain.png')
sky_image=pygame.image.load('img/background/sky_cloud.png')


save_img=pygame.image.load('img/save_btn.png')
load_img=pygame.image.load('img/load_btn.png')
scroll_right=False
scroll_left=False
scroll=0
scroll_speed=1
#game variable
current_tile=0
ROW=20
MAX_COLUMN=150
TILE_SIZE=SCREEN_HIGHT//ROW
TILE_TYPE=21
level=0
#define font
font=pygame.font.SysFont(None,30)
def drawtext(text,font,textcolor,x,y):
    img=font.render(text,True,textcolor)
    screen.blit(img,(x,y))




def draw():
    screen.fill(GREEN)
    width=sky_image.get_width()
    for x in range(4):
        screen.blit(sky_image, ((x * width) - scroll * 0.5, 0))
        screen.blit(mountain_image, ((x * width) - scroll * 0.6, SCREEN_HIGHT - 500))
        screen.blit(pine1_image, ((x * width) - scroll * 0.7, SCREEN_HIGHT - 420))
        screen.blit(pine2_image, ((x * width) - scroll * 0.8, SCREEN_HIGHT - 400))


#draw grid
def draw_grid():
    for c in range(MAX_COLUMN+1):
        pygame.draw.line(screen,WHITE,(c*TILE_SIZE-scroll,0),(c*TILE_SIZE-scroll,SCREEN_HIGHT))
    for c in range(ROW+1):
        pygame.draw.line(screen,WHITE,(0,c*TILE_SIZE),(SCREEN_WIDTH,c*TILE_SIZE))
#function for drawing world tile
def draw_world():
    for y,row in enumerate(world_data):
        for x,tile in enumerate(row):
            if tile>=0:
                screen.blit(img_list[tile],(x*TILE_SIZE-scroll,y*TILE_SIZE))



#tile
img_list=[]
for i in range(TILE_TYPE):
    img=pygame.image.load(f'img/tile/{i}.png')
    img=pygame.transform.scale(img,(TILE_SIZE,TILE_SIZE))
    img_list.append(img)
#make button
#buttoon list
button_list=[]
button_colm=0
button_row=0

for i in range(len(img_list)):
    tile_button=button.Button(SCREEN_WIDTH+75*button_colm+50,75*button_row+50,img_list[i],1)
    button_list.append(tile_button)
    button_colm+=1
    if button_colm==3:
        button_row+=1
        button_colm=0
#make empty list
world_data=[]
for row in range(ROW):
    r=[-1]*MAX_COLUMN
    world_data.append(r)
#make ground
for tile in range(0,MAX_COLUMN):
    world_data[ROW-1][tile]=0
print(world_data)

#make button
save_button=button.Button(350,SCREEN_HIGHT+SCREEN_LOWER-50,save_img,1)
load_button=button.Button(600,SCREEN_HIGHT+SCREEN_LOWER-50,load_img,1)

run=True
while run:

    draw()
    draw_grid()
    draw_world()
    drawtext(f'Level:{level}',font,WHITE,10,SCREEN_HIGHT+SCREEN_LOWER-90)
    drawtext('press UP or DOWN to increase level',font,WHITE,10,SCREEN_HIGHT+SCREEN_LOWER-70)
    if save_button.draw(screen):
        # save level data
        with open(f'level{level}_data.csv','w',newline='')as csv_file:
            writer=csv.writer(csv_file,delimiter=',')
            for row in world_data:
                writer.writerow(row)

    if load_button.draw(screen):
        with open(f'level{level}_data.csv', 'r', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for x,row in enumerate(reader):
                for y,tile in enumerate(row):
                    world_data[x][y]=int(tile)

    #draw tile pannel
    pygame.draw.rect(screen,GREEN,(SCREEN_WIDTH,0,SCREEN_SIDE,SCREEN_HIGHT))

    #choose a tile
    button_count=0
    for button_count,i in enumerate(button_list):
        if i.draw(screen):
            current_tile=button_count
    #highlight button
    pygame.draw.rect(screen,RED,(button_list[current_tile]).rect,3)

    #scroll the map
    if scroll_right==True and scroll<MAX_COLUMN*TILE_SIZE-SCREEN_WIDTH:
        scroll+=5*scroll_speed
    if scroll_left==True and scroll>ROW*TILE_SIZE-SCREEN_HIGHT:
        scroll-=5*scroll_speed

    #add new tile to the screen
    #get mouse position
    pos=pygame.mouse.get_pos()
    x=(pos[0]+scroll)//TILE_SIZE
    y=pos[1]//TILE_SIZE
    #check the coordinate within tile area
    if pos[0]<SCREEN_WIDTH and pos[1]<SCREEN_HIGHT:
        #update tile value
        if __name__ == '__main__':
            if pygame.mouse.get_pressed()[0]==1:
                if world_data[y][x]!=current_tile:
                    world_data[y][x]=current_tile
            if pygame.mouse.get_pressed()[2]==1:
                world_data[y][x]=-1


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_UP:
                 level+=1
             if event.key==pygame.K_DOWN and level>0:
                 level-=1
             if event.key==pygame.K_RIGHT:
                 scroll_right=True
             if event.key == pygame.K_LEFT:
                 scroll_left =True
             if event.key == pygame.K_RSHIFT:
                 scroll_speed = 5
        if event.type==pygame.KEYUP:
             if event.key==pygame.K_RIGHT:
                 scroll_right=False
             if event.key == pygame.K_LEFT:
                 scroll_left =False
             if event.key == pygame.K_RSHIFT:
                 scroll_speed = 5

    pygame.display.update()
pygame.quit()
