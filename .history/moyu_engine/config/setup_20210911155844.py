
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F
import moyu_engine.config.sound as S

import moyu_engine.config.components.tilemap_manager

import moyu_engine.config.surface.MENUmain_surface
import moyu_engine.config.event.MENUmain_event

import moyu_engine.config.surface.GAMEmain_surface
import moyu_engine.config.event.GAMEmain_event

def run(): 
    init()
    gameloop()

def init(): 

    pygame.init()
    pygame.mixer.init()

    C.SCREEN       = pygame.display.set_mode(C.WINDOW_SIZE)
    C.SCREEN_TITLE = pygame.display.set_caption('Tinyland 弹丸之地')
    pygame.display.set_icon(G.tl16)
    C.CLOCK = pygame.time.Clock()
    pygame.display.flip()

    return C.SCREEN,C.SCREEN_TITLE,C.CLOCK

def gameloop(): 

    moyu_engine.config.components.tilemap_manager.tilemap_builder()

    #pygame.mixer.music.load('moyu_engine/assets/music/Grace Behind the Curtain - Silent Partner.mp3')
    #pygame.mixer.music.play(-1)

    while True: #TODO 需要一个检测游戏是否运行的布尔值 使用for来优化

        if C.MENUmain = = True:

            moyu_engine.config.surface.MENUmain_surface.blit()

            moyu_engine.config.event.MENUmain_event.event()

        if C.GAMEmain = = True:

            moyu_engine.config.surface.GAMEmain_surface.update()

            moyu_engine.config.event.GAMEmain_event.event()

        pygame.display.update()
        C.CLOCK.tick(60)

run()