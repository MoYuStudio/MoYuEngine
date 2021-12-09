
import random
import noise

class Tilemap:
    def __init__(self):
        self.config = {
                            'tile_id':{},
                            'hight':[],
                            'tilemap':[],
                            'boarder':64,
                            'tile_size':64,
                            'time_speed':100,
                            'octaves':2,
                            'freq':12,
                            'seed':0,
                        }

    def set(self):
        self.config['seed'] = random.randint(100000, 999999)

        # 0 tile land   1 tile preview   2 tile   3 time   4 buildable   5 tile button x   6 tile button y   7 Dv Code

        self.config['tilemap'] = [[[
                                            int(noise.pnoise2((x/self.config['freq'])+self.config['seed'],(y/self.config['freq'])+self.config['seed'],self.config['octaves'])*100+50),
                                            0,
                                            random.randint(0,200),
                                            0,
                                            0,
                                            0,
                                            0,
                                            0
                                        ] for x in range(0,self.config['boarder'],1)] for y in range(0,self.config['boarder'],1)]
        
        return self.config

    def blit(self,blit_surface,move=[0,0]):
        self.blit_surface = blit_surface
        self.move = move

        tilemap_n = len(self.config['tilemap'])
        tilemap_m = len(self.config['tilemap'][0])

        for tilemap_x in range(tilemap_n):
            for tilemap_y in range(tilemap_m):

                tile_info = self.config['tilemap'][tilemap_x][tilemap_y]

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

                    tile_info[5] = (tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0]

                # === 6 tile_pos_y ===

                    tile_info[6] = (tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]

                # === 7 tile_dvcode ===

                    tile_info[7] = 1

                    #print(tilemap)

                if tile_info[7] == 1:

                # === 0 tile_land ===

                    if tile_info[0] == 1:
                        self.blit_surface.blit(G.tl1,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))

                    if tile_info[0] == 6:
                        self.blit_surface.blit(G.tl6,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))

                    if tile_info[0] == 11:
                        self.blit_surface.blit(G.tl11,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))

                    if tile_info[0] == 16:
                        self.blit_surface.blit(G.tl16,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))

                    if tile_info[0] == 21:
                        self.blit_surface.blit(G.tl21,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))

                # === 1 tile_preview ===

                    if tile_info[1] == 0:
                        pass

                    if tile_info[1] == 1:
                        self.blit_surface.blit(G.pretile_choose,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1] - 1))
                        self.blit_surface.blit(G.pretile_green,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1] - 1))
                        if C.build == True:
                            tile_info[2] = C.tile_type
                            C.build = False

                    if tile_info[1] == 2:
                        self.blit_surface.blit(G.pretile_choose,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1] - 1))
                        self.blit_surface.blit(G.pretile_red,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1] - 1))

                    if tile_info[1] == 3:
                        self.blit_surface.blit(G.pretile_choose,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1] - 1))
                        if C.reward == True:
                            if tile_info[2] == 5:
                                tile_info[1] = 0
                                tile_info[2] = 1
                                tile_info[3] = 0
                                C.money += 80
                            C.reward = False

                    def tile_preview_top():

                        if tile_info[1] == 3:
                            self.blit_surface.blit(G.pretile_reward,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1] - 6))
                    
                # === 2 tile_building ===

                    if tile_info[2] == 0:
                        pass

                    if tile_info[2] == 1:
                        self.blit_surface.blit(G.t1,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))

                    if tile_info[2] == 2:
                        self.blit_surface.blit(G.t2,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))
                        tile_info[3] += self.config['time_speed']
                        if tile_info[3] >= 4000:
                            tile_info[2] = 3

                    if tile_info[2] == 3:
                        self.blit_surface.blit(G.t3,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))
                        tile_info[3] += self.config['time_speed']
                        if tile_info[3] >= 8000:
                            tile_info[2] = 4

                    if tile_info[2] == 4:
                        self.blit_surface.blit(G.t4,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))
                        tile_info[3] += self.config['time_speed']
                        if tile_info[3] >= 12000:
                            tile_info[2] = 5

                    if tile_info[2] == 5:
                        self.blit_surface.blit(G.t5,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1]))
                        tile_info[3] += self.config['time_speed']

                    if tile_info[2] == 105 and tile_info[0] == 6:
                        self.blit_surface.blit(G.t105,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))-32+self.move[1]))

                    if tile_info[2] == 155 and tile_info[0] == 16:
                        self.blit_surface.blit(G.t155,((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0],(tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))-32+self.move[1]))

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

                    # 16*self.blit_surface_level,9*self.blit_surface_level

                    tile_info[5] = ((tilemap_y*(self.config['tile_size']/2)-tilemap_x*(self.config['tile_size']/2))+self.move[0])*C.surface_level

                # === 6 tile_pos_y ===

                    tile_info[6] = ((tilemap_y*(self.config['tile_size']/4)+tilemap_x*(self.config['tile_size']/4))+self.move[1])*C.surface_level

                # === 7 tile_dvcode ===



if __name__ == "__main__":
    pass
