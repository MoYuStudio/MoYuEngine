
import moyu_engine.config.window as C

import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

class Window:

    def __init__(self):

        self.run = C.run
        self.icon = C.icon
        self.title = C.title
        self.size = C.size
        self.fps = C.fps
        self.clock = C.clock

    def set(self):

        pygame.init()
        pygame.display.init()
        pygame.mixer.init()

        if C.resizable == False:
            self.screen = pygame.display.set_mode(self.size)
        if C.resizable == True:
            self.screen = pygame.display.set_mode(self.size,pygame.RESIZABLE)

        self.screen_title = pygame.display.set_caption(self.title)
        self.icon = pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()

        pygame.display.flip()

        while self.run:

            self.blit()

            pygame.display.update()

            for self.event in pygame.event.get():

                if self.event.type == QUIT:
                    self.run = False

                # self.event()

        return self.screen

    def blit(self):
        pass

    def event(self):
        pass