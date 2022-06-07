# latest update at 6/5/2022
import pygame, math, os
from OpenGL.GL import *

def load_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

def set_img_colorkey(img, list=False):
    if list:
        for i in img:
            i.set_colorkey((255, 255, 255))
    else:
        img.set_colorkey((255, 255, 255))

def load_image(path):
    return pygame.image.load(path).convert()

def load_animation(path, base_name, img_count): # data/entities/player/ # player_walk_l
    img_count += 1 # adding one since 'range' starts from 0
    img_list = []
    count = 0
    loop = True

    if not path.endswith(os.path.sep):
        path += '/'
        
    for img in range(img_count):
        count += 1
        if count >= img_count:
            count = img_count
            loop = False

        if loop:
            imgs = path + base_name + str(count) + '.png' 
            load_img = pygame.image.load(imgs)
            img_list.append(load_img)

    return img_list

def get_iso_pos(x, y, width=16, height=16):# converts coords to isometric
    return (x * width) - (y * height), 0.5*((x * width) + (y * height))

def get_cart_pos(x, y, width=16, height=16):# converts coords to cartesian
    return ( 2 * (y/height) + (x/width) ) / 2 - 1, ( 2 * (y/height) - (x/width) ) / 2
        
def get_sortedList(sub_list):
    return (sorted(sub_list, key=lambda x : x[1][2]))

def create_range_rect(objx, objy, tile_range):
    from main import surface
    rect = pygame.Rect(objx, objy, tile_range * 2 , tile_range * 2)
    rect.center = (objx, objy)
    return rect

def get_angle(x, y, x2, y2, scroll=[0,0]):
    angle = math.atan2(y2 - (int(y)), x2 - (int(x)))
    return angle

def get_rot_angle(x, y, playerx, playery, scroll):
    angle = math.degrees(math.atan2(playery - (int(y)), playerx - (int(x))))
    return angle

def get_radians(degrees):
    return degrees * (math.pi/180)

def get_degrees(radians):
    return radians * (180/math.pi)

#OpenGL_____________________________________________#
def delete_shader(vertex, fragment):
    try:
        glDeleteShader(vertex)
        glDeleteShader(fragment)
    except:
        pass

def delete_buffers(vao, vbo, ebo):
    try:
        glDeleteVertexArrays(vao)
        glDeleteBuffers(vbo)
        glDeleteBuffers(ebo)
    except:
        pass

success = 0
infolog = [512]
def check_compilation(shader):
    glGetShaderiv(shader, GL_COMPILE_STATUS, success)
    if success != 0:
        glGetShaderInfoLog(shader, 512, None, infolog)
        print(f"ERROR::{infolog}")

def use_texture(tex_id, gltextures): # [pixel_texture, wave_texture]
        tex = [list(l) for l in zip(tex_id, gltextures)]
        for i in tex:
            glActiveTexture(i[1])
            glBindTexture(GL_TEXTURE_2D, i[0])

def set_color(R, G, B, A):
    return R/255, G/255, B/255, A/255


