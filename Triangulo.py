from OpenGL.GL import *
import numpy as np


class Triangulo:
    def __init__(self, opera):
        self.opera = opera
        self.color = [1.0, 1.0, 1.0]
        self.dir = [0, 0]
        #puntos en el centro de la figura
        self.points = np.array([[-10.0,-6.7,1.0], [0.0, 13.3, 1.0], [10.0, -6.7, 1.0]])
        # points en el vertices exteriores
        #self.points = np.array([[0.0,0.0,1.0], [10.0, 20.0, 1.0], [20.0, 0.0, 1.0]]

       # self.points = np.array(points)

    def render(self):
        # la copia de los puntos es para no solo operar en el posh pop adonde apliques el render, para no modificar los puntos originales
        pointsR = self.points.copy()
        pointsR = self.points.copy()

        self.opera.mult_Points(pointsR)

        glColor3fv(self.color)
        glBegin(GL_TRIANGLES)
        glVertex2f(pointsR[0][0], pointsR[0][1])
        glVertex2f(pointsR[1][0], pointsR[1][1])
        glVertex2f(pointsR[2][0], pointsR[2][1])
        glEnd()


    def setPoints(self, nuevos_puntos):
              self.points = nuevos_puntos

    def update(self):
              self.dir[0] = 0


    def setColor(self, r, g, b):
        self.color[0] = r
        self.color[1] = g
        self.color[2] = b

    def ejes(self, points):
        self.points = points
        glBegin(GL_POINTS)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(points[0][0], points[0][1])
        glVertex2f(points[1][0], points[1][1])
        glVertex2f(points[2][0], points[2][1])
        glEnd()



    def centro(self):
        glBegin(GL_POINTS)
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(50)
        glVertex2f(0.0, 0.0)
        glEnd()
