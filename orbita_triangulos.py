import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys
# Importamos las clases
from OpMat2D import OpMat2D
from Triangulo import Triangulo

#iniciamos ventana
pygame.init()
screen_width = 900
screen_height = 900
#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500


#triangulo ini
opera = OpMat2D()
t1 = Triangulo(opera)
t2 = Triangulo(opera)
t3 = Triangulo(opera)

    # Para diferenciarlos, le damos un color al t2 (ej. Rojo)
t1.setColor(255.0, 191.0, 0.0)
t2.setColor(0.0, 0.0, 1.0)
t3.setColor(107.0, 107.0, 107.0)




def Axis():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glShadeModel(GL_SMOOTH)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(X_MIN,0.0)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(X_MAX,1.0)
    glEnd()
    #Y axis in green
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(0.0,Y_MIN)
    glVertex2f(0.0,Y_MAX)
    glEnd()
    glLineWidth(1.0)

#def display():


def setup():
    screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: matrices de transformacion")
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluOrtho2D(-450, 450, -450, 450)
    gluOrtho2D(-600, 600, -600, 600)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0, 0, 0, 0)
    #gluOrtho2D(-10, 10.0, -10.0, 10.0)

setup()
angulo = 0
angle = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    opera.loadId()

    #Axis()
   # display()
    # opera y render
#sol; escalar, modificar puntos(para que rote sobre si mismo) y render
    opera.pushMatrix()
    opera.escalar(5.0, 5.0)
    #t1.setPoints([[-10.0,-6.7,1.0], [0.0, 13.3, 1.0], [10.0, -6.7, 1.0]])
    opera.rotacion(angulo)
    t1.render()
    opera.popMatrix()

# tierra y luna; rotar sobre el sol, transladado
    opera.pushMatrix()
    opera.rotacion(angulo)
    opera.translacion(200.0, 200.0)

    # tierra; escalar, rotar sobre su propio eje y render
    opera.pushMatrix()
    opera.escalar(3.0, 3.0)
    opera.rotacion(angulo)
    t2.render()
    opera.popMatrix()
    #opera.popMatrix()


# luna; escalar y rotar sobre la tierra
    opera.pushMatrix()
    opera.rotacion(angulo)
    opera.escalar(1.5, 1.5)
    opera.translacion(50.0,50.0)
    #opera.rotacion(angulo)
    t3.render()
    opera.popMatrix()
    opera.popMatrix()

    angulo += 1
    angle += 5

    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()