
import random
import noise

import data.constants as C

class TilemapSystem:
    def tilemap_builder():

        #random.seed(random.randint(100000000, 999999999))
        C.tilemap['seed'] = random.randint(100000, 999999)

        # 0 tile land   1 tile preview   2 tile   3 time   4 buildable   5 tile button x   6 tile button y   7 Dv Code
        C.tilemap['tilemap'] = [[[int(noise.pnoise2((x/C.tilemap['freq'])+C.tilemap['seed'],(y/C.tilemap['freq'])+C.tilemap['seed'],C.tilemap['octaves'])*100+50),0,random.randint(0,200),0,0,0,0,0] for x in range(0,C.tilemap['boarder'],1)] for y in range(0,C.tilemap['boarder'],1)]

    def tilemap_loarder(tilemap_surface,move_x,move_y):

        tilemap_surface.fill((255,55,55,0))

        tilemap_n = len(C.tilemap['tilemap'])
        tilemap_m = len(C.tilemap['tilemap'][0])

        for tilemap_x in range(tilemap_n):
            for tilemap_y in range(tilemap_m):

                tile_info = C.tilemap['tilemap'][tilemap_x][tilemap_y]

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

                    tile_info[5] = (tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x

                # === 6 tile_pos_y ===

                    tile_info[6] = (tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y

                # === 7 tile_dvcode ===

                    tile_info[7] = 1

                    #print(tilemap)

                if tile_info[7] == 1:

                # === 0 tile_land ===

                    if tile_info[0] == 1:
                        tilemap_surface.blit(C.assets['tileland'][-1],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))

                    if tile_info[0] == 6:
                        tilemap_surface.blit(C.assets['tileland'][-2],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))

                    if tile_info[0] == 11:
                        tilemap_surface.blit(C.assets['tileland'][-3],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))

                    if tile_info[0] == 16:
                        tilemap_surface.blit(C.assets['tileland'][-4],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))

                    if tile_info[0] == 21:
                        tilemap_surface.blit(C.assets['tileland'][-5],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))

                # # === 1 tile_preview ===

                #     if tile_info[1] == 0:
                #         pass

                #     if tile_info[1] == 1:
                #         tilemap_surface.blit(G.pretile_choose,((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y - 1))
                #         tilemap_surface.blit(G.pretile_green,((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y - 1))
                #         if C.build == True:
                #             tile_info[2] = C.tile_type
                #             C.build = False

                #     if tile_info[1] == 2:
                #         tilemap_surface.blit(G.pretile_choose,((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y - 1))
                #         tilemap_surface.blit(G.pretile_red,((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y - 1))

                #     if tile_info[1] == 3:
                #         tilemap_surface.blit(G.pretile_choose,((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y - 1))
                #         if C.reward == True:
                #             if tile_info[2] == 5:
                #                 tile_info[1] = 0
                #                 tile_info[2] = 1
                #                 tile_info[3] = 0
                #                 C.money += 80
                #             C.reward = False

                #     def tile_preview_top():

                #         if tile_info[1] == 3:
                #             tilemap_surface.blit(G.pretile_reward,((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y - 6))
                    
                # # === 2 tile_building ===

                    if tile_info[2] == 0:
                        pass

                    if tile_info[2] == 1:
                        tilemap_surface.blit(C.assets['tilebuilding'][-2],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))

                    if tile_info[2] == 2:
                        tilemap_surface.blit(C.assets['tilebuilding'][-3],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))
                        tile_info[3] += C.time_speed
                        if tile_info[3] >= 4000:
                            tile_info[2] = 3

                    if tile_info[2] == 3:
                        tilemap_surface.blit(C.assets['tilebuilding'][-4],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))
                        tile_info[3] += C.time_speed
                        if tile_info[3] >= 8000:
                            tile_info[2] = 4

                    if tile_info[2] == 4:
                        tilemap_surface.blit(C.assets['tilebuilding'][-5],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))
                        tile_info[3] += C.time_speed
                        if tile_info[3] >= 12000:
                            tile_info[2] = 5

                    if tile_info[2] == 5:
                        tilemap_surface.blit(C.assets['tilebuilding'][-6],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y))
                        tile_info[3] += C.time_speed

                    if tile_info[2] == 105 and tile_info[0] == 6:
                        tilemap_surface.blit(C.assets['tilebuilding'][-7],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))-32+move_y))

                    if tile_info[2] == 155 and tile_info[0] == 16:
                        tilemap_surface.blit(C.assets['tilebuilding'][-8],((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x,(tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))-32+move_y))

                # # === 1 tile_preview top ===

                #     tile_preview_top()

                # # === 3 tile_time ===

                # # === 4 tile_buildable ===

                #     if C.tile_type == 1:
                #         if tile_info[0] == 1 or \
                #         tile_info[0] == 6:

                #             tile_info[4] = 1

                #         else:
                #             tile_info[4] = 0

                #     if C.tile_type == 2:
                #         if tile_info[2] == 1:
                #             tile_info[4] = 1
                #         else:
                #             tile_info[4] = 0

                # # === 5 tile_pos_x ===

                #     # 16*tilemap_surface_level,9*tilemap_surface_level

                #     tile_info[5] = ((tilemap_y*(C.tilemap['tile_size']/2)-tilemap_x*(C.tilemap['tile_size']/2))+move_x)*C.surface_level

                # # === 6 tile_pos_y ===

                #     tile_info[6] = ((tilemap_y*(C.tilemap['tile_size']/4)+tilemap_x*(C.tilemap['tile_size']/4))+move_y)*C.surface_level

                # # === 7 tile_dvcode ===

    def tilemap_clicker():
        pass
