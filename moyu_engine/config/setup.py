
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F
import sound as S

import components.tilemap_manager

import surface.game_main_surface

import event.game_main_event

def run():
    init()
    gameloop()

def init():

    pygame.init()
    pygame.mixer.init()

    C.screen = pygame.display.set_mode(C.window_size)
    C.screen_title = pygame.display.set_caption('Not Enough Space ! 空间不足！ ')
    pygame.display.set_icon(G.tl16)
    C.clock = pygame.time.Clock()
    pygame.display.flip()

    return C.screen,C.screen_title,C.clock

def gameloop():

    components.tilemap_manager.tilemap_builder()

    pygame.mixer.music.load('moyu_engine/assets/music/Grace Behind the Curtain - Silent Partner.mp3')
    pygame.mixer.music.play(-1)

    while True: # 需要一个检测游戏是否运行的布尔值 使用for来优化

        surface.game_main_surface.update()

        event.game_main_event.event()

        C.clock.tick(60)

run()