
import constants as C
import graphics as G

def tilebutton_clicker_event():

    tilemap_n = len(C.tilemap)
    tilemap_m = len(C.tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = C.tilemap[tilemap_x][tilemap_y]

            if tile_info[5] <= C.mouse_down_pos_x <= tile_info[5] + C.tile_size*(1280/C.game_main_surface_size[0]) and tile_info[6] <= C.mouse_down_pos_y <= tile_info[6] + C.tile_size*(720/C.game_main_surface_size[1]):

                if C.tile_choose == True:

                    (C.tilemap[C.tile_choose_info[0]][C.tile_choose_info[1]])[2] = 0

                (C.tilemap[tilemap_x][tilemap_y])[2] = 1

                C.tile_choose_info = [tilemap_x,tilemap_y,((C.tilemap[tilemap_x][tilemap_y])[4])]

                C.tile_choose = True

                print('='*30)

                print(C.game_main_surface_level)
                print(tile_info[5],tile_info[6])
                print(C.game_main_surface_size)
                print(C.tile_size*(1280/C.game_main_surface_size[0]))
                print(1+(1-(1280/C.game_main_surface_size[0])))

                '''

                C.mouse_x,C.mouse_y = (tile_info[4]-C.move_x),(tile_info[5]-C.move_y)

                C.tile_choose_info = tile_info

                print(C.tile_choose_info)

                '''