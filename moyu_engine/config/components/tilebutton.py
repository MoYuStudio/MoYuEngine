
import constants as C
import graphics as G

def tilebutton_clicker(mouse_pos_x,mouse_pos_y):

    tilemap_n = len(C.tilemap)
    tilemap_m = len(C.tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = C.tilemap[tilemap_x][tilemap_y]

            if tile_info[4]+8*C.tile_level <= mouse_pos_x <= tile_info[4]+8*C.tile_level + C.tile_size and tile_info[5]+8*C.tile_level <= mouse_pos_y <= tile_info[5]+8*C.tile_level + C.tile_size:
                C.mouse_x,C.mouse_y = (tile_info[4]-C.move_x),(tile_info[5]-C.move_y)

                C.tile_choose_info = tile_info

    return C.mouse_x,C.mouse_y,C.tile_choose_info

def tile_preview(tile_choose_info):

    if tile_choose_info[3] == 0:
        C.buildable_preview = False

    if tile_choose_info[3] == 1:
        C.buildable_preview = True

    if C.buildable_preview == False:
        C.mainwindow.blit(G.pretile_redFin,(C.mouse_x+C.move_x,C.mouse_y+C.move_y)) 

    if C.buildable_preview == True:
        C.mainwindow.blit(G.pretile_greenFin,(C.mouse_x+C.move_x,C.mouse_y+C.move_y))

    C.mainwindow.blit(G.pretile_chooseFin,(C.mouse_x+C.move_x,C.mouse_y+C.move_y))

    return C.buildable_preview