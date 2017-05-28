import pygame

screen = pygame.display.set_mode((400,400))
pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()
# pygame.joystick.Joystick.init()
# Prints the joystick's name
JoyName = pygame.joystick.Joystick(0).get_name()
print ("Name of the joystick:")
print (JoyName)
# Gets the number of axes
JoyAx = pygame.joystick.Joystick(0).get_numaxes()
print ("Number of axis:")
print (JoyAx)

"""
num 0 = A
num 1 = B
num 2 = X
num 3 = Y
num 4 = LB
num 5 = RB
num 6 = Back
num 7 = Start
num 8 = LS
num 9 = RS


"""
# Prints the values for axis0
while True:
    screen.fill((0,0,0))
    pygame.event.pump()
    pygame.draw.circle(screen,(100,100,255),(100,100),100,2)
    pygame.display.update()
    # ko = pygame.joystick.Joystick(0).get_axis(0)
    # print(ko)

    # pygame.time.wait(90)
    # for i in range(0,10):
    #     if pygame.joystick.Joystick(0).get_button(i) == 1:
    #         print('yes',i)
    #