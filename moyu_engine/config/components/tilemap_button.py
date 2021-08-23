
import constants as C
import graphics as G

def tilebutton_clicker_surface():

    if C.tile_choose_info[2] == 0:
        C.buildable_preview = False

    if C.tile_choose_info[2] == 1:
        C.buildable_preview = True

    if C.buildable_preview == False:
        C.game_main_surface.blit(G.pretile_red,(C.mouse_x+C.move_x,C.mouse_y+C.move_y)) 

    if C.buildable_preview == True:
        C.game_main_surface.blit(G.pretile_green,(C.mouse_x+C.move_x,C.mouse_y+C.move_y))

    C.game_main_surface.blit(G.pretile_choose,(C.mouse_x+C.move_x,C.mouse_y+C.move_y))

def tilebutton_clicker_event():

    tilemap_n = len(C.tilemap)
    tilemap_m = len(C.tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = C.tilemap[tilemap_x][tilemap_y]

            if tile_info[5]-C.tile_size/2 <= C.mouse_down_pos_x <= tile_info[5]-C.tile_size/2 + C.tile_size and tile_info[6]-C.tile_size/4 <= C.mouse_down_pos_y <= tile_info[6]-C.tile_size/4 + C.tile_size:

                if C.tile_choose == True:

                    (C.tilemap[C.tile_choose_info[0]][C.tile_choose_info[1]])[2] = 0

                (C.tilemap[tilemap_x][tilemap_y])[2] = 1

                C.tile_choose_info = [tilemap_x,tilemap_y,((C.tilemap[tilemap_x][tilemap_y])[4])]

                C.tile_choose = True

                '''

                C.mouse_x,C.mouse_y = (tile_info[4]-C.move_x),(tile_info[5]-C.move_y)

                C.tile_choose_info = tile_info

                print(C.tile_choose_info)

                '''