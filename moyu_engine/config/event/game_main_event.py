
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F
import sound as S

import components.tilemap_manager
import components.tilemap_button
import components.button
import components.scrollbar

def event():

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:

            C.mouse_pos_x,C.mouse_pos_y = event.pos

            components.scrollbar.scrollbar_h_event_MOUSEMOTION()

        if event.type == pygame.MOUSEBUTTONDOWN:

            C.mouse_down_pos_x,C.mouse_down_pos_y = event.pos
            
            components.tilemap_button.tilebutton_clicker_event_MOUSEBUTTONDOWN()

            components.scrollbar.scrollbar_h_event_MOUSEBUTTONDOWN()

            if pygame.Rect.collidepoint(C.bar_button01_rect,event.pos):
                S.button_sound.play()
                C.pretile_type = 1
                C.tile_type = 1

            if pygame.Rect.collidepoint(C.bar_button02_rect,event.pos):
                S.button_sound.play()
                C.pretile_type = 2
                C.tile_type = 2

            if pygame.Rect.collidepoint(C.bar_button03_rect,event.pos):
                S.button_sound.play()
                C.pretile_type = 3
                C.tile_type = 3

            if pygame.Rect.collidepoint(C.bar_button04_rect,event.pos):
                S.button_sound.play()
                C.pretile_type = 4
                C.tile_type = 4

            if pygame.Rect.collidepoint(C.bar_button05_rect,event.pos):
                S.button_sound.play()
                C.pretile_type = 5
                C.tile_type = 5

        if event.type == pygame.MOUSEBUTTONUP:
            
            components.scrollbar.scrollbar_h_event_MOUSEBUTTONUP()

        if event.type == MOUSEWHEEL:

            mousewheel = event.y
            
            components.scrollbar.scrollbar_h_event_MOUSEWHEEL(event)

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
                C.zoom_in = True

            if event.key == K_e:
                C.zoom_out = True

            if event.key == K_b:
                C.build = True
                if C.tile_type == 1:
                    C.money -= 30
                if C.tile_type == 2:
                    C.money -= 5

            if event.key == K_r:
                C.reward = True

            if event.key == K_z:
                C.game_main_surface_level = 60
                C.move_speed = 5
                C.move_x,C.move_y = 450,5

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

            if event.key == K_q:
                C.zoom_in = False

            if event.key == K_e:
                C.zoom_out = False

            if event.key == K_b:
                C.build = False

            if event.key == K_r:
                C.reward = False
