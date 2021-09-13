
import pygame

import config

import system.setting as S
import system.assets as A

transition_surface_size       = S.WINDOW_SIZE
transition_surface            = pygame.Surface(transition_surface_size).convert_alpha()

def blit():

    transition_surface.fill((0,0,0,0))

    S.SCREEN.blit(transition_surface, (0, 0))
    