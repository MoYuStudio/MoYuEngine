
import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode([320,180])

while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()