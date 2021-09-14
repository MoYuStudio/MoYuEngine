
import pygame
import pygame.locals as pglocals

import config

import system.setting as S
import system.assets as A

class BackgroundSurface:
    def __init__(self,alpha_color=(0,0,0,0)):
        self.surface_size = S.WINDOW_SIZE
        self.surface = pygame.Surface(S.WINDOW_SIZE,flags=pglocals.SRCALPHA).convert_alpha()
        self.surface.fill(alpha_color)
    
    def update(self,interval):
        self.surface.blit(A.menu_backgroundFin, (0,0))
        return self.surface

    def accept(self,evt):
        return False
