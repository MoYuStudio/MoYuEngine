
import sys
import pygame
from pygame.locals import *

import data.constants as C

import system

class WindowsSystem:

    @ staticmethod
    def menu_main_surface():

        background_surface      = pygame.Surface(C.window['size']).convert_alpha()
        gui_surface             = pygame.Surface(C.window['size']).convert_alpha()

        background_surface.fill((0,0,0,0))
        background_surface.fill((255,0,0))

        gui_surface.fill((0,0,0,0))
        gui_surface.blit(C.assets['gui']['button'][1], (C.window['size'][0]-64*3*1 - 20, C.window['size'][1]-16*3*5 - 10*5))
        gui_surface.blit(C.assets['gui']['button'][1], (C.window['size'][0]-64*3*1 - 20, C.window['size'][1]-16*3*4 - 10*4))
        gui_surface.blit(C.assets['gui']['button'][1], (C.window['size'][0]-64*3*1 - 20, C.window['size'][1]-16*3*3 - 10*3))
        gui_surface.blit(C.assets['gui']['button'][1], (C.window['size'][0]-64*3*1 - 20, C.window['size'][1]-16*3*2 - 10*2))
        gui_surface.blit(C.assets['gui']['button'][1], (C.window['size'][0]-64*3*1 - 20, C.window['size'][1]-16*3*1 - 10*1))

        menu_main_surface = pygame.Surface(C.window['size']).convert_alpha()

        menu_main_surface.blit(background_surface, (0, 0))
        menu_main_surface.blit(gui_surface, (0, 0))
        
        C.screen.blit(menu_main_surface, (0, 0))