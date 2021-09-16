
import sys

import pygame
from pygame.locals import *

import config.system.setting as S

class MainEvent:
    def __init__(self, initial_stack=[]):
        self.surf_stack = initial_stack
    
    def distribute(self):
        for evt in pygame.event.get():

            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
            # distribute event here (from top to bottom)

            for surf in self.surf_stack[::-1]:
                res = surf.accept(evt)
                if res:
                    # distribution abort
                    break

    def update_all(self, interval, screen): 
        # update all surface
        for surf in self.surf_stack:
            s = surf.update(interval)
            screen.blit(s,(0,0))
