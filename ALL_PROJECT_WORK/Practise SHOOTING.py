
import pygame
import os
import random
import csv
import button
import pickle
pygame.init()
SCREEN_WIDTH=800
SCREEN_HIGHT=SCREEN_WIDTH*0.8

#screen setup
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
pygame.display.set_caption('SHOOTING --GAME')
clock=pygame.time.Clock()
fps=60
#define color
BG=(144,205,120)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)


#game variable
#gravity
GRAVITY=0.75
TILE_SIZE=40
ROW=20
COLMN=150
TILE_SIZE=SCREEN_HIGHT//ROW
TILE_TYPE=21
level=8
scroll=0
SCROLL_THRES=200
screen_scroll=0
bg_scroll=0


#define font
font=pygame.font.SysFont(None,30)
#define font
def draw_font(text,tex_color,font,x,y):
    img=font.render(text,True,tex_color)
    screen.blit(img,(x,y))


def BGcolor():
    screen.fill(BG)
def draw_line():
    pass
    #pygame.draw.line(screen,BLACK,(0,300),(SCREEN_WIDTH,300))
#player variable
moving_right=False
moving_left=False
shoot=False
grenade=False
grenade_throne=False
start_game=False

#load button
start_image=pygame.image.load('img/start_btn.png').convert_alpha()
exit_image=pygame.image.load('img/exit_btn.png').convert_alpha()
restart_image=pygame.image.load('img/restart_btn.png').convert_alpha()

#load all images
pine1_image=pygame.image.load('img/background/pine1.png').convert_alpha()
pine2_image=pygame.image.load('img/background/pine2.png').convert_alpha()
mountain_image=pygame.image.load('img/background/mountain.png').convert_alpha()
sky_image=pygame.image.load('img/background/sky_cloud.png').convert_alpha()
def draw_bg():
    for x in range(5):
        width=sky_image.get_width()
        screen.blit(sky_image,((x*width)-bg_scroll*0.5,0))
        screen.blit(mountain_image,((x*width)-bg_scroll*0.6,SCREEN_HIGHT-mountain_image.get_height()-300))
        screen.blit(pine1_image,((x*width)-bg_scroll*0.7,SCREEN_HIGHT-pine1_image.get_height()-150))
        screen.blit(pine2_image,((x*width)-bg_scroll*0.8,SCREEN_HIGHT-pine2_image.get_height()))

#function to reset the level
def reset_level():
    enemy_group.empty()
    bullet_group.empty()
    grenade_group.empty()
    explosion_group.empty()
    item_box_group.empty()
    decoration_group.empty()
    water_group.empty()
    exit_group.empty()

    # make empty tile list
    data = []
    for row in range(ROW):
        r = [-1] * COLMN
        data.append(r)
    return data





#bullet
img_list=[]
for x in range(TILE_TYPE):
    img=pygame.image.load(f'img/tile/{x}.png')
    img=pygame.transform.scale(img,(TILE_SIZE,TILE_SIZE))
    img_list.append(img)




bullet_image=pygame.image.load('img/icons/bullet.png').convert_alpha()
#Grenade
grenade_image=pygame.image.load('img/icons/grenade.png').convert_alpha()
#pick up boxes
health_box_img=pygame.image.load('img/icons/health_box.png').convert_alpha()
ammo_box_img=pygame.image.load('img/icons/ammo_box.png').convert_alpha()
grenade_box_img=pygame.image.load('img/icons/grenade_box.png').convert_alpha()
item_boxes={
    'Health' :health_box_img,
    'Ammo'   :ammo_box_img,
    'Grenade':grenade_box_img

}



