
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F
import moyu_engine.config.sound as S

import moyu_engine.config.components.tilemap_manager

import moyu_engine.config.surface.menu_main_surface
import moyu_engine.config.event.menu_main_event

import moyu_engine.config.surface.game_main_surface
import moyu_engine.config.event.game_main_event

def run():
    init()
    gameloop()

def init():

    pygame.init()
    pygame.mixer.init()

    C.screen = pygame.display.set_mode(C.window_size)
    C.screen_title = pygame.display.set_caption('Tinyland 弹丸之地')
    pygame.display.set_icon(G.tl16)
    C.clock = pygame.time.Clock()
    pygame.display.flip()

    return C.screen,C.screen_title,C.clock

def gameloop():

    moyu_engine.config.components.tilemap_manager.tilemap_builder()

    pygame.mixer.music.load('moyu_engine/assets/music/Grace Behind the Curtain - Silent Partner.mp3')
    pygame.mixer.music.play(-1)

    while True: # 需要一个检测游戏是否运行的布尔值 使用for来优化

        if C.menu_main == True:

            moyu_engine.config.surface.menu_main_surface.update()

            moyu_engine.config.event.menu_main_event.event()

        if C.game_main == True:

            moyu_engine.config.surface.game_main_surface.update()

            moyu_engine.config.event.game_main_event.event()

        C.clock.tick(60)

run()