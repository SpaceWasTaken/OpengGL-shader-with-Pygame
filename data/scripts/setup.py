import pygame, numpy, math, glm

from OpenGL.GL import *
from OpenGL.GLU import *

class Opengl:
    def __init__(self, screen_res):
        self.screen_res = screen_res
        glViewport(0, 0, self.screen_res[0], self.screen_res[1])

        self.lineVertices = (
            1,  1, 0.0,  1.0, 1.0,  1.0, 1.0, 1.0,   
            1, -1, 0.0,  1.0, 0.0,  1.0, 1.0, 1.0,  
            -1, -1, 0.0,  0.0, 0.0,  1.0, 1.0, 1.0,  
            -1,  1, 0.0,  0.0, 1.0,  1.0, 1.0, 1.0)
        self.lineVertices = numpy.array(self.lineVertices, dtype=numpy.float32)

        self.lineEdges = (0, 1, 2, 2, 3, 0)
        self.lineEdges = numpy.array(self.lineEdges, dtype=numpy.int32)

        #____________________________________________________# Generating Buffers
        self.VAO = glGenVertexArrays(1) # buffer to hold data
        self.VBO = glGenBuffers(1) # buffer to manage data handling
        self.EBO = glGenBuffers(1) # buffer to draw indices
    
        glBindVertexArray(self.VAO)

        glBindBuffer(GL_ARRAY_BUFFER, self.VBO) # specifying the buffer type and binding it
        glBufferData(GL_ARRAY_BUFFER, self.lineVertices.nbytes, self.lineVertices, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO) # specifying the buffer type and binding it
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.lineEdges.nbytes, self.lineEdges, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)




