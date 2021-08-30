
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

    gui_graphics()

    game_main_gui_surfaceFin = pygame.transform.scale(C.game_main_gui_surface,C.window_size)
    
    C.screen.blit(game_main_gui_surfaceFin, (0, 0))

    components.scrollbar.scrollbar_h_surface(C.screen)

    components.window_move.move_Fn()
    components.window_zoom.zoom_Fn()

    pygame.display.update()

def tilemap_graphics():

    C.game_main_surface_size = [16*C.game_main_surface_level,9*C.game_main_surface_level]
    C.game_main_surface = pygame.Surface(C.game_main_surface_size)

    C.game_main_surface.fill((0,0,0))
    C.game_main_surface.blit(G.backgroundFin, ((-(C.move_x/3))-1280,(-(C.move_y/3))-720))

    components.tilemap_manager.tilemap_loarder()

def gui_graphics():

    C.game_main_gui_surface_size = [16*C.game_main_gui_surface_level,9*C.game_main_gui_surface_level]
    C.game_main_gui_surface = pygame.Surface(C.game_main_gui_surface_size)

    tilemap_graphics()
    C.surface_level = (1280/(16*C.game_main_surface_level))

    C.game_main_surfaceFin = pygame.transform.scale(C.game_main_surface,C.window_size)
    C.game_main_gui_surface.blit(C.game_main_surfaceFin, (0, 0))

    # === GUI ===

    C.game_main_gui_surface.blit(G.button001Fin, (10,10*1 + 64*0))
    C.game_main_gui_surface.blit(G.button001Fin, (10,10*2 + 64*1))
    C.game_main_gui_surface.blit(G.button001Fin, (10,10*3 + 64*2))
    C.game_main_gui_surface.blit(G.button001Fin, (10,10*4 + 64*3))
    C.game_main_gui_surface.blit(G.button001Fin, (10,10*5 + 64*4))

    C.game_main_gui_surface.blit(G.button001miniFin, (100,10*1 + 48*0))
    C.game_main_gui_surface.blit(G.button001miniFin, (100,10*2 + 48*1))
    C.game_main_gui_surface.blit(G.button001miniFin, (100,10*3 + 48*2))
    C.game_main_gui_surface.blit(G.button001miniFin, (100,10*4 + 48*3))
    C.game_main_gui_surface.blit(G.button001miniFin, (100,10*5 + 48*4))
    C.game_main_gui_surface.blit(G.button001miniFin, (100,10*6 + 48*5))

    C.game_main_gui_surface.blit(G.home_buttonFin, (C.window_size[0]-64 - 10,10))

    C.game_main_gui_surface.blit(G.money_iconFin, (C.window_size[0]-64*2 - 20 - 100, 10+16))

    money_text = F.font1.render(str(C.money), True, (255, 255, 255))
    C.game_main_gui_surface.blit(money_text,(C.window_size[0]-64*2 - 20 - 50, 10+16))