import pygame
import os

pygame.init()
clock=pygame.time.Clock()
FPS=60
screen_width=800
screen_hight=screen_width*0.8

screen=pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption('Shooter')

#define game variable
GRAVITY=0.75
TILE_SIZE=40

#define player variable
moving_left=False
moving_right=False
shoot=False
grenade=False
grenade_throne=False

#load image
#bullet
bullet_img=pygame.image.load('img/icons/bullet.png').convert_alpha()
grenade_img=pygame.image.load('img/icons/grenade.png').convert_alpha()

#define color
BG=(144,201,120)
black=(0,0,0)
RED=(255,0,0)
Green=(0,255,0)
#define  font
font=pygame.font.SysFont(None,33)
#define text
def draw_text(text,tex_color,font,x,y):
    img=font.render(text,True,tex_color)
    screen.blit(img,(x,y))

def draw_BG():
    screen.fill(BG)
    pygame.draw.line(screen,RED,(0,300),(screen_width,300))
#pick up box
health_box_img=pygame.image.load('img/icons/health_box.png')
ammo_box_img=pygame.image.load('img/icons/ammo_box.png')
grenade_box_img=pygame.image.load('img/icons/grenade_box.png')




#define item_tyoe
item_boxes={
    'Health' :health_box_img,
    'Ammo'   :ammo_box_img,
    'Grenade':grenade_box_img
}
class Soldier(pygame.sprite.Sprite):
    def __init__(self,char_type,x,y,scale,speed,ammo,grenade):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.char_type=char_type
        self.speed=speed
        self.grenade=grenade
        self.ammo=ammo
        self.health=100
        self.max_health=self.health
        self.start_ammo=ammo
        self.shoot_cooldown=0
        self.direction=1
        self.vel_y=0
        self.jump=False
        self.in_air=True
        self.flip=False
        self.animation_list = []
        self.fram_index = 0
        self.action=0
        self.update_time=pygame.time.get_ticks()
        #ai specific variable
        self.move_counter=0
        #load all image for players
        animation_type=['Idle','Run','Jump','death']
        for animation in animation_type:
            #reset temporary list of images
            temp_list=[]
            #count number of file in folder
            num_of_frames=len(os.listdir(f'img/{char_type}/{animation}'))
            for i in range(num_of_frames):
                img=pygame.image.load(f'img/{char_type}/{animation}/{i}.png').convert_alpha()
                img= pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image=self.animation_list[self.action][self.fram_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.update_animation()
        self.check_alive()
        #update cooldown
        if self.shoot_cooldown>0:
            self.shoot_cooldown-=1

    def move(self,moving_left,moving_right):
        #reset movement variable
        dx=0
        dy=0
        #assign movement variable if moving_left or right
        if moving_left:
            dx=-self.speed
            self.flip=True
            self.direction=-1
        if moving_right:
            dx=self.speed
            self.flip = False
            self.direction = 1

        if self.jump==True and self.in_air==False:
            self.vel_y=-11
            self.jump=False
            self.in_air=True

        #apply Gravity
        self.vel_y+=GRAVITY
        if self.vel_y>10:
            self.vel_y
        dy+=self.vel_y
        #check collision with floor
        if self.rect.bottom+ dy >300:
            dy=300-self.rect.bottom
            self.in_air=False

        #update resctangle
        self.rect.x+=dx
        self.rect.y+=dy

    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN=100
        #update image
        self.image=self.animation_list[self.action][self.fram_index]
        # check if enough time has passed since last update
        if pygame.time.get_ticks()-self.update_time>ANIMATION_COOLDOWN:
            self.update_time=pygame.time.get_ticks()
            self.fram_index+=1
        # check if image is run out then update it to beginning
        if self.fram_index>=len(self.animation_list[self.action]):
            if self.action==3:
                self.fram_index=len(self.animation_list[self.action])-1
            else:
                self.fram_index=0

    def update_action(self,new_action):
        #check if new action is different to previous one
        if new_action!=self.action:
            self.action=new_action

            #update animation setting
            self.fram_index=0
            self.update_time=pygame.time.get_ticks()

    def check_alive(self):
        if self.health<=0:
            self.health=0
            self.speed=0
            self.alive=False
            self.update_action(3)


    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False), self.rect)

    def shoot(self):
        if self.shoot_cooldown==0 and self.ammo>0:
            self.shoot_cooldown=20
            bullet = Bullet(self.rect.centerx + (0.5 * self.rect.size[0] * self.direction), self.rect.centery,self.direction)
            bullet_group.add(bullet)
            #reduce ammo
            self.ammo-=1
    def ai(self):
        if self.alive and player.alive:
            if self.direction==1:

                ai_moving_right=True
            else:
                ai_moving_right=False
            ai_moving_left=not ai_moving_right
            self.move(ai_moving_left,ai_moving_right)
            self.move_counter+=1
            if self.move_counter>TILE_SIZE:
                self.direction*=-1
                self.move_counter*=-1




