
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F

import components.tilemap_manager

def graphics():
    C.tilemap_surface.blit(G.backgroundFin, ((-(C.move_x/3))-1280,(-(C.move_y/3))-720))
    #C.tilemap_surface.fill((0,0,0))
    components.tilemap_manager.tilemap_loarder()