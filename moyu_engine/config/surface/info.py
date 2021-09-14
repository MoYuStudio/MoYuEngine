
import pygame

import config

import system.setting as S
import system.assets as A

info_surface_size       = S.WINDOW_SIZE
info_surface            = pygame.Surface(info_surface_size).convert_alpha()

def blit():

    info_surface.fill((0,0,0,0))

    S.SCREEN.blit(info_surface, (0, 0))
