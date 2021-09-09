
import sys
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F
import moyu_engine.config.sound as S

import moyu_engine.config.components.tilemap_manager
import moyu_engine.config.components.read_data

def event():

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            C.mouse_down_pos_x,C.mouse_down_pos_y = event.pos

            if pygame.Rect.collidepoint(C.menu_main_button01_rect,event.pos):
                S.button_sound.play()

                moyu_engine.config.components.tilemap_manager.tilemap_builder()

                C.menu_main = False
                C.game_main = True

            if pygame.Rect.collidepoint(C.menu_main_button02_rect,event.pos):
                S.button_sound.play()

                moyu_engine.config.components.read_data.read_tilemap()

                C.menu_main = False
                C.game_main = True

            if pygame.Rect.collidepoint(C.menu_main_button03_rect,event.pos):
                S.button_sound.play()

            if pygame.Rect.collidepoint(C.menu_main_button04_rect,event.pos):
                S.button_sound.play()

                pygame.quit()
                sys.exit()

            if pygame.Rect.collidepoint(C.menu_main_button05_rect,event.pos):
                S.button_sound.play()
