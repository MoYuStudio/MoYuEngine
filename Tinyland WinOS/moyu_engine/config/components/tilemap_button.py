
import pygame

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G

def tilebutton_clicker_event_MOUSEBUTTONDOWN():

    tilemap_n = len(C.tilemap)
    tilemap_m = len(C.tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = C.tilemap[tilemap_x][tilemap_y]
 
            if tile_info[5] + 8*C.surface_level <= C.mouse_down_pos_x <= tile_info[5] + C.tile_size*C.surface_level - 8*C.surface_level \
                and tile_info[6] + 8*C.surface_level <= C.mouse_down_pos_y <= tile_info[6] + C.tile_size*C.surface_level - 8*C.surface_level:

                if pygame.Rect.collidepoint(C.bar_button01_rect,(C.mouse_down_pos_x,C.mouse_down_pos_y))or\
                   pygame.Rect.collidepoint(C.bar_button02_rect,(C.mouse_down_pos_x,C.mouse_down_pos_y))or\
                   pygame.Rect.collidepoint(C.bar_button03_rect,(C.mouse_down_pos_x,C.mouse_down_pos_y))or\
                   pygame.Rect.collidepoint(C.bar_button04_rect,(C.mouse_down_pos_x,C.mouse_down_pos_y))or\
                   pygame.Rect.collidepoint(C.bar_button05_rect,(C.mouse_down_pos_x,C.mouse_down_pos_y)):
                    pass

                else:
                    if C.tile_choose == True:

                        (C.tilemap[C.tile_choose_info[0]][C.tile_choose_info[1]])[1] = 0
                        C.tile_choose = False
                        
                    if tile_info[4] == 1:

                        (C.tilemap[tilemap_x][tilemap_y])[1] = 1

                    if tile_info[4] == 0:

                        (C.tilemap[tilemap_x][tilemap_y])[1] = 2

                    if tile_info[3] >= 12000:

                        (C.tilemap[tilemap_x][tilemap_y])[1] = 3

                    C.tile_choose_info = [tilemap_x,tilemap_y,((C.tilemap[tilemap_x][tilemap_y])[4])]

                    C.tile_choose = True

                    if tile_info[2] == 0:
                        pass
                    else:
                        C.pretile_type = tile_info[2]