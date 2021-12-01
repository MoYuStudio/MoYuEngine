
import sys
import pygame
from pygame.locals import *

class Event:
    def __init__(self):
        pass
    def quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    pass
