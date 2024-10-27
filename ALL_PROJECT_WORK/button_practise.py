import pygame

pygame.init()

SCREEN_WIDTH=800
SCREEN_HIGHT=SCREEN_WIDTH*0.8

#screen setup
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
pygame.display.set_caption('BUTTON')

#load images
start_img=pygame.image.load('img/start_btn.png').convert_alpha()
exit_img=pygame.image.load('img/exit_btn.png').convert_alpha()

GREEN=(202,228,241)
class Button():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(scale*width,scale*height))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def draw(self):
        action=False
        #get mouse position
        pos=pygame.mouse.get_pos()

        #check if mouse is over or clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

start_button=Button(100,200,start_img,0.8)
exit_button=Button(450,200,exit_img,0.8)

run=True
while run:


    screen.fill(GREEN)
    if start_button.draw():
        print('START')
    if exit_button.draw():
        print('EXIT')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()