class Sholdier(pygame.sprite.Sprite):
    def __init__(self,char_type,x,y,scale,speed,ammo,grenade):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.grenade=grenade
        self.in_air=True
        self.shoot_cooldown=0
        self.ammo=ammo
        self.start_ammo=ammo
        self.health=100
        self.max_health=self.health
        self.jump=False
        self.vel_y=0
        self.speed=speed
        self.char_type=char_type
        self.direction=1
        self.flip=False
        self.animation_list=[]
        self.action=0
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()
        #ai specific variable
        self.move_counter=0
        self.idling=False
        self.idling_counter=0
        self.vision=pygame.Rect(0,0,150,20)
        #loas all images for player
        animation_type=['Idle','Run','Jump','Death']
        for animation in animation_type:
            temp_list = []
            num_fram=len(os.listdir(f'img/{self.char_type}/{animation}'))
            for i in range(num_fram):
                img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img= pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image=self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width=self.image.get_width()
        self.height=self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown>0:
            self.shoot_cooldown-=1
    def move(self,moving_left,moving_right):
        #reset movement variable
        dx=0
        dy=0
        screen_scroll=0
        #assiign movement variable if moving right  or left
        if moving_left:
            dx=-self.speed
            self.flip=True
            self.direction=-1
        if moving_right:
            dx=self.speed
            self.flip = False
            self.direction =1
        #jump
        if self.jump==True and self.in_air==False:
            self.vel_y=-11
            self.jump=False
            self.in_air=True
        #apply gravity
        self.vel_y+=GRAVITY
        if self.vel_y>10:
            self.vel_y
        dy+=self.vel_y
        #check for collution
        for tile in world.obstacle_list:
            #check collition for x direction
            if tile[1].colliderect(self.rect.x+dx,self.rect.y,self.width,self.height):
                dx=0
                #if enemy hit the wall then move another side
                if self.char_type=='enemy':
                    self.direction*=-1
                    self.move_counter=0
            #check collition for y direction
            if tile[1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                #check if below the ground i.e, jumping
                if self.vel_y<0:
                    self.vel_y=0
                    dy=tile[1].bottom-self.rect.top
                #check if above the ground i.e, falling
                elif self.vel_y>=0:

                    self.vel_y=0
                    self.in_air=False
                    dy=tile[1].top-self.rect.bottom

        #check colloision with water
        if pygame.sprite.spritecollide(self,water_group,False):
            self.health=0
        if self.rect.bottom>SCREEN_HIGHT:
            self.health=0



        #check if player go out of the screen
        if self.char_type=='player':
            if self.rect.left+dx<0 or self.rect.right+dx>SCREEN_WIDTH:
                dx=0


        #update rectangle position
        self.rect.x+=dx
        self.rect.y+=dy
        #screen scroll based on player position
        if self.char_type=='player':
            if (self.rect.right>SCREEN_WIDTH-SCROLL_THRES and bg_scroll<(world.level_length*TILE_SIZE)-SCREEN_WIDTH)\
                    or (self.rect.left<SCROLL_THRES and bg_scroll>abs(dx)):
                self.rect.x-=dx
                screen_scroll=-dx
            return  screen_scroll




    def shoot(self):
        if self.shoot_cooldown==0 and self.ammo>0:
            self.shoot_cooldown=20
            bullet = Bullet(self.rect.centerx + 0.80 * self.rect.size[0] * self.direction, self.rect.centery,self.direction)
            bullet_group.add(bullet)
            #reduce ammo
            self.ammo-=1
    def ai(self):
        if self.alive and player.alive:
            if self.idling==False and random.randint(1,200)==1:
                self.update_action(0)#idle:0
                self.idling=True
                self.idling_counter=50
            #check if ai is near the player
            if self.vision.colliderect(player.rect):
                #stop running and face the player
                self.update_action(0)#idle:0
                #shoot
                self.shoot()
            else:

                if self.idling==False:
                    if self.direction==1:
                        ai_moving_right=True
                    else:
                        ai_moving_right=False
                    ai_moving_left=not ai_moving_right
                    self.move(ai_moving_left,ai_moving_right)
                    self.update_action(1)#1:run
                    self.move_counter+=1
                    #update ai vision as enemy move
                    self.vision.center=(self.rect.centerx+75*self.direction,self.rect.centery)
                    #pygame.draw.rect(screen,RED,self.vision)     #---want to see remove comment
                    if self.move_counter>TILE_SIZE:
                        self.direction*=-1
                        self.move_counter*=-1
                else:
                    self.idling_counter-=1
                    if self.idling_counter<=0:
                        self.idling=False

        #scroll the enemy
        self.rect.x+=screen_scroll



    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN=100
        #update image depending on current images
        self.image=self.animation_list[self.action][self.frame_index]
        #CHECK  if enough time has passed since last update
        if pygame.time.get_ticks()-self.update_time>ANIMATION_COOLDOWN:
            self.update_time=pygame.time.get_ticks()
            self.frame_index+=1

        #check if image run out of frame then reset it to back
        if self.frame_index>=len(self.animation_list[self.action]):
            if self.action==3:
                self.frame_index=len(self.animation_list[self.action])-1
            else:
                self.frame_index=0


    def update_action(self,new_action):
        if new_action!=self.action:
            self.action=new_action
            #update animation setting
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()

    def check_alive(self):
        if self.health<=0:
            self.health=0
            self.speed=0
            self.alive=False
            self.update_action(3)

    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)
        #pygame.draw.rect(screen,BLACK,self.rect,1)         #border of img

