import pygame

#initialize pygame
pygame.init()

#create a display surface
width=500
height=500
display_surface=pygame.display.set_mode((width,height))
#hello world caption
pygame.display.set_caption('Hello')



#loop
running=True
while running:
    pass
    #loops through list of Event object that have occured
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            running=False
