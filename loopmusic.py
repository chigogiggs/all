import pygame,time
from pygame.locals import *
file  = 'bruh.mp3'

screen= pygame.display.set_mode((100,100))
pygame.init()
pygame.mixer.init()
music =pygame.mixer.music
music.load(file)
# music.set_volume(4)
strtvar = 10
var = 0
def genesis():
    def musical(strt):
        global var
        music.play(0,strt)
        strttime = time.time()

        clock = pygame.time.Clock()
        while True:
            currenttime = time.time()
            print( currenttime - strttime)
            if currenttime - strttime >31:
                musical(strt)
            pygame.event.poll()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        if var != 12:
                            var += 1
                            strt+=strtvar
                            musical(strt)
                        if var == 12:
                            var = 0
                            strt = 27
                            musical(strt)
            print(strt)
            pygame.display.update()


    musical(218)

try:
    genesis()
except:
    time.sleep(1)
    genesis()