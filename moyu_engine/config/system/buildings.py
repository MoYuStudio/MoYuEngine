
import random
import noise
import pygame

import system.setting as S
import system.assets as A

class TileMap_Manager:
    def __init__(self):
        
        self.tile_size = 64

        self.freq = 2
        self.octaves = 12

    def tilemap_builder(self):

        #random.seed(random.randint(100000000, 999999999))

        S.SEED = random.randint(100000, 999999)

        # 0 tile land   1 tile preview   2 tile   3 time   4 buildable   5 tile button x   6 tile button y   7 Dv Code

        S.TILEMAP = [[[int(noise.pnoise2((x/self.freq)+S.SEED,(y/self.freq)+S.SEED,self.octaves)*100+50),0,random.randint(0,200),0,0,0,0,0] for x in range(0,S.BOARDER,1)] for y in range(0,S.BOARDER,1)]

    def tilemap_loarder(self, tilemap_surface, move_x, move_y):

        tilemap_surface.fill((0,0,0,0))

        tilemap_n = len(S.TILEMAP)
        tilemap_m = len(S.TILEMAP[0])

        for tilemap_x in range(tilemap_n):
            for tilemap_y in range(tilemap_m):

                tile_info = S.TILEMAP[tilemap_x][tilemap_y]

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

                    tile_info[5] = (tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x

                # === 6 tile_pos_y ===

                    tile_info[6] = (tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y

                # === 7 tile_dvcode ===

                    tile_info[7] = 1

                    #print(tilemap)

                if tile_info[7] == 1:

                # === 0 tile_land ===

                    if tile_info[0] == 1:
                        tilemap_surface.blit(A.tl1,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))

                    if tile_info[0] == 6:
                        tilemap_surface.blit(A.tl6,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))

                    if tile_info[0] == 11:
                        tilemap_surface.blit(A.tl11,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))

                    if tile_info[0] == 16:
                        tilemap_surface.blit(A.tl16,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))

                    if tile_info[0] == 21:
                        tilemap_surface.blit(A.tl21,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))

                # === 1 tile_preview ===

                    if tile_info[1] == 0:
                        pass

                    if tile_info[1] == 1:
                        tilemap_surface.blit(A.pretile_choose,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y - 1))
                        tilemap_surface.blit(A.pretile_green,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y - 1))
                        if S.build == True:
                            tile_info[2] = S.tile_type
                            S.build = False

                    if tile_info[1] == 2:
                        tilemap_surface.blit(A.pretile_choose,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y - 1))
                        tilemap_surface.blit(A.pretile_red,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y - 1))

                    if tile_info[1] == 3:
                        tilemap_surface.blit(A.pretile_choose,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y - 1))
                        if S.REWARD == True:
                            if tile_info[2] == 5:
                                tile_info[1] = 0
                                tile_info[2] = 1
                                tile_info[3] = 0
                                S.MONEY += 80
                            S.REWARD = False

                    def tile_preview_top():

                        if tile_info[1] == 3:
                            tilemap_surface.blit(A.pretile_reward,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y - 6))
                    
                # === 2 tile_building ===

                    if tile_info[2] == 0:
                        pass

                    if tile_info[2] == 1:
                        tilemap_surface.blit(A.t1,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))

                    if tile_info[2] == 2:
                        tilemap_surface.blit(A.t2,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))
                        tile_info[3] += S.TIME_SPEED
                        if tile_info[3] >= 4000:
                            tile_info[2] = 3

                    if tile_info[2] == 3:
                        tilemap_surface.blit(A.t3,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))
                        tile_info[3] += S.TIME_SPEED
                        if tile_info[3] >= 8000:
                            tile_info[2] = 4

                    if tile_info[2] == 4:
                        tilemap_surface.blit(A.t4,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))
                        tile_info[3] += S.TIME_SPEED
                        if tile_info[3] >= 12000:
                            tile_info[2] = 5

                    if tile_info[2] == 5:
                        tilemap_surface.blit(A.t5,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y))
                        tile_info[3] += S.TIME_SPEED

                    if tile_info[2] == 105 and tile_info[0] == 6:
                        tilemap_surface.blit(A.t105,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))-32+move_y))

                    if tile_info[2] == 155 and tile_info[0] == 16:
                        tilemap_surface.blit(A.t155,((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x,(tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))-32+move_y))

                # === 1 tile_preview top ===

                    tile_preview_top()

                # === 3 tile_time ===

                # === 4 tile_buildable ===

                    if S.tile_type == 1:
                        if tile_info[0] == 1 or \
                        tile_info[0] == 6:

                            tile_info[4] = 1

                        else:
                            tile_info[4] = 0

                    if S.tile_type == 2:
                        if tile_info[2] == 1:
                            tile_info[4] = 1
                        else:
                            tile_info[4] = 0

                # === 5 tile_pos_x ===

                    # 16*tilemap_surface_level,9*tilemap_surface_level

                    tile_info[5] = ((tilemap_y*(self.tile_size/2)-tilemap_x*(self.tile_size/2))+move_x)*S.surface_level

                # === 6 tile_pos_y ===

                    tile_info[6] = ((tilemap_y*(self.tile_size/4)+tilemap_x*(self.tile_size/4))+move_y)*S.surface_level

                # === 7 tile_dvcode ===

'''
    def tilebutton_clicker_event_MOUSEBUTTONDOWN():

        tilemap_n = len(S.TILEMAP)
        tilemap_m = len(S.TILEMAP[0])

        for tilemap_x in range(tilemap_n):
            for tilemap_y in range(tilemap_m):

                tile_info = S.TILEMAP[tilemap_x][tilemap_y]
    
                if tile_info[5] + 8*C.surface_level <= C.mouse_down_pos_x <= tile_info[5] + C.tile_size*C.surface_level - 8*C.surface_level \
                    and tile_info[6] + 8*C.surface_level <= C.mouse_down_pos_y <= tile_info[6] + C.tile_size*C.surface_level - 8*C.surface_level:

                    else:
                        if C.tile_choose == True:

                            (S.TILEMAP[C.tile_choose_info[0]][C.tile_choose_info[1]])[1] = 0
                            C.tile_choose = False
                            
                        if tile_info[4] == 1:

                            (S.TILEMAP[tilemap_x][tilemap_y])[1] = 1

                        if tile_info[4] == 0:

                            (S.TILEMAP[tilemap_x][tilemap_y])[1] = 2

                        if tile_info[3] >= 12000:

                            (S.TILEMAP[tilemap_x][tilemap_y])[1] = 3

                        C.tile_choose_info = [tilemap_x,tilemap_y,((S.TILEMAP[tilemap_x][tilemap_y])[4])]

                        C.tile_choose = True

                        if tile_info[2] == 0:
                            pass
                        else:
                            C.pretile_type = tile_info[2]
'''