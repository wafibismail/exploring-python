from OpenGL.GL import *
import pygame


class Mesh:
    def __init__(self):
        self.vertices = [
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5)
        ]
        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glVertex3f(
                self.vertices[self.triangles[t]][0],
                self.vertices[self.triangles[t]][1],
                self.vertices[self.triangles[t]][2]
            )
            glVertex3f(
                self.vertices[self.triangles[t + 1]][0],
                self.vertices[self.triangles[t + 1]][1],
                self.vertices[self.triangles[t + 1]][2]
            )
            glVertex3f(
                self.vertices[self.triangles[t + 2]][0],
                self.vertices[self.triangles[t + 2]][1],
                self.vertices[self.triangles[t + 2]][2]
            )
            glEnd()
