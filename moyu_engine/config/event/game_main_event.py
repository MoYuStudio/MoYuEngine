
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F

import components.tilemap_manager
import components.tilebutton
import components.window_move
import components.scrollbar

def event():

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:

            C.mouse_pos_x,C.mouse_pos_y = event.pos

            components.scrollbar.scrollbar_h_event_MOUSEMOTION(C.scrollbar_move,C.scrollbar_moveable)

        if event.type == pygame.MOUSEBUTTONDOWN:

            C.mouse_down_pos_x,C.mouse_down_pos_y = event.pos

            print(C.mouse_down_pos_x,C.mouse_down_pos_y )
            
            components.tilebutton.tilebutton_clicker(C.mouse_down_pos_x,C.mouse_down_pos_y)

            components.scrollbar.scrollbar_h_event_MOUSEBUTTONDOWN(C.scrollbar_button_event_pos,C.scrollbar_button_event_size,C.scrollbar_move,C.scrollbar_moveable)

        if event.type == pygame.MOUSEBUTTONUP:
            
            components.scrollbar.scrollbar_h_event_MOUSEBUTTONUP(C.scrollbar_moveable)

        if event.type == MOUSEWHEEL:
            
            components.scrollbar.scrollbar_h_event_MOUSEWHEEL(C.scrollbar_move,event)

        if event.type == pygame.KEYDOWN:

            if event.key == K_UP or event.key == K_w:
                C.move_up = True
                
            if event.key == K_DOWN or event.key == K_s:
                C.move_down = True

            if event.key == K_LEFT or event.key == K_a:
                C.move_left = True

            if event.key == K_RIGHT or event.key == K_d:
                C.move_right = True

            if event.key == K_q:
                #C.tile_level += 1
                C.move_speed += 2

            if event.key == K_e:
                if C.tile_level == 1:
                    C.tile_level = 1
                else:
                    C.tile_level -= 1
                    C.move_speed -= 2

            if event.key == K_z:
                C.tile_level = 1
                C.move_speed = 5
                C.move_x,C.move_y = 19*30,3*30

            if event.key == K_x:
                components.tilemap_manager.tilemap_builder()

        if event.type == pygame.KEYUP:

            if event.key == K_UP or event.key == K_w:
                C.move_up = False

            if event.key == K_DOWN or event.key == K_s:
                C.move_down = False

            if event.key == K_LEFT or event.key == K_a:
                C.move_left = False

            if event.key == K_RIGHT or event.key == K_d:
                C.move_right = False
