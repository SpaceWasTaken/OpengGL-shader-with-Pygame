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
WIDTH, HEIGHT = 800, 600 # 4:3

win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF|pygame.OPENGL)
surface = pygame.Surface((400/1.5, 300/1.5))

shader = Shader('data/scripts/vertex.txt', 'data/scripts/fragment.txt')
pixel_texture = Texture()

opengl = Opengl((WIDTH, HEIGHT))
camera = Camera(5, 2, 5)

# vars
aspectratio = WIDTH/HEIGHT 
angle = 0
img_pos = glm.vec3(0, 0, -12)


def draw_rect():
    shader.use_shader()

    use_texture([pixel_texture.tex_id], [GL_TEXTURE0])
    glBindVertexArray(opengl.VAO)
    
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)  

def __blit__():
    global pixel_texture
    # opengl render stuff
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)
    
    draw_rect()

    surface.blit(tree_img, (WIDTH//6 - tree_img.get_width()//2, HEIGHT//6 - tree_img.get_height()//2))
    win.blit(pygame.transform.scale(surface, win.get_rect().size), (0,0))
    pixel_texture.create_texture(tree_img)

    pixel_texture.delete()
    pygame.display.flip()

def main():
    shader.use_shader()
    shader.set_bool('sWaterTex', 0)
    
    FPS = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        
        shader.use_shader()
        glBindVertexArray(opengl.VAO)
        shader.clear_screen(0.1, 0.1, 0.1, 1.0)

        cam_view = camera.create_view()
        
        clock.tick(FPS)
        win.fill((255, 255, 255))
        pygame.display.set_caption(str(f"FPS : {clock.get_fps()}"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #____________________________________________________# 
        time = pygame.time.get_ticks()/500
        colorVal = (math.cos(time))+0.8
        if colorVal < 0.5:
            colorVal = 0.5

        # projection _________________________________________#
        img_pos = glm.vec3(0, 0, -12)
        model = glm.mat4(1)
        model = glm.rotate(model, glm.radians(0), glm.vec3(0, 0.5, .5))

        trans = glm.mat4(1)
        trans = glm.translate(trans, img_pos)
        trans = glm.scale(trans, glm.vec3(2,2,0))

        projection = glm.mat4(1)
        projection = glm.perspective(glm.radians(45), aspectratio, 0.1, 100)
        ortho_proj = glm.ortho(-1, 1, -(HEIGHT/WIDTH), (HEIGHT/WIDTH), 0.1, 10) * trans  # orthographic position to retain the scaling while rotating

        shader.set_vec1('vtime', pygame.time.get_ticks()/1000)
        shader.set_vec4('vertexColorRGB', colorVal, 0.8, 1.4, 1)
        shader.set_mat4('model', model)
        shader.set_mat4('view', trans)
        shader.set_mat4('projection', projection)
        shader.set_mat4('vertexRotation', ortho_proj)
        
        #____________________________________________________# 

        __blit__()

    shader.delete()
    pixel_texture.delete()
    delete_buffers(opengl.VAO, opengl.VBO, opengl.EBO)
    pygame.quit()
    
main()















