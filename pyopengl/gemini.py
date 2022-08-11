import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF |
                                 OPENGL)
pygame.display.set_caption('Gemini constellation')


def add_star(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)


done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        #Right twin
        add_star(138, 346, 8)   #Castor
        add_star(251, 359, 18)   #Theta Gem
        add_star(196, 320, 22)   #Tau Gem
        add_star(268, 251, 15)   #Mebsuta
        add_star(326, 217, 14)   #Tejat
        add_star(351, 216, 16)   #Propus
        add_star(383, 225, 7)   #1 Gem
        add_star(307, 189, 20)   #Nu Gem

        #Link
        add_star(152, 296, 7)   #L Gem

        #Left twin
        add_star(102, 301, 5)   #Pollux
        add_star(121, 289, 20)   #Upsilon Gem
        add_star(91, 263, 18)    #Kappa Gem
        add_star(158, 225, 16)   #Wasat
        add_star(154, 158, 18)   #Lambda Gem
        add_star(250, 104, 17)   #Alzirr
        add_star(203, 202, 19)   #Mekbuda
        add_star(276, 147, 9)   #Alhena

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
