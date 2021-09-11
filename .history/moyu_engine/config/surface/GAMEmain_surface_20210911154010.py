
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

#FIXME 清洗代码

def update():

    gui_graphics()

    GAMEmain_gui_surfaceFin = pygame.transform.scale(C.GAMEmain_gui_surface,C.WINDOW_SIZE)
    
    C.SCREEN.blit(GAMEmain_gui_surfaceFin, (0, 0))

    #components.scrollbar.scrollbar_h_surface(C.SCREEN)

    moyu_engine.config.components.window_move.MOVE_Fn()
    moyu_engine.config.components.window_zoom.ZOOM_Fn()

def tilemap_graphics():

    C.GAMEmain_surface_size = [16*C.GAMEmain_surface_level,9*C.GAMEmain_surface_level]
    C.GAMEmain_surface = pygame.Surface(C.GAMEmain_surface_size)

    C.GAMEmain_surface.fill((0,0,0))
    C.GAMEmain_surface.blit(G.backgroundFin, ((-(C.MOVE[0]/3))-1280,(-(C.MOVE[1]/3))-720))

    moyu_engine.config.components.tilemap_manager.tilemap_loarder()

def gui_graphics():

    C.GAMEmain_gui_surface_size = [16*C.GAMEmain_gui_surface_level,9*C.GAMEmain_gui_surface_level]
    C.GAMEmain_gui_surface = pygame.Surface(C.GAMEmain_gui_surface_size)

    tilemap_graphics()
    C.surface_level = (1280/(16*C.GAMEmain_surface_level))

    C.GAMEmain_surfaceFin = pygame.transform.scale(C.GAMEmain_surface,C.WINDOW_SIZE)
    C.GAMEmain_gui_surface.blit(C.GAMEmain_surfaceFin, (0, 0))

    # === GUI ===

    C.GAMEmain_gui_surface.blit(G.button001Fin, (10,10*1 + 64*0))
    if C.pretile_type == 1:
        C.GAMEmain_gui_surface.blit(G.t1_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 2:
        C.GAMEmain_gui_surface.blit(G.t2_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 3:
        C.GAMEmain_gui_surface.blit(G.t3_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 4:
        C.GAMEmain_gui_surface.blit(G.t4_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 5:
        C.GAMEmain_gui_surface.blit(G.t5_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 105:
        C.GAMEmain_gui_surface.blit(G.t105_icon, (10*1 + 64*0 + 8,(10*1 + 64*0)))

    # === Bar button ===
    # = 1 =
    C.GAMEmain_gui_surface.blit(G.button001Fin, (10*1 + 64*0,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    C.GAMEmain_gui_surface.blit(G.t1_icon, (10*1 + 64*0 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))
    # = 2 =
    C.GAMEmain_gui_surface.blit(G.button001Fin, (10*2 + 64*1,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    C.GAMEmain_gui_surface.blit(G.t2_icon, (10*2 + 64*1 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))
    # = 3 =
    C.GAMEmain_gui_surface.blit(G.button001Fin, (10*3 + 64*2,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    C.GAMEmain_gui_surface.blit(G.t3_icon, (10*3 + 64*2 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))
    # = 4 =
    C.GAMEmain_gui_surface.blit(G.button001Fin, (10*4 + 64*3,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    C.GAMEmain_gui_surface.blit(G.t4_icon, (10*4 + 64*3 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))
    # = 5 =
    C.GAMEmain_gui_surface.blit(G.button001Fin, (10*5 + 64*4,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    C.GAMEmain_gui_surface.blit(G.t5_icon, (10*5 + 64*4 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))

    #C.GAMEmain_gui_surface.blit(G.button001Fin, (10,10*1 + 64*0))

    #C.GAMEmain_gui_surface.blit(G.button001miniFin, (100,10*1 + 48*0))

    C.GAMEmain_gui_surface.blit(G.home_buttonFin, (C.WINDOW_SIZE[0]-64 - 10,10))

    C.GAMEmain_gui_surface.blit(G.money_iconFin, (C.WINDOW_SIZE[0]-64*2 - 20 - 100, 10+16))

    money_text = F.font1.render(str(C.money), True, (255, 255, 255))
    C.GAMEmain_gui_surface.blit(money_text,(C.WINDOW_SIZE[0]-64*2 - 20 - 50, 10+16))