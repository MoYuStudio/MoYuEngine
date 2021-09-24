
import sys
import pygame
from pygame.locals import *

class System:
    # __slots__ = []

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        pygame.display.set_caption('Tinyland 弹丸之地')
        # pygame.display.set_icon(A.tl6)
        pygame.display.flip()


    
