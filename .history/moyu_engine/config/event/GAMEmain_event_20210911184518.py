
import sys
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F
import moyu_engine.config.sound as S

import moyu_engine.config.components.tilemap_manager
import moyu_engine.config.components.tilemap_button
import moyu_engine.config.components.button
import moyu_engine.config.components.scrollbar
import moyu_engine.config.components.save_data
import moyu_engine.config.components.read_data

def event(): 

    for event in pygame.event.get(): 
        if  event.type == QUIT: 
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEMOTION:

            C.mouse_pos_x,C.mouse_pos_y = event.pos

            moyu_engine.config.components.scrollbar.scrollbar_h_event_MOUSEMOTION()

        if event.type == pygame.MOUSEBUTTONDOWN:

            C.mouse_down_pos_x,C.mouse_down_pos_y = event.pos
            
            moyu_engine.config.components.tilemap_button.tilebutton_clicker_event_MOUSEBUTTONDOWN()

            moyu_engine.config.components.scrollbar.scrollbar_h_event_MOUSEBUTTONDOWN()

            if pygame.Rect.collidepoint(C.homebutton_RECT,event.pos): 
                S.button_sound.play()
                
                C.GAMEmain = False
                C.MENUmain = True

            if pygame.Rect.collidepoint(C.GAMEbar_button01_RECT,event.pos): 
                S.button_sound.play()
                C.pretile_type = 1
                C.tile_type    = 1

            if pygame.Rect.collidepoint(C.GAMEbar_button02_RECT,event.pos): 
                S.button_sound.play()
                C.pretile_type = 2
                C.tile_type    = 2

            if pygame.Rect.collidepoint(C.GAMEbar_button03_RECT,event.pos): 
                S.button_sound.play()
                C.pretile_type = 3
                C.tile_type    = 3

            if pygame.Rect.collidepoint(C.GAMEbar_button04_RECT,event.pos): 
                S.button_sound.play()
                C.pretile_type = 4
                C.tile_type    = 4

            if pygame.Rect.collidepoint(C.GAMEbar_button05_RECT,event.pos): 
                S.button_sound.play()
                C.pretile_type = 5
                C.tile_type    = 5

        if event.type == pygame.MOUSEBUTTONUP:
            
            moyu_engine.config.components.scrollbar.scrollbar_h_event_MOUSEBUTTONUP()

        if event.type == MOUSEWHEEL:

            mousewheel = event.y
            
            moyu_engine.config.components.scrollbar.scrollbar_h_event_MOUSEWHEEL(event)

        if event.type == pygame.KEYDOWN:

            if event.key == K_UP or event.key == K_w:
               C.MOVE_UP   = True
                
            if event.key == K_DOWN or event.key == K_s:
               C.MOVE_DOWN = True

            if event.key == K_LEFT or event.key == K_a:
               C.MOVE_LEFT = True

            if event.key == K_RIGHT or event.key == K_d:
               C.MOVE_RIGHT = True

            if event.key == K_q:
               C.ZOOM_IN   = True

            if event.key == K_e:
               C.ZOOM_OUT  = True

            if event.key == K_b:
               C.build        = True
            if C.tile_type == 1:
               C.money       -= 30
            if C.tile_type == 2:
               C.money       -= 5

            if event.key == K_r:
               C.reward    = True

            if event.key == K_z:
               C.GAMEmain_surface_level = 60
               C.MOVE_SPEED             = 10
               C.MOVE                   = [450,5]

            if event.key == K_x:
                moyu_engine.config.components.tilemap_manager.tilemap_builder()

            if event.key == K_m:
                moyu_engine.config.components.save_data.save_tilemap()
            
            if event.key == K_n:
                moyu_engine.config.components.read_data.read_tilemap()

        if event.type == pygame.KEYUP:

            if event.key == K_UP or event.key == K_w:
               C.MOVE_UP   = False

            if event.key == K_DOWN or event.key == K_s:
               C.MOVE_DOWN = False

            if event.key == K_LEFT or event.key == K_a:
               C.MOVE_LEFT = False

            if event.key == K_RIGHT or event.key == K_d:
               C.MOVE_RIGHT = False

            if event.key == K_q:
               C.ZOOM_IN   = False

            if event.key == K_e:
               C.ZOOM_OUT  = False

            if event.key == K_b:
               C.build     = False

            if event.key == K_r:
               C.reward    = False
