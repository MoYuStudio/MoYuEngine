
import sys
import pygame
from pygame.locals import *

import system



while True:
    menu_window = system.WindowsSystem()

    background_surface = pygame.Surface((1280,720)).convert_alpha()
    background_surface.fill((0,0,255,255))

    menu_window.background(background_surface)

    menu_window.window_blit()
    menu_window.window_event()