class ItemBox(pygame.sprite.Sprite):
    def __init__(self,item_type,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type=item_type
        self.image=item_boxes[self.item_type]
        self.rect=self.image.get_rect()
        self.rect.midtop=(x+TILE_SIZE//2,y+(TILE_SIZE-self.image.get_height()))

    def update(self):
        #check if player has pick up boxes
        if pygame.sprite.collide_rect(self,player):
            if self.item_type=='Health':
                print(player.health)
                player.health+=25
                if player.health>player.max_health:
                    player.health=player.max_health
                print(player.health)

            elif self.item_type == 'Ammo':
                player.ammo +=15
            elif self.item_type=='Grenade':
                player.grenade+=3
            self.kill()

class HealthBar():
    def __init__(self,x,y,health,max_health):
        self.x=x
        self.y=y
        self.healh=health
        self.max_health=max_health
    def draw(self,health):
        #new health
        self.health=health
        ratio=player.health/player.max_health
        pygame.draw.rect(screen,black,(self.x-2,self.y-2,184,29))
        pygame.draw.rect(screen,RED,(self.x,self.y,180,25))
        pygame.draw.rect(screen,Green,(self.x,self.y,180*ratio,25))



class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed=10
        self.image=bullet_img
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.direction=direction

    def update(self):
        #move bullet
        self.rect.x+=(self.direction*self.speed)
        #check if the bullet  go out off screeen
        if self.rect.right<0 or self.rect.left>screen_width-100:
            self.kill()
        #check collution with character
        if pygame.sprite.spritecollide(player,bullet_group,False):
            if player.alive:
                player.health-=5
                self.kill()
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health-=25
                    print(enemy.health)
                    self.kill()

class Grenade(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer=100
        self.vel_y=-11
        self.speed=7
        self.image=grenade_img
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.direction=direction
    def update(self):
        self.vel_y+=GRAVITY
        dx=self.direction*self.speed
        dy=self.vel_y
        # check collision with floor
        if self.rect.bottom + dy > 300:
            dx = self.direction * self.speed
            dy = 300 - self.rect.bottom
            self.speed=0
        #check if the Grenade  go out off screeen
        if self.rect.left+dx<0 or self.rect.right+dx>screen_width:
            self.direction*=-1
            dx=self.direction*self.speed

        #upgrade Grenade position
        self.rect.x+=dx
        self.rect.y+=dy

        #count_down
        self.timer-=1
        if self.timer<=0:
            self.kill()
            explsion=Explosion(self.rect.x,self.rect.y,1)
            explosion_group.add(explsion)
            #do damage to anyone that is nearby
            if abs(self.rect.centerx-player.rect.centerx)<TILE_SIZE*2 and\
                abs(self.rect.centery-player.rect.centery)<TILE_SIZE*2:
                player.health-=25
            for enemy in enemy_group:
                if abs(self.rect.centerx-enemy.rect.centerx)<TILE_SIZE*2 and\
                    abs(self.rect.centery-enemy.rect.centery)<TILE_SIZE*2:
                    enemy.health-=50
                    print(enemy.health)




class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y,scale):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        for num in range(1,6):
            img=pygame.image.load(f'img/explosion/exp{num}.png')
            img=pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))
            self.images.append(img)
        self.frame_index=0
        self.image=self.images[self.frame_index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.counter=0
    def update(self):
        EXPLOSION_SPEED=4
        self.counter+=1
        if self.counter>=EXPLOSION_SPEED:
            self.counter=0
            self.frame_index+=1
            if self.frame_index>=len(self.images):
                self.kill()
            else:
                self.image=self.images[self.frame_index]

#create sprite groups
enemy_group=pygame.sprite.Group()
bullet_group=pygame.sprite.Group()
grenade_group=pygame.sprite.Group()
explosion_group=pygame.sprite.Group()
item_box_group=pygame.sprite.Group()

#temp create boxes
item_box=ItemBox('Health',350,260)
item_box_group.add(item_box)
item_box=ItemBox('Ammo',400,260)
item_box_group.add(item_box)
item_box=ItemBox('Grenade',600,260)
item_box_group.add(item_box)



player=Soldier('player',200,200,1.65,5,25,5)
health_bar=HealthBar(10,10,player.health,player.health)
enemy=Soldier('enemy',400,200,1.65,5,25,0)
enemy2=Soldier('enemy',600,300,1.65,5,25,0)

enemy_group.add(enemy)
enemy_group.add(enemy2)



run=True
while run:
    clock.tick(FPS)
    draw_BG()
    draw_text('Ammo:',black,font,10,60)
    health_bar.draw(player.health)
    for x in range(player.ammo):
        screen.blit(bullet_img,(110+(x*10),70))
    draw_text('Grenade:',black,font,10,90)
    for x in range(player.grenade):
        screen.blit(grenade_img,(110+(x*10),94))
    player.update()
    player.draw()

    for enemy in enemy_group:
        enemy.ai()
        enemy.update()
        enemy.draw()
    #update and draw
    bullet_group.update()
    grenade_group.update()
    explosion_group.update()
    item_box_group.update()

    bullet_group.draw(screen)
    grenade_group.draw(screen)
    explosion_group.draw(screen)
    item_box_group.draw(screen)

    #update player action
    if player.alive:
        #shoot bullet
        if shoot:
            player.shoot()
        elif grenade and grenade_throne==False and player.grenade>0:
            grenade=Grenade(player.rect.centerx+0.5*player.rect.size[0]*player.direction,\
                            player.rect.top,player.direction)
            grenade_group.add(grenade)
            player.grenade-=1
            grenade_throne=True
            print(player.grenade)
        if player.in_air:
            player.update_action(2)##2: jump
        elif moving_left or moving_right:
            player.update_action(1)##1:run
        else:
            player.update_action(0)##0:idle
    player.move(moving_left,moving_right)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:   #quite
            run=False
        #key presses
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                moving_left=True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_q:
                grenade = True
            #Jump key
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.key==pygame.K_ESCAPE:
                run=False
        # key Released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_q:
                grenade = False
                grenade_throne=False



    pygame.display.update()

pygame.quit()