
import sys

import pygame
from pygame.locals import *

import config.system.setting as S

class MainEvent:
    def __init__(self, surfManager):
        self.surf_manager = surfManager
    
    def distribute(self):
        for evt in pygame.event.get():

            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
            # distribute event here (from top to bottom)

            for surf in self.surf_manager.stack[::-1]:
                res = surf.accept(evt)
                if res:
                    # distribution abort
                    break

    def update_all(self, interval, screen): 
        # update surface manager
        self.surf_manager.update()

        # update all surface
        for surf in self.surf_manager:
            s = surf.update(interval)
            screen.blit(s,(0,0))
