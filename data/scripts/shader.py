import pygame, glm
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
from data.scripts.funcs import *

class Shader:
    def __init__(self, vpath, fpath):
        self.vpath = vpath
        self.fpath = fpath
        self.vertexShader = 0
        self.fragmentShader = 0

        vertexSource = load_file(self.vpath)
        fragmentSource = load_file(self.fpath)

        self.vertexShader = shaders.compileShader(vertexSource, GL_VERTEX_SHADER)
        self.fragmentShader = shaders.compileShader(fragmentSource, GL_FRAGMENT_SHADER)
        self.shader = shaders.compileProgram(self.vertexShader, self.fragmentShader)

    def use_shader(self):
        glUseProgram(self.shader)
    
    def set_bool(self, uName, uVal):
        glUniform1i(glGetUniformLocation(self.shader, uName), uVal)

    def set_vec1(self, uName, uVal1):
        glUniform1f(glGetUniformLocation(self.shader, uName), uVal1)
        
    def set_vec2(self, uName, uVal1, uVal2):
        glUniform2f(glGetUniformLocation(self.shader, uName), uVal1, uVal2)

    def set_vec3(self, uName, uVal1, uVal2, uVal3):
        glUniform3f(glGetUniformLocation(self.shader, uName), uVal1, uVal2, uVal3)

    def set_vec4(self, uName, uVal1, uVal2, uVal3, Uval4):
        glUniform4f(glGetUniformLocation(self.shader, uName), uVal1, uVal2, uVal3, Uval4)

    def set_mat4(self, uName, uVal):
        glUniformMatrix4fv(glGetUniformLocation(self.shader, uName), 1, GL_FALSE, glm.value_ptr(uVal))

    def clear_screen(self, R, G, B, A):
        glClearColor(R, G, B, A)

    def delete(self):
        try:
            glDeleteShader(self.vertexShader)
            glDeleteShader(self.fragmentShader)
            glDeleteShader(self.shader)
        except:
            pass






