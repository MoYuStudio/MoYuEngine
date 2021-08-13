
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F

import components.tilemap_manager
import components.tilebutton
import components.window_move

import window.main.main_window

def run():
    init()
    gameloop()

def init():

    pygame.init()

    C.screen = pygame.display.set_mode((1200,600))
    C.screen_title = pygame.display.set_caption('TinyLand 弹丸之地')
    pygame.display.set_icon(G.tl6)
    C.clock = pygame.time.Clock()
    pygame.display.flip()

    return C.screen,C.screen_title,C.clock

def gameloop():

    components.tilemap_manager.tilemap_builder()

    while True:

        window.main.main_window.display()
        
        C.tile_size = 64*C.tile_level

        window.main.main_window.event()

        C.clock.tick(60)

run()