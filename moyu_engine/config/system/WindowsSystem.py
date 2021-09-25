
import sys
import pygame
from pygame.locals import *

class WindowsSystem:
    def __init__(self):
        self.window_size = [1280,720]

    @ staticmethod
    def menu_main_surface():
        menu_surface = pygame.Surface(self.window_size).convert_alpha()
        pygame.draw.rect(menu_surface,(255,255,255),(50,50,50,50))
        self.screen.blit(menu_surface, (0, 0))