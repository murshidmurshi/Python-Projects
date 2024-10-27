import pygame
import os


#initiaize
pygame.init()

screen_width=800
screen_hight=screen_width*0.8

screen=pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption('Shooter')
clock=pygame.time.Clock()
fps=60

#define player variable
moving_left=False
moving_right=False
shoot=False

#load images
#bullet
bullet_image=pygame.image.load('img/icons/bullet.png')
#define game variable
GRAVITY=0.60
#define color
BG=(144,201,120)
RED=(255,0,0)
def BGcolor():
    screen.fill(BG)
    pygame.draw.line(screen,RED,(0,300),(screen_width,300))




class Soldier(pygame.sprite.Sprite):
    def __init__(self,char_type,x,y,scale,speed,ammo):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.shoot_cooldown=0
        self.ammo=ammo
        self.start_ammo=ammo
        self.health=100
        self.max_health=self.health
        self.vel_y=0
        self.char_type=char_type
        self.speed=speed
        self.direction=1
        self.jump=False
        self.in_air=True
        self.flip=False
        self.animation_list=[]
        self.fram_index=0
        self.action=0
        self.update_time=pygame.time.get_ticks()
        #load all images
        animation_type=['Idle','Run','Jump','death']
        for animation in animation_type:
             #reset temporary list of images
            temp_list=[]
             #count number of file in folder
            num_of_frame=len(os.listdir(f'img/{char_type}/{animation}'))

            for i in range(num_of_frame):
                img=pygame.image.load(f'img/{char_type}/{animation}/{i}.png')
                img=pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image=self.animation_list[self.action][self.fram_index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)


    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown>0:
            self.shoot_cooldown-=1




    def move(self,moving_left,moving_right):
        dx=0
        dy=0
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


        #apply GRAVITY
        self.vel_y+=GRAVITY
        if self.vel_y>10:
            self.vel_y
        dy += self.vel_y

        # check collotion with floor
        if self.rect.bottom + dy>300:
            dy=300-self.rect.bottom
            self.in_air=False


        #update rectangle
        self.rect.x+=dx
        self.rect.y+=dy

    def update_animation(self):
        ANIMATION_COOLDOWN=100
        #update image
        self.image=self.animation_list[self.action][self.fram_index]

        if pygame.time.get_ticks()-self.update_time>=ANIMATION_COOLDOWN:
            self.update_time=pygame.time.get_ticks()
            self.fram_index+=1

        # update if img is run finishing then update it to begiinning
        if self.fram_index>=len(self.animation_list[self.action]):
            if self.action==3:
                self.fram_index=len(self.animation_list[self.action])-1
            else:
                self.fram_index=0


    def update_action(self,new_action):
        # check if action is same as previous one
        if new_action!=self.action:
            self.action=new_action
            # update animation setting
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
            bullet = Bullet(self.rect.centerx + (0.5 * self.rect.size[0] *self.direction),self.rect.centery,self.direction)
            bullet_group.add(bullet)
            self.ammo-=1

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
        self.rect.x+=(self.direction*self.speed)
        # check bullet gone out of screen
        if self.rect.right<0 or self.rect.left>screen_width-100:
            self.kill()
        #check collution with character
        if pygame.sprite.spritecollide(player,bullet_group,False):
            if player.alive:
                player.health-=5
            self.kill()
        if pygame.sprite.spritecollide(enemy,bullet_group,False):
            if enemy.alive:
                enemy.health-=25
                print(enemy.health)
            self.kill()
#create group
bullet_group=pygame.sprite.Group()
player=Soldier('player',200,200,1.65,5,5)
enemy=Soldier('enemy',400,200,3,5,20)





run=True
while run:
    clock.tick(fps)
    BGcolor()
    player.update()
    player.draw()
    enemy.draw()
    enemy.update()

    #update and draw
    bullet_group.update()
    bullet_group.draw(screen)
    if player.alive:
        if shoot:
            player.shoot()

        if player.in_air:
            player.update_action(2) # 2:jump
        elif moving_left or moving_right:
            player.update_action(1) # 1:run
        else:
            player.update_action(0) #0:idle
    player.move(moving_left,moving_right)



    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            run=False
        # key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                player.jump = True
            if event.key == pygame.K_SPACE:
                shoot = True

            if event.key==pygame.K_ESCAPE:
                run=False
        # key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False

    pygame.display.update()

pygame.quit()