
import pygame
from pygame.locals import *

import data.constants as C

class PopupSystem():

    def save_success():

        surface = pygame.Surface(C.window['size']).convert_alpha()
        surface.fill((0,0,0,0))

        surface.blit(C.assets['button'][-1], (0,0))

        C.screen.blit(surface, (0,0))