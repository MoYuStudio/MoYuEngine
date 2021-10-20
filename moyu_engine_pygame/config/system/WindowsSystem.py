
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
            C.assets['zh'][-2].render('新游戏', True, (255, 255, 255)),
            C.assets['zh'][-2].render('继续', True, (255, 255, 255)),
            C.assets['zh'][-2].render('设置', True, (255, 255, 255)),
            C.assets['zh'][-2].render('退出', True, (255, 255, 255)),
            C.assets['zh'][-2].render('关于', True, (255, 255, 255)),
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

        system.TransitionSystem.fade_black()

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
                    C.transition['fade_black'] = True
                    
                    if C.window['page_switch']['switch'] == True:
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
        info_surface             = pygame.Surface((int(C.window['set_size'][0]/C.window['surface_level']),int(C.window['set_size'][1]/C.window['surface_level']))).convert_alpha()
        gui_surface             = pygame.Surface(C.window['size']).convert_alpha()

        background_surface.fill((255,55,55,0))
        background_surface.blit(C.assets['background'][-2],(-C.window['move'][0],-C.window['move'][1]))

        info_surface.fill((255,55,55,0))
        system.TilemapSystem.tilemap_loarder(info_surface,C.window['move'][0],C.window['move'][1])

        gui_surface.fill((255,55,55,0))

        info_surfaceFin = pygame.transform.scale(info_surface,(C.window['size']))

        game_main_surface = pygame.Surface(C.window['size']).convert_alpha()

        game_main_surface.blit(background_surface, (0, 0))
        game_main_surface.blit(info_surfaceFin, (0, 0))
        game_main_surface.blit(gui_surface, (0, 0))
        
        C.screen.blit(game_main_surface, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == VIDEORESIZE:
                C.window['size'] = event.dict['size']
                print(C.window['size'])

            if event.type == pygame.KEYDOWN:

                if event.key == K_UP or event.key == K_w:
                    C.window['move_switch']['up']   = True
                    
                if event.key == K_DOWN or event.key == K_s:
                    C.window['move_switch']['down'] = True

                if event.key == K_LEFT or event.key == K_a:
                    C.window['move_switch']['left'] = True

                if event.key == K_RIGHT or event.key == K_d:
                    C.window['move_switch']['right'] = True

                if event.key == K_q:
                    C.window['zoom_switch']['in']   = True

                if event.key == K_e:
                    C.window['zoom_switch']['out']  = True

                # if event.key == K_b:
                #     C.build        = True
                # if C.tile_type == 1:
                #     C.money       -= 30
                # if C.tile_type == 2:
                #     C.money       -= 5

                # if event.key == K_r:
                #     C.reward    = True

                # if event.key == K_z:
                #     C.GAMEmain_surface_level = 60
                #     C.MOVE_SPEED             = 10
                #     C.MOVE                   = [450,5]

                # if event.key == K_x:
                #     moyu_engine.config.components.tilemap_manager.tilemap_builder()

                # if event.key == K_m:
                #     moyu_engine.config.components.save_data.save_tilemap()
                
                # if event.key == K_n:
                #     moyu_engine.config.components.read_data.read_tilemap()

            if event.type == pygame.KEYUP:

                if event.key == K_UP or event.key == K_w:
                    C.window['move_switch']['up']   = False

                if event.key == K_DOWN or event.key == K_s:
                    C.window['move_switch']['down'] = False

                if event.key == K_LEFT or event.key == K_a:
                    C.window['move_switch']['left'] = False

                if event.key == K_RIGHT or event.key == K_d:
                    C.window['move_switch']['right'] = False

                if event.key == K_q:
                    C.window['zoom_switch']['in']   = False

                if event.key == K_e:
                    C.window['zoom_switch']['out'] = False

                # if event.key == K_b:
                #     C.build     = False

                # if event.key == K_r:
                #     C.reward    = False
