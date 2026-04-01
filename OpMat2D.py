import math
import numpy as np
import math as m
import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *

class OpMat2D:
    def __init__(self):
        self.T = np.identity(3)
        self.R = np.identity(3)
        self.E = np.identity(3)
        self.A = np.identity(3)
        self.stack = []
        #identity(3) significa que regresa la matriz 3x3 como matriz identidad/reseteada

        #self.T[0,0] += dx
        #self.T[0,1] += dy
        #self.T = np.identity(3)
    def translacion(self, dx, dy):
       translate = np.array([[1, 0, dx],
                            [0, 1, dy],
                            [0, 0, 1]
                             ])
       self.A = self.A @ translate

    def escalar(self, sx, sy):
        escalate = np.array([[sx,0,0],
                            [0,sy,0],
                            [0,0,1]
                            ])
        self.A = self.A @ escalate

    def rotacion(self, theta ):
        #do grados a radianes
        giro = np.deg2rad(theta)
        rotate = np.array([[math.cos(giro),-math.sin(giro),0],
                           [math.sin(giro),math.cos(giro),0],
                           [0,0,1]])
        self.A = self.A @ rotate

    def loadId(self):
        self.A = np.identity(3)

    def mult_Points(self, points):
        for i in range(len(points)):
            # points[i] es [x, y, 1]
            p_prime = self.A @ points[i]
           # print(f"punto {i}: {points[i]} -> {p_prime}")

            points[i][0] = p_prime[0]
            points[i][1] = p_prime[1]
            points[i][2] = p_prime[2]

    def pushMatrix(self):
        last = np.copy(self.A)
        self.stack.append(last)

    def popMatrix(self):
        self.A = self.stack.pop()


