from OpenGL.GL import *
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys

class Eje:
    def __init__(self, opera):
        self.opera = opera
        self.points = np.array([[-1.0,0.0,1.0], [1.0, 0.0, 1.0], [0.0, -1.0, 1.0],[0.0, 1.0, 1.0]])


    def draw(self):
        pointsE = self.points.copy()
        pointsE = self.points.copy()

        glLineWidth(5)
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(pointsE[0][0], pointsE[1][0])

        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(pointsE[2][1], pointsE[3][1])
        glEnd()




