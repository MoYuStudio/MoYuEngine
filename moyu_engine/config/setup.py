
import sys
import pygame
from pygame.locals import *

import system



while True:

    menu_window = system.WindowsSystem()

    a = pygame.Surface((menu_window.window_size)).convert_alpha()
    a.fill((0,255,0,255))
    a = pygame.transform.scale(a, (menu_window.window_size))

    #menu_window.background(a)

    menu_window.window_blit(a)
    menu_window.window_event()