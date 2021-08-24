
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F

import components.tilemap_manager
import components.window_move
import components.window_zoom
import components.scrollbar

def update():

    graphics()

    game_main_surfaceFin = pygame.transform.scale(C.game_main_surface,C.window_size)
    
    C.screen.blit(game_main_surfaceFin, (0, 0))

    components.scrollbar.scrollbar_h_surface(C.screen)

    components.window_move.move_Fn()
    components.window_zoom.zoom_Fn()

    pygame.display.update()

    C.surface_level = (1280/(16*C.game_main_surface_level))

def graphics():

    C.game_main_surface_size = [16*C.game_main_surface_level,9*C.game_main_surface_level]
    C.game_main_surface = pygame.Surface(C.game_main_surface_size)

    C.game_main_surface.fill((0,0,0))
    C.game_main_surface.blit(G.backgroundFin, ((-(C.move_x/3))-1280,(-(C.move_y/3))-720))

    components.tilemap_manager.tilemap_loarder()

def font():

    F.font1 = pygame.font.Font('moyu_engine/assets/font/方正像素16.TTF', 10)
