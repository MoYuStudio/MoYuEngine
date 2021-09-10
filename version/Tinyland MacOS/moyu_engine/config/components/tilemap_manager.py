
import random

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

def tilemap_builder():

    # 0 tile land   1 tile preview   2 tile   3 time   4 buildable   5 tile button x   6 tile button y   7 Dv Code

    C.tilemap = [[[random.randint(0,600),0,random.randint(0,100),0,0,0,0,0,0] for i in range(0,C.boarder,1)] for j in range(0,C.boarder,1)]


def tilemap_loarder():

    tilemap_n = len(C.tilemap)
    tilemap_m = len(C.tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = C.tilemap[tilemap_x][tilemap_y]

            if tile_info[7] == 0:

            # === 0 tile_land ===
                
                if 0<=tile_info[0]<=50:
                    tile_info[0] = 1
            
                if 51<=tile_info[0]<=500:
                    tile_info[0] = 6
                            
                if 501<=tile_info[0]<=520:
                    tile_info[0] = 11
                    
                if 521<=tile_info[0]<=530:
                    tile_info[0] = 16
                    
                if 531<=tile_info[0]<=600:
                    tile_info[0] = 21

            # === 1 tile_preview ===

            # === 2 tile_building ===

                if 0<=tile_info[2]<=70:
                    tile_info[2] = 0

                if 71<=tile_info[2]<=100 and tile_info[0] == 6:
                    tile_info[2] = 105

            # === 3 tile_time ===

            # === 4 tile_buildable ===

            # === 5 tile_pos_x ===

                tile_info[5] = (tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x

            # === 6 tile_pos_y ===

                tile_info[6] = (tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y

            # === 7 tile_dvcode ===

                tile_info[7] = 1

                #print(tilemap)

            if tile_info[7] == 1:

            # === 0 tile_land ===

                if tile_info[0] == 1:
                    C.game_main_surface.blit(G.tl1,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))

                if tile_info[0] == 6:
                    C.game_main_surface.blit(G.tl6,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))

                if tile_info[0] == 11:
                    C.game_main_surface.blit(G.tl11,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))

                if tile_info[0] == 16:
                    C.game_main_surface.blit(G.tl16,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))

                if tile_info[0] == 21:
                    C.game_main_surface.blit(G.tl21,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))

            # === 1 tile_preview ===

                if tile_info[1] == 0:
                    pass

                if tile_info[1] == 1:
                    C.game_main_surface.blit(G.pretile_choose,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y - 1))
                    C.game_main_surface.blit(G.pretile_green,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y - 1))
                    if C.build == True:
                        tile_info[2] = C.tile_type
                        C.build = False

                if tile_info[1] == 2:
                    C.game_main_surface.blit(G.pretile_choose,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y - 1))
                    C.game_main_surface.blit(G.pretile_red,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y - 1))

                if tile_info[1] == 3:
                    C.game_main_surface.blit(G.pretile_choose,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y - 1))
                    if C.reward == True:
                        if tile_info[2] == 5:
                            tile_info[1] = 0
                            tile_info[2] = 1
                            tile_info[3] = 0
                            C.money += 80
                        C.reward = False

                def tile_preview_top():

                    if tile_info[1] == 3:
                        C.game_main_surface.blit(G.pretile_reward,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y - 6))
                   
            # === 2 tile_building ===

                if tile_info[2] == 0:
                    pass

                if tile_info[2] == 1:
                    C.game_main_surface.blit(G.t1,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))

                if tile_info[2] == 2:
                    C.game_main_surface.blit(G.t2,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))
                    tile_info[3] += C.time_speed
                    if tile_info[3] >= 4000:
                        tile_info[2] = 3

                if tile_info[2] == 3:
                    C.game_main_surface.blit(G.t3,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))
                    tile_info[3] += C.time_speed
                    if tile_info[3] >= 8000:
                        tile_info[2] = 4

                if tile_info[2] == 4:
                    C.game_main_surface.blit(G.t4,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))
                    tile_info[3] += C.time_speed
                    if tile_info[3] >= 12000:
                        tile_info[2] = 5

                if tile_info[2] == 5:
                    C.game_main_surface.blit(G.t5,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y))
                    tile_info[3] += C.time_speed

                if tile_info[2] == 105:
                    C.game_main_surface.blit(G.t105,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x,(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))-16+C.move_y))

            # === 1 tile_preview top ===

                tile_preview_top()

            # === 3 tile_time ===

            # === 4 tile_buildable ===

                if C.tile_type == 1:
                    if tile_info[0] == 1 or \
                       tile_info[0] == 6:

                        tile_info[4] = 1

                    else:
                        tile_info[4] = 0

                if C.tile_type == 2:
                    if tile_info[2] == 1:
                        tile_info[4] = 1
                    else:
                        tile_info[4] = 0

            # === 5 tile_pos_x ===

                # 16*C.game_main_surface_level,9*C.game_main_surface_level

                tile_info[5] = ((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.move_x)*C.surface_level

            # === 6 tile_pos_y ===

                tile_info[6] = ((tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.move_y)*C.surface_level

            # === 7 tile_dvcode ===


