
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

def update():
    menu_graphics()

    menu_main_surfaceFin = pygame.transform.scale(C.menu_main_surface,C.window_size)
    
    C.screen.blit(menu_main_surfaceFin, (0, 0))

    pygame.display.update()

def menu_graphics():
    C.menu_main_surface_size = [16*C.menu_main_surface_level,9*C.menu_main_surface_level]
    C.menu_main_surface = pygame.Surface(C.menu_main_surface_size)

    C.menu_main_surface.fill((255,255,255))

    C.menu_main_surface.blit(G.menu_backgroundFin, (0,0))

    C.menu_main_surface.blit(G.button001Fin, (10*1 + 64*0,C.window_size[1] - (10*1 + 64*1)))
