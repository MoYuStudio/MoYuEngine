
import sys
import pygame
from pygame.locals import *

import system



while True:
    menu_window = system.WindowsSystem()

    background_surface = pygame.Surface((1280,720)).convert_alpha()
    background_surface.fill((0,255,0,255))
    a = pygame.transform.scale(background_surface, (1280,720))

    menu_window.background(a)

    menu_window.window_blit()
    menu_window.window_event()