
import sys

import pygame
from pygame.locals import *

def event():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()