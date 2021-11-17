
import pygame
from pygame.locals import *

class Window:
    icon1 = pygame.image.load('moyu_engine/assets/graphics/tileland1.png').convert_alpha()
    def __init__(self,icon=icon1,title='MoYu Engine',size=[320,180],resizable=True):
        self.icon = icon
        self.title = title
        self.size = size
        self.resizable = resizable
    def set(self):
        if self.resizable == True:
            screen = pygame.display.set_mode(self.size,pygame.RESIZABLE)
        if self.resizable == False:
            screen = pygame.display.set_mode(self.size)
        screen_title = pygame.display.set_caption(self.title)
        icon = pygame.display.set_icon(self.icon)
        clock = pygame.time.Clock()

if __name__=="__main__":
    window = Window()
    window.set()