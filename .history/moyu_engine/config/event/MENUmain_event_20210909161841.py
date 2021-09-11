
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

            if pygame.Rect.collidepoint(C.MENUmain_button01_RECT,event.pos):
                S.button_sound.play()

                moyu_engine.config.components.tilemap_manager.tilemap_builder()

                C.fade_black = True
                C.buttonStartGame = True

            if pygame.Rect.collidepoint(C.MENUmain_button02_RECT,event.pos):
                S.button_sound.play()

                moyu_engine.config.components.read_data.read_tilemap()

                C.MENUmain = False
                C.GAMEmain = True

            if pygame.Rect.collidepoint(C.MENUmain_button03_RECT,event.pos):
                S.button_sound.play()

            if pygame.Rect.collidepoint(C.MENUmain_button04_RECT,event.pos):
                S.button_sound.play()

                pygame.quit()
                sys.exit()

            if pygame.Rect.collidepoint(C.MENUmain_button05_RECT,event.pos):
                S.button_sound.play()
