
import constants as C
import graphics as G

def tilebutton_clicker_surface():
    pass

def tilebutton_clicker_event():

    tilemap_n = len(C.tilemap)
    tilemap_m = len(C.tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = C.tilemap[tilemap_x][tilemap_y]

            if tile_info[4] <= C.mouse_down_pos_x <= tile_info[4] + C.tile_size and tile_info[5] <= C.mouse_down_pos_y <= tile_info[5] + C.tile_size:
                C.mouse_x,C.mouse_y = (tile_info[4]-C.move_x),(tile_info[5]-C.move_y)

                C.tile_choose_info = tile_info

                print('233')