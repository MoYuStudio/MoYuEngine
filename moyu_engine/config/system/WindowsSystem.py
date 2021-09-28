
import sys
import pygame
from pygame.locals import *

import data.constants as C

import system

class WindowsSystem:

    @ staticmethod
    def menu_main_surface():

        background_surface      = pygame.Surface(C.window['size']).convert_alpha()
        gui_surface             = pygame.Surface(C.window['size']).convert_alpha()

        background_surface.fill((255,55,55,0))
        background_surface.blit(C.assets['background'][0], (0,0))

        gui_surface.fill((255,55,55,0))

        # button_text = (
        #     A.font1.render('新游戏', True, (255, 255, 255)),
        #     A.font1.render('继续', True, (255, 255, 255)),
        #     A.font1.render('设置', True, (255, 255, 255)),
        #     A.font1.render('退出', True, (255, 255, 255)),
        #     A.font1.render('关于', True, (255, 255, 255))
        # )

        for num in range(6):
            gui_surface.blit(C.assets['gui']['button'][0], (C.window['size'][0]-64*3*1 - 20, C.window['size'][1]-16*3*num - 10*num))

        menu_main_surface = pygame.Surface(C.window['size']).convert_alpha()

        menu_main_surface.blit(background_surface, (0, 0))
        menu_main_surface.blit(gui_surface, (0, 0))
        
        C.screen.blit(menu_main_surface, (0, 0))

    @ staticmethod
    def game_main_surface():

        background_surface      = pygame.Surface(C.window['size']).convert_alpha()
        info_surface             = pygame.Surface(C.window['size']).convert_alpha()
        gui_surface             = pygame.Surface(C.window['size']).convert_alpha()

        background_surface.fill((255,55,55,0))
        background_surface.blit(C.assets['background'][0], (0,0))

        info_surface.fill((255,55,55,0))

        gui_surface.fill((255,55,55,0))

        for num in range(6):
            gui_surface.blit(C.assets['gui']['button'][0], (C.window['size'][0]-64*3*1 - 20, C.window['size'][1]-16*3*num - 10*num))

        game_main_surface = pygame.Surface(C.window['size']).convert_alpha()

        game_main_surface.blit(background_surface, (0, 0))
        game_main_surface.blit(gui_surface, (0, 0))
        
        C.screen.blit(game_main_surface, (0, 0))
