
import sys
import pygame
from pygame.locals import *

import data.constants as C

class TransitionSystem:

    @ staticmethod
    def fade_black():
        C.fade_black_surface.fill((0,0,0))
        C.SCREEN.blit(C.fade_black_surface, (0,0))

        if C.fade_black == True:
            if C.fade_black_alpha <= 0 :
                C.fade_black_alpha += 10
                C.fade_black_surface.set_alpha(C.fade_black_alpha)

        if C.fade_black_alpha >= 255:
            C.fade_black = False
            C.fade_black_alpha = 0
            C.window_switch = True