class World():
    def __init__(self):
        self.obstacle_list=[]

    def process_data(self,data):
        self.level_length=len(data[0])
        for y,row in enumerate(data):
            for x,tile in enumerate(row):
                if tile>=0:
                    img=img_list[tile]
                    img_rect=img.get_rect()
                    img_rect.x=x*TILE_SIZE
                    img_rect.y=y*TILE_SIZE
                    tile_data=(img,img_rect)
                    if tile>=0 and tile<=8:
                        self.obstacle_list.append(tile_data)
                    elif tile>=9 and tile<=10:
                        water = Water(img, x * TILE_SIZE, y * TILE_SIZE)
                        water_group.add(water)
                    elif tile>=11 and tile<=14:
                        decorator = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_group.add(decorator)
                    elif tile==15:#player
                        player= Sholdier('player', x * TILE_SIZE, y * TILE_SIZE, 1.65, 5, 20, 5)
                        health_bar = HealthBar(10, 10, player.health, player.health)
                    elif tile==16:
                        enemy = Sholdier('enemy', x*TILE_SIZE,y*TILE_SIZE, 1.65, 2, 20, 0)
                        enemy_group.add(enemy)
                    elif tile==17:#ammo
                        item_box = Item_box('Ammo', x*TILE_SIZE,y*TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile==18:#Grenade
                        item_box = Item_box('Grenade', x*TILE_SIZE,y*TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile==19:#health
                        item_box = Item_box('Health', x*TILE_SIZE,y*TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile==20:#exit
                        exit = Exit(img, x * TILE_SIZE, y * TILE_SIZE)
                        exit_group.add(exit)
        return player ,health_bar
    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0]+=screen_scroll
            screen.blit(tile[0],tile[1])



class Decoration(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.midtop=(x+TILE_SIZE//2,y+(TILE_SIZE-self.image.get_height()))

    def update(self):
        self.rect.x+=screen_scroll

class Water(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.midtop=(x+TILE_SIZE//2,y+(TILE_SIZE-self.image.get_height()))

    def update(self):
        self.rect.x+=screen_scroll

class Exit(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.midtop=(x+TILE_SIZE//2,y+(TILE_SIZE-self.image.get_height()))

class Item_box(pygame.sprite.Sprite):

    def __init__(self,item_type,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type=item_type
        self.image=item_boxes[self.item_type]
        self.rect=self.image.get_rect()
        self.rect.midtop=(x+TILE_SIZE//2,y+(TILE_SIZE-self.image.get_height()))

    def update(self):
        # scroll
        self.rect.x += screen_scroll
        #check if player has pick up box
        if pygame.sprite.collide_rect(self,player):
            if self.item_type=='Health':
                print(player.health)

                player.health+=25
                print(player.health)
                if player.health>player.max_health:
                    player.health=player.max_health
            elif self.item_type=='Ammo':
                player.ammo+=15
            elif self.item_type=='Grenade':
                player.grenade+=3
            #delet item box
            self.kill()

class HealthBar():
    def __init__(self,x,y,health,max_health):
        self.x=x
        self.y=y
        self.health=health
        self.max_health=max_health

    def draw(self,health):
        #update new health
        self.health=health
        #calculate ratio
        ratio=self.health/self.max_health
        # make border
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen,RED,(self.x,self.y,150,20))
        pygame.draw.rect(screen,GREEN,(self.x,self.y,150*ratio,20))






class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed=10
        self.image=bullet_image
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.direction=direction

    def update(self):
        #move bullet
        self.rect.x+=(self.direction*self.speed)+screen_scroll
        #check if bullet gone out of screen
        if self.rect.right<0 or self.rect.left>SCREEN_WIDTH-100:
            self.kill()

        #chceck for collition with level
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()


        #check collotion with character
        if pygame.sprite.spritecollide(player,bullet_group,False):
            if player.alive:
                player.health-=5
                self.kill()
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy,bullet_group,False):
                if enemy.alive:
                    enemy.health-=25
                    self.kill()

class Grenade(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer=100
        self.vel_y=-11
        self.speed=7
        self.image=grenade_image
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.width=self.image.get_width()
        self.height=self.image.get_height()
        self.direction=direction

    def update(self):
        self.vel_y+=GRAVITY
        dx=self.direction*self.speed
        dy=self.vel_y

        for tile in world.obstacle_list:
            # check collition with wall
            if tile[1].colliderect(self.rect.x+dx,self.rect.y,self.width,self.height):
                self.direction *= -1
                dx = self.direction * self.speed

            # check collition for y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                # check if below the ground i.e, thrown out
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground i.e, falling
                elif self.vel_y >=0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom

        #update grenade position
        self.rect.x+=dx+screen_scroll
        self.rect.y+=dy
        #count
        self.timer-=1
        if self.timer<=0:
            self.kill()
            explosion=Explosion(self.rect.x,self.rect.y,1)
            explosion_group.add(explosion)
            #do damage anything that near by
            if abs(self.rect.centerx-player.rect.centerx)<TILE_SIZE*2 and \
                    abs(self.rect.centery- player.rect.centery) < TILE_SIZE * 2:
                player.health-=25
            for enemy in enemy_group:
                if abs(self.rect.centerx-enemy.rect.centerx)<TILE_SIZE*2 and \
                    abs(self.rect.centery- enemy.rect.centery) < TILE_SIZE * 2:


                    enemy.health-=50
                    print(enemy.health)

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y,scale):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        for i in range(1,6):
            img=pygame.image.load(f'img/explosion/exp{i}.png')
            img=pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))
            self.images.append(img)
        self.frame_index=0
        self.image=self.images[self.frame_index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.counter=0

    def update(self):
        #scroll
        self.rect.x+=screen_scroll
        EXPLOSION_SPEED=4
        self.counter+=1
        if self.counter>=EXPLOSION_SPEED:
            self.counter=0
            self.frame_index+=1
            if self.frame_index>=len(self.images):
                self.kill()
            else:
                self.image=self.images[self.frame_index]




#make button
start_button=button.Button(250,SCREEN_HIGHT//2-100,start_image,1)
exit_button=button.Button(270,SCREEN_HIGHT//2+100,exit_image,1)
restart_button=button.Button(270,SCREEN_HIGHT//2-100,restart_image,1)


enemy_group=pygame.sprite.Group()
bullet_group=pygame.sprite.Group()
grenade_group=pygame.sprite.Group()
explosion_group=pygame.sprite.Group()
item_box_group=pygame.sprite.Group()
decoration_group=pygame.sprite.Group()
water_group=pygame.sprite.Group()
exit_group=pygame.sprite.Group()



#make empty tile list
world_data=[]

for row in range(ROW):
    r=[-1]*COLMN
    world_data.append(r)


with open(f'level{level}_data.csv',newline='')as csv_file:
   reader=csv.reader(csv_file,delimiter=',')
   for x,row in enumerate(reader):
       for y,tile in enumerate(row):
           world_data[x][y]=int(tile)

#pickle_out=open(f'level{level}data','wb')
#pickle.dump(world_data,pickle_out)
#pickle_out.close()
world=World()
player,health_bar=world.process_data(world_data)
run=True
while run:
    clock.tick(fps)

    if start_game==False:
        #draw the menu
        screen.fill(BG)
        #add button
        if start_button.draw(screen):
            start_game=True
        if exit_button.draw(screen):
            run=False
    else:
        BGcolor()
        draw_bg()

        draw_line()
        # update world map
        world.draw()
        health_bar.draw(player.health)
        draw_font('Ammo: ',BLACK,font,10,30)
        for x in range(player.ammo):
            screen.blit(bullet_image,(90 + (x*10),35))
        draw_font('Grenade: ',BLACK,font,10,60)
        for x in range(player.grenade):
            screen.blit(grenade_image,(110 + (x*10),63))

        player.draw()
        player.update()
        for enemy in enemy_group:
            enemy.ai()
            enemy.draw()
            enemy.update()

        #update and draw
        bullet_group.update()
        grenade_group.update()
        explosion_group.update()
        item_box_group.update()
        decoration_group.update()
        water_group.update()
        exit_group.update()

        bullet_group.draw(screen)
        grenade_group.draw(screen)
        explosion_group.draw(screen)
        item_box_group.draw(screen)
        decoration_group.draw(screen)
        water_group.draw(screen)
        exit_group.draw(screen)




        if player.alive:
            if shoot:
                player.shoot()
            elif grenade and grenade_throne==False and player.grenade>0:
                grenade=Grenade(player.rect.centerx+(0.5*player.rect.size[0]*player.direction),\
                                player.rect.top,player.direction)
                grenade_group.add(grenade)
                #reduce grenade
                player.grenade-=1
                grenade_throne=True
                print(player.grenade)
            if player.in_air:
                player.update_action(2)
            #update player action
            elif moving_left or moving_right:
                player.update_action(1)
            else:
                player.update_action(0)
            screen_scroll=player.move(moving_left,moving_right)
            bg_scroll-=screen_scroll
        else:
            screen_scroll=0
            if restart_button.draw(screen):
                bg_scroll=0
                world_data=reset_level()

                with open(f'level{level}_data.csv', newline='') as csv_file:
                    reader = csv.reader(csv_file, delimiter=',')
                    for x, row in enumerate(reader):
                        for y, tile in enumerate(row):
                            world_data[x][y] = int(tile)
                world = World()
                player, health_bar = world.process_data(world_data)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


        #Keyboard presses
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_a:
                moving_left=True
            if event.key==pygame.K_d:
                moving_right = True
            if event.key==pygame.K_q:
                grenade = True

            if event.key==pygame.K_SPACE:
                shoot = True

            if event.key==pygame.K_w and player.alive:
                player.jump = True

            if event.key==pygame.K_ESCAPE:
                run=False
        # Keyboard Released
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                 moving_left= False
            if event.key == pygame.K_d:
                 moving_right= False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_q:
                grenade = False
                grenade_throne=False

    pygame.display.update()

pygame.quit()