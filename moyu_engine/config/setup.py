
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F

import components.tilemap_manager
import components.tilebutton
import components.window_move

import surface.main_window

def run():
    init()
    gameloop()

def init():

    pygame.init()

    C.screen = pygame.display.set_mode(C.window_size)
    C.screen_title = pygame.display.set_caption('TinyLand 弹丸之地')
    pygame.display.set_icon(G.tl6)
    C.clock = pygame.time.Clock()
    pygame.display.flip()

    return C.screen,C.screen_title,C.clock

def gameloop():

    components.tilemap_manager.tilemap_builder()

    while True:

        surface.main_window.display()

        surface.main_window.event()

        C.clock.tick(60)

run()