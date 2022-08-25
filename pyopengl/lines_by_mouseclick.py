import pygame
import math
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Utils import *

pygame.init()

screen_width = 1000
screen_height = 800

ortho_left = 0
ortho_right = 640
ortho_top = 0
ortho_bottom = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Lines by mouse clicks')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_lines():
    for line in lines:
        glBegin(GL_LINE_STRIP)
        for point in line:
            glVertex2f(point[0], point[1])
        glEnd()


done = False

init_ortho()
glLineWidth(5)

lines = [[]]    # 2D array of each point of each line recorded
curr_line = 0   # Current line index

mouse_down = False  # True while mouse button is held down

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == MOUSEBUTTONUP:
            curr_line += 1
            lines.append([])
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            lines[curr_line].append(
                (
                    map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                    map_value(0, screen_height, ortho_bottom, ortho_top, p[1])
                )
            )

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_lines()
    pygame.display.flip()

pygame.quit()
