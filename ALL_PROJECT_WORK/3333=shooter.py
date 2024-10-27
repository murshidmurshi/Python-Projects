import pygame

pygame.init()

screen_width=800
screen_hight=screen_width*0.8

screen=pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption('Shooter')

moving_left=False
moving_right=False
clock=pygame.time.Clock()
FPS=60

class Sholdier(pygame.sprite.Sprite):
    def __init__(self,char_type,x,y,scale,speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type=char_type
        self.direction=1
        self.flip=False
        self.speed=speed
        img = pygame.image.load(f'img/{char_type}/idle/0.png')
        self.image=pygame.transform.scale(img,(img.get_width()*scale,img.get_height()*scale))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)



    def move(self,moving_left,moving_right):
        dx=0
        dy=0
        if moving_left:
            dx=-self.speed
            self.flip=True
            self.direction=-1
        if moving_right:
            dx=self.speed
            self.flip=False
            self.direction=1
        self.rect.x+=dx
        self.rect.y+=dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)

player=Sholdier('player',200,200,3,3)
#define color
PG=(144,201,120)
def PGcolor():
    screen.fill(PG)
run=True
while run:
    clock.tick(FPS)
    PGcolor()
    player.draw()

    player.move(moving_left,moving_right)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        #keyboard Press
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                moving_left=True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False
        # keyboard Released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False


    pygame.display.update()

pygame.quit()
