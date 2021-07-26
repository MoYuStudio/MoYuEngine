
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F
import components.tilemap_manager
import components.tilebutton
import components.window_move

def run():
    init()
    gameloop()

def init():

    pygame.init()

    C.mainwindow = pygame.display.set_mode((1200,600))
    C.window_title = pygame.display.set_caption('TinyLand 弹丸之地')
    pygame.display.set_icon(G.tl6)
    C.clock = pygame.time.Clock()
    pygame.display.flip()

    return C.mainwindow,C.window_title,C.clock

def gameloop():

    components.tilemap_manager.tilemap_builder()

    while True:

        G.tl1Fin = pygame.transform.scale(G.tl1, (64 * C.tile_level,64 * C.tile_level))

        G.tl6Fin = pygame.transform.scale(G.tl6, (64 * C.tile_level,64 * C.tile_level))

        G.tl11Fin = pygame.transform.scale(G.tl11, (64 * C.tile_level,64 * C.tile_level))

        G.tl16Fin = pygame.transform.scale(G.tl16, (64 * C.tile_level,64 * C.tile_level))

        G.tl21Fin = pygame.transform.scale(G.tl21, (64 * C.tile_level,64 * C.tile_level))

        G.t105Fin = pygame.transform.scale(G.t105, (64 * C.tile_level,48 * C.tile_level))

        G.pretile_chooseFin = pygame.transform.scale(G.pretile_choose, (64 * C.tile_level,32 * C.tile_level))

        G.pretile_greenFin = pygame.transform.scale(G.pretile_green, (64 * C.tile_level,32 * C.tile_level))

        G.pretile_redFin = pygame.transform.scale(G.pretile_red, (64 * C.tile_level,32 * C.tile_level))
        
        C.tile_size = 64*C.tile_level

        F.font1 = pygame.font.Font('moyu_engine/assets/font/方正像素16.TTF', 10 * C.tile_level)

        C.mainwindow.fill((0,0,0))

        components.tilemap_manager.tilemap_loarder()

        components.window_move.move_Fn()

        components.tilebutton.tile_preview(C.tile_choose_info) 

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:

                C.mouse_pos_x,C.mouse_pos_y = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:

                C.mouse_pos_x,C.mouse_pos_y = event.pos
                
                components.tilebutton.tilebutton_clicker(C.mouse_pos_x,C.mouse_pos_y)

            if event.type == pygame.KEYDOWN:
        
                if event.key == K_UP or event.key == K_w:
                    C.move_up = True
                    
                if event.key == K_DOWN or event.key == K_s:
                    C.move_down = True

                if event.key == K_LEFT or event.key == K_a:
                    C.move_left = True

                if event.key == K_RIGHT or event.key == K_d:
                    C.move_right = True

                if event.key == K_q:
                    C.tile_level += 1

                    components.tilebutton.tilebutton_clicker(C.mouse_pos_x,C.mouse_pos_y)

                if event.key == K_e:
                    if C.tile_level == 1:
                        C.tile_level = 1
                    else:
                        C.tile_level -= 1

                    components.tilebutton.tilebutton_clicker(C.mouse_pos_x,C.mouse_pos_y)

                if event.key == K_z:
                    C.tile_level = 1
                    C.move_x,C.move_y = 19*30,3*30

                if event.key == K_x:
                    components.tilemap_manager.tilemap_builder()

            if event.type == pygame.KEYUP:

                if event.key == K_UP or event.key == K_w:
                    C.move_up = False

                if event.key == K_DOWN or event.key == K_s:
                    C.move_down = False

                if event.key == K_LEFT or event.key == K_a:
                    C.move_left = False

                if event.key == K_RIGHT or event.key == K_d:
                    C.move_right = False

        C.clock.tick(60)

run()