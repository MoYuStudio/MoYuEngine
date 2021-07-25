
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
move_speed = 5

tile_choose_info = [0,0,0,0,0,0]

mouse_x,mouse_y = (boarder/2*(tile_size/2)-boarder/2*(tile_size/2)),(boarder/2*(tile_size/4)+boarder/2*(tile_size/4))

mainwindow = pygame.display.set_mode((1200,600))
window_title = pygame.display.set_caption('TinyLand 弹丸之地')
#pygame.display.set_icon(.icon)
clock = pygame.time.Clock()
pygame.display.flip()

def tilemap_builder():
    global tilemap

    # 0 tile land   1 tile   2 time   3 buildable   4 tile button x   5 tile button y   6 Dv Code

    tilemap = [[[random.randint(0,600),random.randint(0,100),0,0,0,0,0] for i in range(0,boarder,1)] for j in range(0,boarder,1)]

    print(tilemap)
    return tilemap

def tilemap_loarder():
    global tilemap_x,tilemap_y

    tilemap_n = len(tilemap)
    tilemap_m = len(tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = tilemap[tilemap_x][tilemap_y]

            if tile_info[6] == 0:

            # === tile_land ===
                
                if 0<=tile_info[0]<=50:
                    tile_info[0] = 1
            
                if 51<=tile_info[0]<=500:
                    tile_info[0] = 6
                            
                if 501<=tile_info[0]<=520:
                    tile_info[0] = 11
                    
                if 521<=tile_info[0]<=530:
                    tile_info[0] = 16
                    
                if 531<=tile_info[0]<=600:
                    tile_info[0] = 21

            # === tile_building ===

                if 0<=tile_info[1]<=70:
                    tile_info[1] = 0

                if 71<=tile_info[1]<=100 and tile_info[0] == 6:
                    tile_info[1] = 105

            # === tile_time ===

            # === tile_buildable ===

            # === tile_pos_x ===

                tile_info[4] = (tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x

            # === tile_pos_y ===

                tile_info[5] = (tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y

            # === tile_dvcode ===

                tile_info[6] = 1

                #print(tilemap)

            if tile_info[6] == 1:

            # === tile_land ===

                if tile_info[0] == 1:
                    mainwindow.blit(tl1Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))

                if tile_info[0] == 6:
                    mainwindow.blit(tl6Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))
                            
                if tile_info[0] == 11:
                    mainwindow.blit(tl11Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))

                if tile_info[0] == 16:
                    mainwindow.blit(tl16Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))
                
                if tile_info[0] == 21:
                    mainwindow.blit(tl21Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y))

            # === tile_building ===

                if tile_info[1] == 0:
                    pass

                if tile_info[1] == 105:
                    mainwindow.blit(t105Fin,((tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x,(tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))-16*tile_level+move_y))

            # === tile_time ===

            # === tile_buildable ===

            # === tile_pos_x ===

                tile_info[4] = (tilemap_y*(tile_size/2)-tilemap_x*(tile_size/2))+move_x

            # === tile_pos_y ===

                tile_info[5] = (tilemap_y*(tile_size/4)+tilemap_x*(tile_size/4))+move_y

            # === tile_dvcode ===

def tilebutton_clicker(mouse_pos_x,mouse_pos_y):
    global tilemap_x,tilemap_y,tile_size,mouse_x,mouse_y,tile_choose_info

    tilemap_n = len(tilemap)
    tilemap_m = len(tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = tilemap[tilemap_x][tilemap_y]

            if tile_info[4]+8*tile_level <= mouse_pos_x <= tile_info[4]+8*tile_level + tile_size and tile_info[5]+8*tile_level <= mouse_pos_y <= tile_info[5]+8*tile_level + tile_size:
                mouse_x,mouse_y = (tile_info[4]-move_x),(tile_info[5]-move_y)

                tile_choose_info = tile_info

    return mouse_x,mouse_y,tile_choose_info

def tile_preview(tile_choose_info):
    global buildable_preview
    if tile_choose_info[3] == 0:
        buildable_preview = False

    if tile_choose_info[3] == 1:
        buildable_preview = True

    if buildable_preview == False:
        mainwindow.blit(pretile_redFin,(mouse_x+move_x,mouse_y+move_y)) 

    if buildable_preview == True:
        mainwindow.blit(pretile_greenFin,(mouse_x+move_x,mouse_y+move_y))

    mainwindow.blit(pretile_chooseFin,(mouse_x+move_x,mouse_y+move_y))

    return buildable_preview


def move_Fn():
    global move_x,move_y,move_up,move_down,move_left,move_right
    if move_up == True:
        move_y += move_speed
    if move_down == True:
        move_y -= move_speed
    if move_left == True:
        move_x += move_speed
    if move_right == True:
        move_x -= move_speed
    return move_x,move_y,move_up,move_down,move_left,move_right


tilemap_builder()

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

    pretile_green = pygame.image.load('resources/graphics/pretile/PretileGreen.png').convert_alpha()
    pretile_greenFin = pygame.transform.scale(pretile_green, (64 * tile_level,32 * tile_level))

    pretile_red = pygame.image.load('resources/graphics/pretile/PretileRed.png').convert_alpha()
    pretile_redFin = pygame.transform.scale(pretile_red, (64 * tile_level,32 * tile_level))
    
    tile_size = 64*tile_level

    mainwindow.fill((0,0,0))

    tilemap_loarder()

    move_Fn()

    tile_preview(tile_choose_info) 

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:

            mouse_pos_x,mouse_pos_y = event.pos

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos_x,mouse_pos_y = event.pos
            
            tilebutton_clicker(mouse_pos_x,mouse_pos_y)

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