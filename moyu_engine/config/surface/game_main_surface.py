
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

def update():
    graphics()

    game_main_surfaceFin = pygame.transform.scale(C.game_main_surface, C.window_size)
    
    C.screen.blit(game_main_surfaceFin, (0, 0))

    components.window_move.move_Fn()

    components.tilebutton.tile_preview(C.tile_choose_info) 

    pygame.display.update()

def graphics():
    C.game_main_surface.blit(G.backgroundFin, ((-(C.move_x/3))-1280,(-(C.move_y/3))-720))
    #C.tilemap_surface.fill((0,0,0))
    components.tilemap_manager.tilemap_loarder()

    components.scrollbar.scrollbar_h_display(C.game_main_surface,(255,0,0),(10,10),(3,30),(0,255,0),(10,10+C.scrollbar_move),(5,3),line_width=0,button_width=0)

def font():

    F.font1 = pygame.font.Font('moyu_engine/assets/font/方正像素16.TTF', 10)
