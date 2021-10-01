
import sys
import pygame
from pygame.locals import *

import data.constants as C

class TransitionSystem:

    alpha = 255

    @ staticmethod
    def fade_black():

        fade_black_surface = pygame.Surface(C.window['size']).convert_alpha()
        fade_black_surface.fill((0,0,0))

        if C.transition['fade_black'] == True:
            if TransitionSystem.alpha <= 0 :
                TransitionSystem.alpha += 10
                fade_black_surface.set_alpha(TransitionSystem.alpha)

        if TransitionSystem.alpha >= 255:
            C.transition['fade_black'] = False
            TransitionSystem.alpha = 0
            window_switch = True

        C.screen.blit(fade_black_surface, (0,0))