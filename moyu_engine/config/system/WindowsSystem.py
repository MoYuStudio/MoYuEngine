
import sys
import pygame
from pygame.locals import *

import data.constants as C

import system

class WindowsSystem:

    @ staticmethod
    def menu_main_surface():

        button_rect = []

        background_surface = pygame.Surface(C.window['size']).convert_alpha()
        gui_surface        = pygame.Surface(C.window['size']).convert_alpha()

        background_surface.fill((255,55,55,0))
        background_surface.blit(C.assets['background'][-1], (0,0))

        gui_surface.fill((255,55,55,0))

        button_text =\
        (
            C.assets['zh'][-1].render('新游戏', True, (255, 255, 255)),
            C.assets['zh'][-1].render('继续', True, (255, 255, 255)),
            C.assets['zh'][-1].render('设置', True, (255, 255, 255)),
            C.assets['zh'][-1].render('退出', True, (255, 255, 255)),
            C.assets['zh'][-1].render('关于', True, (255, 255, 255)),
        )

        for num in range(0,5,1):
            #print(num)
            button_rect.append(pygame.Rect((C.window['size'][0]-64*3*1 - 20, C.window['size'][1]-16*3*(num+1) - 10*(num+1),64*3,16*3),width=0))
            gui_surface.blit(C.assets['button'][-1], button_rect[num])
            gui_surface.blit(button_text[4-num],(C.window['size'][0]-64*2.5*1, C.window['size'][1]-16*2.87*(num+1) - 10*(num+1)))

        if C.gui['button_preclick'] == True:
            gui_surface.blit(C.assets['button'][-2], button_rect[C.gui['button_num']])
            gui_surface.blit(button_text[4-C.gui['button_num']],(C.window['size'][0]-64*2.5*1, C.window['size'][1]-16*2.87*(C.gui['button_num']+1) - 10*(C.gui['button_num']+1)))

        menu_main_surface = pygame.Surface(C.window['size']).convert_alpha()

        menu_main_surface.blit(background_surface, (0, 0))
        menu_main_surface.blit(gui_surface, (0, 0))
        
        C.screen.blit(menu_main_surface, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == VIDEORESIZE:
                C.window['size'] = event.dict['size']
                print(C.window['size'])

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                for num in range(0,5,1):
                    if pygame.Rect.collidepoint(button_rect[num],event.pos): 
                        C.gui['button_preclick'] = True
                        C.gui['button_num'] = num
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if pygame.Rect.collidepoint(button_rect[4],event.pos): 
                    print('新游戏')
                    C.window['page_switch']['game_main_page'] = True
                    C.window['page_switch']['menu_main_page'] = False

                if pygame.Rect.collidepoint(button_rect[3],event.pos): 
                    print('继续')
                    C.window['page_switch']['game_main_page'] = True
                    C.window['page_switch']['menu_main_page'] = False

                if pygame.Rect.collidepoint(button_rect[2],event.pos): 
                    print('设置')

                if pygame.Rect.collidepoint(button_rect[1],event.pos): 
                    print('退出')
                    pygame.quit()
                    sys.exit()

                if pygame.Rect.collidepoint(button_rect[0],event.pos): 
                    print('关于')
            


    @ staticmethod
    def game_main_surface():

        background_surface      = pygame.Surface(C.window['size']).convert_alpha()
        info_surface             = pygame.Surface(C.window['size']).convert_alpha()
        gui_surface             = pygame.Surface(C.window['size']).convert_alpha()

        background_surface.fill((255,55,55,0))
        background_surface.blit(C.assets['background'][-2], (0,0))

        info_surface.fill((255,55,55,0))

        gui_surface.fill((255,55,55,0))

        game_main_surface = pygame.Surface(C.window['size']).convert_alpha()

        game_main_surface.blit(background_surface, (0, 0))
        game_main_surface.blit(gui_surface, (0, 0))
        
        C.screen.blit(game_main_surface, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == VIDEORESIZE:
                C.window['size'] = event.dict['size']
                print(C.window['size'])
