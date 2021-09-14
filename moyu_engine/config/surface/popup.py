
import pygame

import config

import system.setting as S
import system.assets as A

popup_surface_size       = S.WINDOW_SIZE
popup_surface            = pygame.Surface(popup_surface_size).convert_alpha()

def blit():

    popup_surface.fill((0,0,0,0))

    S.SCREEN.blit(popup_surface, (0, 0))
