
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

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
    pass

def info(): 
    pass

def gui(): 
    pass

def popup(): 
    pass

def transition(): 
    pass

blit_surface_size       = C.WINDOW_SIZE
blit_surface            = pygame.Surface(blit_surface_size).convert_alpha()
background_surface_size = C.WINDOW_SIZE
background_surface      = pygame.Surface(background_surface_size).convert_alpha()
info_surface_size       = C.WINDOW_SIZE
info_surface            = pygame.Surface(info_surface_size).convert_alpha()
gui_surface_size        = C.WINDOW_SIZE
gui_surface             = pygame.Surface(gui_surface_size).convert_alpha()
popup_surface_size      = C.WINDOW_SIZE
popup_surface           = pygame.Surface(popup_surface_size).convert_alpha()
transition_surface_size = C.WINDOW_SIZE
transition_surface      = pygame.Surface(transition_surface_size).convert_alpha()