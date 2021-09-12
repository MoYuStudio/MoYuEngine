
import random
import noise

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

def tilemap_builder():

    #random.seed(random.randint(100000000, 999999999))

    C.seed = random.randint(100000, 999999)

    # 0 tile land   1 tile preview   2 tile   3 time   4 buildable   5 tile button x   6 tile button y   7 Dv Code

    C.tilemap = [[[int(noise.pnoise2((x/C.freq)+C.seed,(y/C.freq)+C.seed,C.octaves)*100+50),0,random.randint(0,200),0,0,0,0,0] for x in range(0,C.boarder,1)] for y in range(0,C.boarder,1)]

def tilemap_loarder():

    tilemap_n = len(C.tilemap)
    tilemap_m = len(C.tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = C.tilemap[tilemap_x][tilemap_y]

            if tile_info[7] == 0:

            # === 0 tile_land ===

                #print(tile_info[0])

                if -100 <=tile_info[0]<= 37:
                    tile_info[0] = 21
            
                if 38 <=tile_info[0]<= 40:
                    tile_info[0] = 11
                    
                if 41 <=tile_info[0]<= 65:
                    tile_info[0] = 6
                    
                if 66 <=tile_info[0]<= 70:
                    tile_info[0] = 1 
                    
                if 70 <=tile_info[0]<= 110:
                    tile_info[0] = 16

            # === 1 tile_preview ===

            # === 2 tile_building ===

                if 0<=tile_info[2]<=30:
                    tile_info[2] = 0

                if 31<=tile_info[2]<=100 and tile_info[0] == 6:
                    tile_info[2] = 105

                if 101<=tile_info[2]<=200 and tile_info[0] == 16:
                    tile_info[2] = 155

            # === 3 tile_time ===

            # === 4 tile_buildable ===

            # === 5 tile_pos_x ===

                tile_info[5] = (tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0]

            # === 6 tile_pos_y ===

                tile_info[6] = (tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]

            # === 7 tile_dvcode ===

                tile_info[7] = 1

                #print(tilemap)

            if tile_info[7] == 1:

            # === 0 tile_land ===

                if tile_info[0] == 1:
                    C.tilemap_surface.blit(G.tl1,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))

                if tile_info[0] == 6:
                    C.tilemap_surface.blit(G.tl6,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))

                if tile_info[0] == 11:
                    C.tilemap_surface.blit(G.tl11,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))

                if tile_info[0] == 16:
                    C.tilemap_surface.blit(G.tl16,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))

                if tile_info[0] == 21:
                    C.tilemap_surface.blit(G.tl21,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))

            # === 1 tile_preview ===

                if tile_info[1] == 0:
                    pass

                if tile_info[1] == 1:
                    C.tilemap_surface.blit(G.pretile_choose,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1] - 1))
                    C.tilemap_surface.blit(G.pretile_green,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1] - 1))
                    if C.build == True:
                        tile_info[2] = C.tile_type
                        C.build = False

                if tile_info[1] == 2:
                    C.tilemap_surface.blit(G.pretile_choose,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1] - 1))
                    C.tilemap_surface.blit(G.pretile_red,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1] - 1))

                if tile_info[1] == 3:
                    C.tilemap_surface.blit(G.pretile_choose,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1] - 1))
                    if C.reward == True:
                        if tile_info[2] == 5:
                            tile_info[1] = 0
                            tile_info[2] = 1
                            tile_info[3] = 0
                            C.money += 80
                        C.reward = False

                def tile_preview_top():

                    if tile_info[1] == 3:
                        C.tilemap_surface.blit(G.pretile_reward,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1] - 6))
                   
            # === 2 tile_building ===

                if tile_info[2] == 0:
                    pass

                if tile_info[2] == 1:
                    C.tilemap_surface.blit(G.t1,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))

                if tile_info[2] == 2:
                    C.tilemap_surface.blit(G.t2,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))
                    tile_info[3] += C.time_speed
                    if tile_info[3] >= 4000:
                        tile_info[2] = 3

                if tile_info[2] == 3:
                    C.tilemap_surface.blit(G.t3,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))
                    tile_info[3] += C.time_speed
                    if tile_info[3] >= 8000:
                        tile_info[2] = 4

                if tile_info[2] == 4:
                    C.tilemap_surface.blit(G.t4,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))
                    tile_info[3] += C.time_speed
                    if tile_info[3] >= 12000:
                        tile_info[2] = 5

                if tile_info[2] == 5:
                    C.tilemap_surface.blit(G.t5,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1]))
                    tile_info[3] += C.time_speed

                if tile_info[2] == 105 and tile_info[0] == 6:
                    C.tilemap_surface.blit(G.t105,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))-32+C.MOVE[1]))

                if tile_info[2] == 155 and tile_info[0] == 16:
                    C.tilemap_surface.blit(G.t155,((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0],(tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))-32+C.MOVE[1]))

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

                # 16*C.tilemap_surface_level,9*C.tilemap_surface_level

                tile_info[5] = ((tilemap_y*(C.tile_size/2)-tilemap_x*(C.tile_size/2))+C.MOVE[0])*C.surface_level

            # === 6 tile_pos_y ===

                tile_info[6] = ((tilemap_y*(C.tile_size/4)+tilemap_x*(C.tile_size/4))+C.MOVE[1])*C.surface_level

            # === 7 tile_dvcode ===


