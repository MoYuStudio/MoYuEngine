
import pygame

import config

import system.setting as S
import system.assets as A

map_surface_size       = S.WINDOW_SIZE
map_surface            = pygame.Surface(map_surface_size).convert_alpha()

def blit():

    map_surface.fill((0,0,0,0))

    S.SCREEN.blit(map_surface, (0, 0))
