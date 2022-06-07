import pygame, glm, math
from OpenGL.GL import *
from OpenGL.GLU import *
from data.scripts.funcs import *

class Camera:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vel = .5
        self.pos = (self.x, self.y, self.z)
        self.cameraFront = (-5, -2, -5)
        self.cameraUp = (0, 1, 0)
        self.radius = 10

    def create_view(self):
        view = glm.lookAt(glm.vec3(self.pos), glm.vec3(self.pos) + glm.vec3(self.cameraFront), self.cameraUp)
        return view







