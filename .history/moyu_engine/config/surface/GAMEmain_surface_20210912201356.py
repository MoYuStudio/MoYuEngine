
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

import moyu_engine.config.components.tilemap_manager
import moyu_engine.config.components.window_move
import moyu_engine.config.components.window_zoom

#FIXME Tilemap 移动bug

def blit(): 

    background()
    info()
    gui()
    popup()
    transition()

    background_surfaceFin = pygame.transform.scale(background_surface, C.WINDOW_SIZE)
    #info_surfaceFin       = pygame.transform.scale(C.tilemap_surface, C.WINDOW_SIZE)
    gui_surfaceFin        = pygame.transform.scale(gui_surface, C.WINDOW_SIZE)
    popup_surfaceFin      = pygame.transform.scale(popup_surface, C.WINDOW_SIZE)
    transition_surfaceFin = pygame.transform.scale(transition_surface, C.WINDOW_SIZE)

    C.SCREEN.blit(background_surfaceFin, (0, 0))
    C.SCREEN.blit(C.tilemap_surface, (0,0))
    C.SCREEN.blit(gui_surfaceFin, (0, 0))
    C.SCREEN.blit(popup_surfaceFin, (0, 0))
    C.SCREEN.blit(transition_surfaceFin, (0, 0))

def background(): 
    background_surface.fill((0,0,0,0))

    background_surface.blit(G.backgroundFin, ((-(C.MOVE[0]/3))-1280,(-(C.MOVE[1]/3))-720))

def info():   
    C.tilemap_surface_size = [16*C.tilemap_surface_level,9*C.tilemap_surface_level]
    C.tilemap_surface = pygame.Surface(C.tilemap_surface_size)

    C.surface_level = (1280/(16*C.GAMEmain_surface_level))

    C.tilemap_surface.fill((0,0,0,0))
    
    moyu_engine.config.components.tilemap_manager.tilemap_loarder()

def gui():
    gui_surface.fill((0,0,0,0))

    gui_surface.blit(G.button001Fin, (10,10*1 + 64*0))
    if C.pretile_type == 1:
        gui_surface.blit(G.t1_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 2:
        gui_surface.blit(G.t2_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 3:
        gui_surface.blit(G.t3_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 4:
        gui_surface.blit(G.t4_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 5:
        gui_surface.blit(G.t5_icon, (10*1 + 64*0 + 8,(10*1 + 64*0) + 24))
    if C.pretile_type == 105:
        gui_surface.blit(G.t105_icon, (10*1 + 64*0 + 8,(10*1 + 64*0)))

    # === Bar button ===

    # = 1 =
    gui_surface.blit(G.button001Fin, (10*1 + 64*0,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    gui_surface.blit(G.t1_icon, (10*1 + 64*0 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))
    # = 2 =
    gui_surface.blit(G.button001Fin, (10*2 + 64*1,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    gui_surface.blit(G.t2_icon, (10*2 + 64*1 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))
    # = 3 =
    gui_surface.blit(G.button001Fin, (10*3 + 64*2,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    gui_surface.blit(G.t3_icon, (10*3 + 64*2 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))
    # = 4 =
    gui_surface.blit(G.button001Fin, (10*4 + 64*3,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    gui_surface.blit(G.t4_icon, (10*4 + 64*3 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))
    # = 5 =
    gui_surface.blit(G.button001Fin, (10*5 + 64*4,C.WINDOW_SIZE[1] - (10*1 + 64*1)))
    gui_surface.blit(G.t5_icon, (10*5 + 64*4 + 8,C.WINDOW_SIZE[1] - (10*1 + 64*1) + 24))

    gui_surface.blit(G.home_buttonFin, (C.WINDOW_SIZE[0]-64 - 10,10))

    gui_surface.blit(G.money_iconFin, (C.WINDOW_SIZE[0]-64*2 - 20 - 100, 10+16))

    money_text = F.font1.render(str(C.money), True, (255, 255, 255))
    gui_surface.blit(money_text,(C.WINDOW_SIZE[0]-64*2 - 20 - 50, 10+16))

def popup():
    popup_surface.fill((0,0,0,0))

def transition():
    transition_surface.fill((0,0,0,0))

blit_surface_size       = C.WINDOW_SIZE
blit_surface            = pygame.Surface((blit_surface_size)).convert_alpha()
background_surface_size = C.WINDOW_SIZE
background_surface      = pygame.Surface((background_surface_size)).convert_alpha()
#C.tilemap_surface_size       = C.WINDOW_SIZE
#C.tilemap_surface            = pygame.Surface((C.tilemap_surface_size)).convert_alpha()
gui_surface_size        = C.WINDOW_SIZE
gui_surface             = pygame.Surface((gui_surface_size)).convert_alpha()
popup_surface_size      = C.WINDOW_SIZE
popup_surface           = pygame.Surface((popup_surface_size)).convert_alpha()
transition_surface_size = C.WINDOW_SIZE
transition_surface      = pygame.Surface((transition_surface_size)).convert_alpha()
