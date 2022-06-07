import pygame, numpy, math, glm
from data.scripts.shader import *
from data.scripts.textures import *
from data.scripts.camera import *
from data.scripts.funcs import *
from data.scripts.load import *
from data.scripts.setup import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
WIDTH, HEIGHT = 800, 600 

win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF|pygame.OPENGL)

shader = Shader('data/scripts/vertex.txt', 'data/scripts/fragment.txt')

opengl = Opengl((WIDTH, HEIGHT))
camera = Camera(5, 2, 5)

# vars
aspectratio = WIDTH/HEIGHT 

def draw_rect():
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)  

def glRenderSetup():
    shader.use_shader()
    glBindVertexArray(opengl.VAO)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)

def __blit__():
    glRenderSetup()
    draw_rect()

    pygame.display.flip()

def main():
    shader.use_shader()
    
    FPS = 60
    clock = pygame.time.Clock()
    running = True
    while running:

        clock.tick(FPS)
        pygame.display.set_caption(str(f"FPS : {clock.get_fps()}"))
        
        shader.use_shader()
        glBindVertexArray(opengl.VAO)
        shader.clear_screen(set_color(10, 10, 10, 255))

        # cam_view = camera.create_view() # for view projection
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        __blit__()

    shader.delete()
    delete_buffers(opengl.VAO, opengl.VBO, opengl.EBO)
    pygame.quit()
    
main()















