
import pygame

import config

import system.setting as S
import system.assets as A

background_surface_size = S.WINDOW_SIZE
background_surface      = pygame.Surface(background_surface_size).convert_alpha()

def blit():

    background_surface.fill((0,0,0,0))
    background_surface.blit(A.menu_backgroundFin, (0, 0))

    S.SCREEN.blit(background_surface, (0, 0))
