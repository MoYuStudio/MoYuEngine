import os
import sys
import numpy
import random
import pygame
from pygame.locals import *

boarder = 16
tile_level = 1
tile_size = 64*tile_level
move_x,move_y = 19*30,3*30
mouse_x,mouse_y = (boarder/2*(tile_size/2)-boarder/2*(tile_size/2))+move_x,(boarder/2*(tile_size/4)+boarder/2*(tile_size/4))+move_y

# 8 * (64*1)/2 - 8 * (64*1)/2 + move_x , 8 * (64*1)/4 + 8 * (64*1)/4 +move_y
# x = 8 * (64*1)/2 - 8 * (64*1)/2 + move_x 
# x = mox / 8 * 8 * (64*1)/2 - 8 * (64*1)/2

mainwindow = pygame.display.set_mode((1200,600))
window_title = pygame.display.set_caption('TinyLand 弹丸之地')
#pygame.display.set_icon(.icon)
clock = pygame.time.Clock()

pygame.display.flip()

'''

def imageloard_TL():
    image_id = 0
    #path_before = os.getcwd()
    for i in range(0,25,1):

        image_name = 'tl' + str(image_id)
        image_name_Fin = image_name + 'Fin'
        path = 'resources/graphics/tileland/' + image_name + '.png'
        #pathFin = path_before + path
        print('='*30)
        print(path)

        get_file = os.path.isfile(path)

        image_id += 1

        if get_file == True:
            image_name = pygame.image.load(path).convert_alpha()
            image_name_Fin = pygame.transform.scale(image_name, (64 * tile_level,64 * tile_level))
            print('True')
        else:
            print('F')
            pass
    
    return image_name,image_name_Fin

'''

def tilemap_builder():
    global tilemap
    tilemap = [[random.randint(0,600) for i in range(0,boarder,1)] \
                    for j in range(0,boarder,1)]
    #print(tilemap)
    return tilemap

def tilemap_building_builder():
    global tilemap_building
    tilemap_building = [[random.randint(0,100) for i in range(0,boarder,1)] \
                    for j in range(0,boarder,1)]
    #print(tilemap_building)
    return tilemap_building

def buildable_builder():
    global buildable_map
    buildable_map = [[0 for i in range(0,boarder,1)] \
                    for j in range(0,boarder,1)]
    #print(buildable_map)
    return buildable_map

def tilebutton_builder():
    global tilebutton_map
    tilebutton_map = [[0 for i in range(0,boarder,1)] \
                    for j in range(0,boarder,1)]
    #print(tilebutton_map)
    return tilebutton_map

def tilemap_loader_first():
    global tilemap_x,tilemap_y

    tilemap_n = len(tilemap)
    tilemap_m = len(tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):
            
            if 0<=tilemap[tilemap_x][tilemap_y]<=50:
                tilemap[tilemap_x][tilemap_y] = 1
            
            if 51<=tilemap[tilemap_x][tilemap_y]<=500:
                tilemap[tilemap_x][tilemap_y] = 6
                        
            if 501<=tilemap[tilemap_x][tilemap_y]<=520:
                tilemap[tilemap_x][tilemap_y] = 11
                
            if 521<=tilemap[tilemap_x][tilemap_y] <=530:
                tilemap[tilemap_x][tilemap_y] = 16
                
            if 531<=tilemap[tilemap_x][tilemap_y] <=600:
                tilemap[tilemap_x][tilemap_y] = 21
                
    return tilemap_x,tilemap_y

def tilemap_loader():

    global tilemap_x,tilemap_y

    tilemap_n = len(tilemap)
    tilemap_m = len(tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):
            
            if tilemap[tilemap_x][tilemap_y] == 1:
                mainwindow.blit(tl1Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))

            if tilemap[tilemap_x][tilemap_y] == 6:
                mainwindow.blit(tl6Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))
                        
            if tilemap[tilemap_x][tilemap_y] == 11:
                mainwindow.blit(tl11Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))

            if tilemap[tilemap_x][tilemap_y] == 16:
                mainwindow.blit(tl16Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))
            
            if tilemap[tilemap_x][tilemap_y] == 21:
                mainwindow.blit(tl21Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))

    return tilemap_x,tilemap_y

def tilemap_building_loader_first():
    global tilemap_building_x,tilemap_building_y

    tilemap_building_n = len(tilemap_building)
    tilemap_building_m = len(tilemap_building[0])

    for tilemap_building_x in range(tilemap_building_n):
        for tilemap_building_y in range(tilemap_building_m):

            if 0<=tilemap_building[tilemap_building_x][tilemap_building_y]<=30 and buildable_map[tilemap_building_x][tilemap_building_y] == 1:
                tilemap_building[tilemap_building_x][tilemap_building_y] = 105
                
            if 31<=tilemap_building[tilemap_building_x][tilemap_building_y]<=100:
                pass

    return tilemap_building_x,tilemap_building_y

def tilemap_building_loader():
    global tilemap_building_x,tilemap_building_y

    tilemap_building_n = len(tilemap_building)
    tilemap_building_m = len(tilemap_building[0])

    for tilemap_building_x in range(tilemap_building_n):
        for tilemap_building_y in range(tilemap_building_m):

            if tilemap_building[tilemap_building_x][tilemap_building_y] == 105:
                mainwindow.blit(t105Fin,((tilemap_building_y*(tile_size/2)-tilemap_building_x*(tile_size/2))+move_x,(tilemap_building_y*(tile_size/4)+tilemap_building_x*(tile_size/4))-16*tile_level+move_y))
            
            if 31<=tilemap_building[tilemap_building_x][tilemap_building_y]<=100:
                pass

    return tilemap_building_x,tilemap_building_y

