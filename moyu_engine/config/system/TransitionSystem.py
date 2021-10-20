
import sys
import pygame
from pygame.locals import *

import data.constants as C

class TransitionSystem:

    alpha = 0

    @ staticmethod
    def fade_black():

        surface = pygame.Surface(C.window['size']).convert_alpha()
        surface.fill((0,0,0,0))

        if C.transition['fade_black'] == True:
            if TransitionSystem.alpha <= 0 :
                TransitionSystem.alpha += 10
                surface.set_alpha(TransitionSystem.alpha)

        if TransitionSystem.alpha >= 255:
            C.transition['fade_black'] = False
            TransitionSystem.alpha = 0
            C.window['page_switch']['switch'] = True

        C.screen.blit(surface, (0,0))