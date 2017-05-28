import pygame
import sys, random
from pygame.locals import *


w = 800
h = 400

z = 0
screen = pygame.display.set_mode((w,h))

pygame.display.update()

class Ball:
    def __init__(self, radius, y,x, color, size , maxforce, force, life):
        self.y = y
        self.x = x
        self.color = color
        self.size = size
        self.maxforce = maxforce
        self.force = force
        self.radius = radius
        self.life = life

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def fall(self):
        if self.y < h - self.radius:
            self.y+=self.force
            if self.force < self.maxforce:
                self.force += 1
        elif self.y > h-self.radius or self.y == h-self.radius:
            self.y = h-self.radius-1
            self.force = self.force*-1
            self.maxforce = (self.maxforce/2)

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        self.life -=1
        if self.life < 0:
            ball.remove(self)


check = 0
clock = pygame.time.Clock()
ball = []
ball.append(Ball(25,250,250, (00,50,50), 'L', 25, 1, 100))

x = 0
while True:

    y = 0
    clock.tick(60)
    if x == 0:
        check = 1
    elif x == 800 or x > 800:
        check = 0
    # if x > 800 and check == 0 or x == 800 and check == 0:
    #     x-=4
    if x == 0 and check == 1 or x < 800 and check == 1:
        x += 10
    else:
        x -= 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif 3 == 3:
            z = 1
        elif event.type == MOUSEBUTTONUP:
            # z=
            pass

    if z == 1 :
        ball.append(Ball(25,y,x, (50,50,87), 'L', 25, 1, 100))
        z = 3
    elif z > 1:
        z -= 1


    screen.fill((0,0,0))

    for i in ball:
        i.fall()

    pygame.display.update()