def buildable_loader():
    global buildable_map_x,buildable_map_y
    
    buildable_map_n = len(tilemap)
    buildable_map_m = len(tilemap[0])

    for buildable_map_x in range(buildable_map_n):
        for buildable_map_y in range(buildable_map_m):
            if tilemap[buildable_map_x][buildable_map_y] == 6:
                buildable_map[buildable_map_x][buildable_map_y] = 1

    return  buildable_map_x,buildable_map_y

def tilebutton_loader(mouse_pos_x,mouse_pos_y):
    global button_x_pos,button_y_pos
    
    tilebutton_map_n = len(tilebutton_map)
    tilebutton_map_m = len(tilebutton_map[0])

    for tilebutton_map_x in range(tilebutton_map_n):
        for tilebutton_map_y in range(tilebutton_map_m):
            button_x_pos = (tilebutton_map_y*(tile_size/2)-tilebutton_map_x*(tile_size/2))+move_x
            button_y_pos = (tilebutton_map_y*(tile_size/4)+tilebutton_map_x*(tile_size/4))+move_y

            print(button_x_pos,button_y_pos)

    return button_x_pos,button_y_pos

def move_up_Fn():
    global move_y,move_up
    if move_up == True:
        move_y += 5
    return move_y,move_up

def move_down_Fn():
    global move_y,move_down
    if move_down == True:
        move_y -= 5
    return move_y,move_down

def move_left_Fn():
    global move_x,move_left
    if move_left == True:
        move_x += 5
    return move_x,move_left

def move_right_Fn():
    global move_x,move_right
    if move_right == True:
        move_x -= 5
    return move_x,move_right



def button_loop(button_width,button_height,button_x_pos,button_y_pos,mouse_x_pos,mouse_y_pos,button_name = 'button',button_type = 'tile_type',button_type_data_1 = '0',button_type_data_2 = '0'):
    
    button_x = str(button_name) + '_x'
    button_y = str(button_name) + '_y'
    button_w = str(button_name) + '_w'
    button_h = str(button_name) + '_h'

    button_x, button_y = button_x_pos, button_y_pos
    button_w, button_h = button_width, button_height
                
    if button_x <= mouse_x_pos <= button_x + button_w and button_y <= mouse_y_pos <= button_y + button_h:
        print(str(button_name) + ' be clicked')




tilemap_builder()
tilemap_loader_first()
buildable_builder()
buildable_loader()
tilemap_building_builder()
tilemap_building_loader_first()

tilebutton_builder()

move_up = False
move_down = False
move_left = False
move_right = False

while True:

    tl1 = pygame.image.load('resources/graphics/tileland/TL1.png').convert_alpha()
    tl1Fin = pygame.transform.scale(tl1, (64 * tile_level,64 * tile_level))

    tl6 = pygame.image.load('resources/graphics/tileland/TL6.png').convert_alpha()
    tl6Fin = pygame.transform.scale(tl6, (64 * tile_level,64 * tile_level))

    tl11 = pygame.image.load('resources/graphics/tileland/TL11.png').convert_alpha()
    tl11Fin = pygame.transform.scale(tl11, (64 * tile_level,64 * tile_level))

    tl16 = pygame.image.load('resources/graphics/tileland/TL16.png').convert_alpha()
    tl16Fin = pygame.transform.scale(tl16, (64 * tile_level,64 * tile_level))

    tl21 = pygame.image.load('resources/graphics/tileland/TL21.png').convert_alpha()
    tl21Fin = pygame.transform.scale(tl21, (64 * tile_level,64 * tile_level))

    t105 = pygame.image.load('resources/graphics/tile/T105.png').convert_alpha()
    t105Fin = pygame.transform.scale(t105, (64 * tile_level,48 * tile_level))

    pretile_choose = pygame.image.load('resources/graphics/pretile/Pretilechoose.png').convert_alpha()
    pretile_chooseFin = pygame.transform.scale(pretile_choose, (64 * tile_level,32 * tile_level))
    
    tile_size = 64*tile_level

    mainwindow.fill((0,0,0))

    tilemap_loader()
    buildable_loader()
    tilemap_building_loader()

    move_up_Fn()
    move_down_Fn()
    move_left_Fn()
    move_right_Fn()

    mainwindow.blit(pretile_chooseFin,(mouse_x,mouse_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            mouse_pos_x,mouse_pos_y = event.pos
            tilebutton_loader(mouse_pos_x,mouse_pos_y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:
    
            if event.key == K_UP or event.key == K_w:
                move_up = True
                
            if event.key == K_DOWN or event.key == K_s:
                move_down = True

            if event.key == K_LEFT or event.key == K_a:
                move_left = True

            if event.key == K_RIGHT or event.key == K_d:
                move_right = True

            if event.key == K_q:
                tile_level += 1

            if event.key == K_e:
                if tile_level == 1:
                    tile_level = 1
                else:
                    tile_level -= 1

            if event.key == K_z:
                tile_level = 1
                move_x,move_y = 19*30,3*30

            if event.key == K_x:
                tilemap_builder()
                tilemap_loader_first()
                buildable_builder()
                buildable_loader()
                tilemap_building_builder()
                tilemap_building_loader_first()

        if event.type == pygame.KEYUP:

            if event.key == K_UP or event.key == K_w:
                move_up = False

            if event.key == K_DOWN or event.key == K_s:
                move_down = False

            if event.key == K_LEFT or event.key == K_a:
                move_left = False

            if event.key == K_RIGHT or event.key == K_d:
                move_right = False



    clock.tick(60)