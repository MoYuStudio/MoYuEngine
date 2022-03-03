
import moyu_engine.config.global_config as G

import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

class Window:

    def __init__(self):

        
        self.icon = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')
        self.title = 'MoYu Engine'

        self.run = True
        self.size = G.window_size
        self.fps = 60
        self.clock = None

        self.resizable = True

    def set(self):

        pygame.init()
        pygame.display.init()
        pygame.mixer.init()

        if self.resizable == False:
            self.screen = pygame.display.set_mode(self.size)
        if self.resizable == True:
            self.screen = pygame.display.set_mode(self.size,pygame.RESIZABLE)

        self.screen_title = pygame.display.set_caption(self.title)
        self.icon = pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()

        pygame.display.flip()

        while self.run:

            self.blit()

            pygame.display.update()

            for self.key_event in pygame.event.get():

                if self.key_event.type == QUIT:
                    self.run = False

                self.event()

        return self.screen,self.key_event

    def blit(self):
        pass

    def event(self):
        pass