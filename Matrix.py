import math

import numpy as np
import math as m
import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *


class OpMat2D:
    def _init_(self):
        self.T = np.identity(3)
        self.R = np.identity(3)
        self.S = np.identity(3)
        self.A = np.identity(3)
        # identity(3) significa que regresa la matriz 3x3 como matriz identidad/reseteada

    def loadIdentity(self):
        self.T = np.identity(3)
        self.R = np.identity(3)
        self.S = np.identity(3)
        self.A = np.identity(3)

    def mult_points(self, points):
        return points @ self.A.T  # p′=pAT

    def translate(self, dx, dy):
        self.T = np.array([[1, 0, dx],
                           [0, 1, dy],
                           [0, 0, 1]])
        self.A = self.T @ self.A

    def scalate(self, sx, sy):
        scale = np.array([[sx, 0, 0, ]
                          [0, sy, 0]
                          [0, 0, 1,]
                          ])
        self.A = self.S @ self.A

    def rotation(self, theta):
        # do gdos a radianes
        grad = np.deg2rad(theta)
        self.R = np.array([[math.cos(grad), -math.sin(grad), 0],
                           [math.sin(grad), math.cos(grad), 0],
                           [0, 0, 1]])
        self.A = self.R @ self.A

    # Funciones print ADD for Debuggin

    def printTransformation(self):
        for x, y in self.T:
            print(x, y)