
import pygame
import pygame.locals as pglocals

import config.system.setting as S

# def blit():
#     S.SCREEN.fill((255,0,0,255))

class BackgroundSurface:
    def __init__(self,color=(255,0,0,255)):
        self.surface = pygame.Surface(S.WINDOW_SIZE,flags=pglocals.SRCALPHA)
        self.surface.fill(color)
    
    def update(self,interval):
        return self.surface

    def accept(self,evt):
        return False