
import moyu_engine.config.global_config as G

import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

screen = pygame.display.set_mode([320,180])

class Surface:

    def __init__(self):

        self.size = [1920,1080]
        self.transform_window = True

        self.window_size = G.window_size

        self.surface = pygame.Surface(self.size).convert_alpha()
        self.surface.fill((255,55,55,0))

    def blit(self,blit_surface):

        self.blit_surface = blit_surface

        if self.transform_window == True:
            self.surface = pygame.transform.scale(self.surface,self.window_size)
        if self.transform_window == False:
            pass

        self.blit_surface.blit(self.surface,(0,0))

        pygame.display.update()
        
if __name__ == '__main__':
    pass