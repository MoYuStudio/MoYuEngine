
import sys
import pygame
from pygame.locals import *

import data.constants as C

import system

class WindowsSystem:

    @ staticmethod
    def menu_main_surface():
        menu_surface = pygame.Surface(C.window['size']).convert_alpha()
        pygame.draw.rect(menu_surface,(255,255,255),(50,50,50,50))
        C.screen.blit(menu_surface, (0, 0))