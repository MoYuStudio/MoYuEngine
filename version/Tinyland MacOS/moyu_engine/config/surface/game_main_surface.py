
import sys
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

import moyu_engine.config.components.tilemap_manager
import moyu_engine.config.components.window_move
import moyu_engine.config.components.window_zoom
import moyu_engine.config.components.scrollbar

def update():

    gui_graphics()

    game_main_gui_surfaceFin = pygame.transform.scale(C.game_main_gui_surface,C.window_size)
    
    C.screen.blit(game_main_gui_surfaceFin, (0, 0))

    #components.scrollbar.scrollbar_h_surface(C.screen)

    moyu_engine.config.components.window_move.move_Fn()
    moyu_engine.config.components.window_zoom.zoom_Fn()

    pygame.display.update()

def tilemap_graphics():

    C.game_main_surface_size = [16*C.game_main_surface_level,9*C.game_main_surface_level]
    C.game_main_surface = pygame.Surface(C.game_main_surface_size)

    C.game_main_surface.fill((0,0,0))
    C.game_main_surface.blit(G.backgroundFin, ((-(C.move_x/3))-1280,(-(C.move_y/3))-720))

    moyu_engine.config.components.tilemap_manager.tilemap_loarder()

def gui_graphics():

    C.game_main_gui_surface_size = [16*C.game_main_gui_surface_level,9*C.game_main_gui_surface_level]
    C.game_main_gui_surface = pygame.Surface(C.game_main_gui_surface_size)

    tilemap_graphics()
    C.surface_level = (1280/(16*C.game_main_surface_level))

    C.game_main_surfaceFin = pygame.transform.scale(C.game_main_surface,C.window_size)
    C.game_main_gui_surface.blit(C.game_main_surfaceFin, (0, 0))

    # === GUI ===

    C.game_main_gui_surface.blit(G.button001Fin, (10,10*1 + 64*0))
    if C.pretile_type == 1:
        C.game_main_gui_surface.blit(G.t1_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 2:
        C.game_main_gui_surface.blit(G.t2_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 3:
        C.game_main_gui_surface.blit(G.t3_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 4:
        C.game_main_gui_surface.blit(G.t4_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 5:
        C.game_main_gui_surface.blit(G.t5_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 105:
        C.game_main_gui_surface.blit(G.t105_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 18))

    # === Bar button ===
    # = 1 =
    C.game_main_gui_surface.blit(G.button001Fin, (10*1 + 64*0,C.window_size[1] - (10*1 + 64*1)))
    C.game_main_gui_surface.blit(G.t1_icon, (10*1 + 64*0 + 8,C.window_size[1] - (10*1 + 64*1) + 24))
    # = 2 =
    C.game_main_gui_surface.blit(G.button001Fin, (10*2 + 64*1,C.window_size[1] - (10*1 + 64*1)))
    C.game_main_gui_surface.blit(G.t2_icon, (10*2 + 64*1 + 8,C.window_size[1] - (10*1 + 64*1) + 24))
    # = 3 =
    C.game_main_gui_surface.blit(G.button001Fin, (10*3 + 64*2,C.window_size[1] - (10*1 + 64*1)))
    C.game_main_gui_surface.blit(G.t3_icon, (10*3 + 64*2 + 8,C.window_size[1] - (10*1 + 64*1) + 24))
    # = 4 =
    C.game_main_gui_surface.blit(G.button001Fin, (10*4 + 64*3,C.window_size[1] - (10*1 + 64*1)))
    C.game_main_gui_surface.blit(G.t4_icon, (10*4 + 64*3 + 8,C.window_size[1] - (10*1 + 64*1) + 24))
    # = 5 =
    C.game_main_gui_surface.blit(G.button001Fin, (10*5 + 64*4,C.window_size[1] - (10*1 + 64*1)))
    C.game_main_gui_surface.blit(G.t5_icon, (10*5 + 64*4 + 8,C.window_size[1] - (10*1 + 64*1) + 24))

    #C.game_main_gui_surface.blit(G.button001Fin, (10,10*1 + 64*0))

    #C.game_main_gui_surface.blit(G.button001miniFin, (100,10*1 + 48*0))

    C.game_main_gui_surface.blit(G.home_buttonFin, (C.window_size[0]-64 - 10,10))

    C.game_main_gui_surface.blit(G.money_iconFin, (C.window_size[0]-64*2 - 20 - 100, 10+16))

    money_text = F.font1.render(str(C.money), True, (255, 255, 255))
    C.game_main_gui_surface.blit(money_text,(C.window_size[0]-64*2 - 20 - 50, 10+16))