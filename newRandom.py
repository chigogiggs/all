import pygame
import sys
from pygame.locals import *

bif  = 'bg.jpg'
mif = 'ball.png'

pygame.init()

screen = pygame.display.set_mode((640,360),0, 32)

background = pygame.image.load(bif).convert()

mouse_c = pygame.image.load(mif).convert_alpha()


x,y = 0,0
moveX, moveY = 0,0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveX = -1

            elif event.key == K_RIGHT:
                moveX = +1

            elif event.key == K_UP:
                moveY = -1

            elif event.key == K_DOWN:
                moveY = +1


        if event.type == KEYUP:

            if event.key == K_LEFT:
                moveX = 0

            elif event.key == K_RIGHT:
                moveX = 0

            elif event.key == K_UP:
                moveY = 0

            elif event.key == K_DOWN:
                moveY = 0



    moux , mousy = pygame.mouse.get_pos()
    j, h = mouse_c.get_width()/2, mouse_c.get_height()/2
    j= moux - j
    h=mousy - h

    screen.blit(background,(0,0))
    screen.blit(mouse_c, (j,h))

    pygame.display.update()