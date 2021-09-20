
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

import moyu_engine.config.components.tilemap_manager

def blit(): 

    background()
    info_surface.blit(background_surface, (0, 0))
    info()
    gui_surface.blit(info_surface, (0, 0))
    gui()
    popup_surface.blit(gui_surface, (0, 0))
    popup()
    transition_surface.blit(popup_surface, (0, 0))
    transition()
    blit_surface.blit(transition_surface, (0, 0))

    C.SCREEN.blit(blit_surface, (0, 0))

def background(): 

    background_surface.fill((0,0,0))
    background_surface.blit(G.backgroundFin, ((-(C.MOVE[0]/3))-1280,(-(C.MOVE[1]/3))-720))

def info(): 
    C.GAMEmain_gui_surface_size = [16*C.GAMEmain_gui_surface_level,9*C.GAMEmain_gui_surface_level]
    C.GAMEmain_gui_surface = pygame.Surface(C.GAMEmain_gui_surface_size)

    moyu_engine.config.components.tilemap_manager.tilemap_loarder()
    C.surface_level = (1280/(16*C.GAMEmain_surface_level))

def gui(): 
    pass

def popup(): 
    pass

def transition(): 
    pass

blit_surface_size       = C.WINDOW_SIZE
blit_surface            = pygame.Surface(blit_surface_size)
background_surface_size = C.WINDOW_SIZE
background_surface      = pygame.Surface(background_surface_size)
info_surface_size       = C.WINDOW_SIZE
info_surface            = pygame.Surface(info_surface_size)
gui_surface_size        = C.WINDOW_SIZE
gui_surface             = pygame.Surface(gui_surface_size)
popup_surface_size      = C.WINDOW_SIZE
popup_surface           = pygame.Surface(popup_surface_size)
transition_surface_size = C.WINDOW_SIZE
transition_surface      = pygame.Surface(transition_surface_size)